
#################################################################################
#
# {___     {__          {__       {__
# {_ {__   {__          {_ {__   {___
# {__ {__  {__   {__    {__ {__ { {__
# {__  {__ {__ {__  {__ {__  {__  {__
# {__   {_ {__{__    {__{__   {_  {__
# {__    {_ __ {__  {__ {__       {__
# {__      {__   {__    {__       {__
#
# (C) Copyright European Space Agency, 2024
# 
# This file is subject to the terms and conditions defined in file 'LICENCE.txt', 
# which is part of this source code package. No part of the package, including 
# this file, may be copied, modified, propagated, or distributed except 
# according to the terms contained in the file ‘LICENCE.txt’.“ 
#
#################################################################################

import json
import time
from functools import wraps

from flask import current_app , request , Response , g as _g , redirect , url_for

from esanom import database as _database , config as _config, util as _util

####################################################################

ROUTES_VERSION = 3

####################################################################

def response_default( messages = False ) :

    res = {
        "VERSION" : ROUTES_VERSION ,
        "TIME" : time.time( ) ,
        "STATUS" : "OK" ,
        "MESSAGES" : { } 
    }

    if messages is not False : res[ "MESSAGES" ] = messages

    return( Response( json.dumps( res , default = str ) , status = 200 , mimetype = "application/json" ) )

def response_error( e_msg = "GENERAL" , e_code = 99999 , http_code = 400 ) :

    current_app.logger.warning( f"{e_code},{e_msg}" )

    return(
        Response(
            json.dumps( {
                "VERSION" : ROUTES_VERSION ,
                "TIME" : time.time( ) ,
                "STATUS" : "ERROR" ,
                "ERROR_MESSAGE" : e_msg ,
                "ERROR_CODE" : e_code ,
                "MESSAGES" : { } 
            } , default = str ) ,
            status = http_code , mimetype = "application/json"
        )
    )

####################################################################

def decorator_token_required( f ) :

    @wraps( f )
    def decorator_function( *args , **kwargs ) :

        if not "Authorization" in request.headers : return( response_error( e_msg = "No token supplied" , e_code = 9102 , http_code = 401 ) )

        ####

        authorization_header = request.headers.get( "Authorization" )
        authorization_header_parts = authorization_header.split( " " )

        if len( authorization_header_parts ) != 2 : return( response_error( e_msg = "authorization_header_parts" , e_code = 9111 , http_code = 401 ) )

        token = authorization_header_parts[ 1 ]

        if len( token.strip( ) ) < 5 : return( response_error( e_msg = "token" , e_code = 9115 , http_code = 401 ) )

        if len( token.strip( ) ) == 64 :
            _g.api = _database.api_getbytoken( token )
        else :
            if not _config.DATA[ "server_security_lax" ] : return( response_error( e_msg = "token" , e_code = 9115 , http_code = 401 ) )
            _g.api = _database.api_getbytoken_lax( token )

        ####

        if _g.api == None : return( response_error( e_msg = "get_api_by_token" , e_code = 9126 , http_code = 401 ) )

        ####

        if not _g.api[ "enable" ] : return( response_error( e_msg = "api enable" , e_code = 9135 , http_code = 403 ) )

        #if int( request.headers.get( "Content-Length" ) or 0 ) > _g.api[ "io_maxsize" ] :
        #if int( request.headers.get( "Content-Length" ) or 0 ) > 16777216 :
        #    return( response_error( e_msg = "content length max size" , e_code = 9139 , http_code = 401 ) )

        ####

        #print( f"FIXME TODO {__file__} {request.remote_addr}")
        user_match_ip = _g.api[ "ip" ]

        if user_match_ip != None and user_match_ip != "" :

            remote_ip = request.headers.get( "X-Forwarded-For" )

            if not remote_ip : remote_ip = request.remote_addr

            #print(f"{remote_ip=}")

            user_match_ip_parts = user_match_ip.split( "," )

            flag_user_match_ip = False

            for user_match_ip_part in user_match_ip_parts:
                if remote_ip.startswith( user_match_ip_part ) :
                    flag_user_match_ip = True
                    break

            if not flag_user_match_ip :
                if _g.api[ "ip_update" ] == 0 : return( response_error( e_msg = f"{remote_ip} api ip" , e_code = 9154 , http_code = 401 ) )
                _database.update_fromdict( "api" , _g.api[ "id" ] , { "ip" : f"{remote_ip}" , "ip_update" : 0 } )


        return( f( *args , **kwargs ) )

    return( decorator_function )

def decorator_role_required( role_name ) :
    def decorator_function( f ) :
        @wraps( f )
        def wrapped( *args , **kwargs ) :
            if _g.api[ "role_name" ] != role_name : return( response_error( e_msg = "role" , e_code = 9229 , http_code = 403 ) )
            return( f( *args , **kwargs ) )
        return( wrapped )
    return( decorator_function )

def decorator_request_json( f ) :

    @wraps( f )
    def decorator_function( *args , **kwargs ) :

        if len( request.data ) == 0 : return( response_error( e_msg = "data empty" , e_code = 9266 , http_code = 400 ) )

        if request.content_type != "application/json" : return( response_error( e_msg = "content type" , e_code = 9271 , http_code = 400 ) )


        if not request.is_json : return( response_error( e_msg = "not is_json" , e_code = 9274 , http_code = 400 ) )

        try :
            if not isinstance( request.json , dict ) : return( response_error( e_msg = "not dict" , e_code = 9274 , http_code = 400 ) )
        except Exception as e :
            return( response_error( e_msg = f"bad json" , e_code = 9274 , http_code = 400 ) )

        return( f( *args , **kwargs ) )

    return( decorator_function )

def decorator_web_login_required( account_name = None ) :
    def decorator_function( f ) :
        @wraps( f )
        def wrapped( *args , **kwargs ) :
            #if _g.api[ "role_name" ] != role_name : return( response_error( e_msg = "role" , e_code = 9229 , http_code = 403 ) )
            session_data = { }
            session_key = request.cookies.get( "key" , "" ).strip( )
            if len( session_key ) != 64 : return( response_error( e_msg = "session empty" , e_code = 9266 , http_code = 400 ) )
            session_row = _database.db_query_select_row( "SELECT * from `session` WHERE `key`=%s LIMIT 1" , [ session_key ] )
            if session_row == None : return( response_error( e_msg = "session none" , e_code = 9267 , http_code = 400 ) )
            session_data = json.loads( session_row[ "data" ] ) 

            if account_name is not None :
                if session_data[ "account_row" ][ "name" ] != account_name : return redirect( url_for( ".page_login" ) )

            return( f( *args , **kwargs ) )
        return( wrapped )
    return( decorator_function )

####################################################################

def request_ip( ) :
    remote_ip = request.headers.get( "X-Forwarded-For" )
    if not remote_ip : remote_ip = request.remote_addr
    return( remote_ip )

def request_arg_str( a ) :
    n = request.args.get( a , default = "" ).strip( )
    return( n )

def request_arg_int( a ) :
    n_str = request_arg_str( a )
    if not n_str.isdigit( ) : raise Exception( f"{a} not isdigit" ) 

    n = int( float( n_str ) )
    #if not task_id > 0 : return( None )

    return( n )

def request_form_str( form , k , minlen = 5 ) :
    if k not in form : raise Exception( f"{k} not found" )
    if len( form[ k ] ) != 1 : raise Exception( f"len form {k} != 1" )
    v = form[ k ][ 0 ].strip( )
    if len( v ) < minlen : raise Exception( f"{k} to short" )
    return( v )

def request_form_email( form , k , minlen = 5 ) :
    if k not in form : raise Exception( f"{k} not found" )
    if len( form[ k ] ) != 1 : raise Exception( f"len form {k} != 1" )
    v = form[ k ][ 0 ].strip( )
    if len( v ) < minlen : raise Exception( f"{k} to short" )
    if not _util.email_check( v ) : raise Exception( "Invalid email address" )
    return( v )

def request_form_checkbox_single( form , k ) :
    return( k in form )

def session_get( ) :
    session_data = { }
    session_key = request.cookies.get( "key" , "" ).strip( )
    if len( session_key ) == 64 :
        session_row = _database.db_query_select_row( "SELECT * from `session` WHERE `key`=%s LIMIT 1" , [ session_key ] )
        if session_row != None :
            session_data = json.loads( session_row[ "data" ] ) 
    return( session_data )
