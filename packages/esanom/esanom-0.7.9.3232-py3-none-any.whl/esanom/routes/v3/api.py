
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

from flask import Blueprint , request , g as _g , send_file
import json
import copy
import os
import time
from datetime import datetime

from esanom import database as _database , util as _util , pipeline as _pipeline , config as _config

from . import common as _common

#####################################################################

ROUTES = Blueprint( "routes" , __name__ )

####


@ROUTES.after_request
def after_request_func( resp ) :

    #print(f"after_request_func{request.url_rule}")
    #/v3/api/model_schedule

    ####
    NoM_Client_Wait = 0
    if "/admin" not in request.url_rule.rule : NoM_Client_Wait = 0.5
    if request.remote_addr.startswith( "127." ): NoM_Client_Wait = 0.01
    resp.headers[ "NoM_Client_Wait" ] = NoM_Client_Wait
    ####

    #if 'Cache-Control' not in response.headers:
    #    response.headers['Cache-Control'] = 'no-store'

    #if "text/html" not in resp.headers[ "Content-Type" ] : return( resp )
    #cookie_key = request.cookies.get( "key" , "" )
    #if cookie_key.strip( ) != "" : return( resp )
    #resp.set_cookie( "key" , session_key , secure = True , samesite = "Strict" )

    ####

    return( resp )


@ROUTES.route( "/admin_state" , methods = [ "GET" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "admin" )
def admin_state( ) :

    messages = { }

    ####

    table = request.args.get( "table" , default = "" ) 
    if table.strip( ) != "" :

        row_id_str = request.args.get( "row_id" , default = "" )
        if row_id_str.strip( ) == "" or ( not row_id_str.lstrip( "-" ).isdigit( ) ) : 
            row_id = None
        else :
            row_id = int( float( row_id_str ) )
            if not row_id > 0 : row_id = None

        messages[ table ] = _database.admin_state( table , row_id = row_id )
        return( _common.response_default( messages ) )

    ####

    for t in _database.NOMTABLES : messages[ t ] = _database.admin_state( t )

    return( _common.response_default( messages ) )

@ROUTES.route( "/admin_create" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "admin" )
@_common.decorator_request_json
def admin_create( ) :

    if not "table" in request.args : return( _common.response_error( e_msg = "request args"  ) )

    id = _database.insert_fromdict( request.args.get( "table" ).strip( ) , request.json )

    if id == None : return( _common.response_error( e_msg = "id none"  ) )

    messages = { "id" : id }

    return( _common.response_default( messages ) )

@ROUTES.route( "/admin_create_bulk" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "admin" )
@_common.decorator_request_json
def admin_create_bulk( ) :

    if not "table" in request.args : return( _common.response_error( e_msg = "request args"  ) )

    if not "rows" in request.json : return( _common.response_error( e_msg = "request json rows"  ) )

    ids = [ ]

    table = _common.request_arg_str( "table" )

    for r in request.json[ "rows" ] :
        id = _database.insert_fromdict( table , r )
        if id == None : return( _common.response_error( e_msg = "id none"  ) )
        ids.append( id )

    messages = { "ids" : ids }

    return( _common.response_default( messages ) )

@ROUTES.route( "/admin_update" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "admin" )
@_common.decorator_request_json
def admin_update( ) :

    if not "table" in request.args : return( _common.response_error( e_msg = "request args"  ) )
    if not "id" in request.args : return( _common.response_error( e_msg = "request args"  ) )

    table = request.args.get( "table" , default = "" ) 
    if table.strip( ) == "" : return( _common.response_error( e_msg = "table blank" ) )

    id_str = request.args.get( "id" , default = "" ) 
    if not id_str.isdigit( ): return( _common.response_error( e_msg = "id not isdigit" ) )
    id = int( float( id_str ) )
    if not id > 0 : return( _common.response_error( e_msg = "not id" ) )

    res = _database.update_fromdict( table , id , request.json )

    if res == None : return( _common.response_error( e_msg = "res none" ) )

    return( _common.response_default( ) )

@ROUTES.route( "/admin_delete" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "admin" )
@_common.decorator_request_json
def admin_delete( ) :

    if not "table" in request.args : return( _common.response_error( e_msg = "request args"  ) )
    if not "id" in request.args : return( _common.response_error( e_msg = "request args"  ) )

    table = request.args.get( "table" , default = "" ) 
    if table.strip( ) == "" : return( _common.response_error( e_msg = "table blank" ) )

    id_str = request.args.get( "id" , default = "" ) 
    if not id_str.isdigit( ) : return( _common.response_error( e_msg = "id not isdigit" ) )
    id = int( float( id_str ) )
    if not id > 0 : return( _common.response_error( e_msg = "not id" ) )

    res = _database.delete_fromid( table , id )

    if res == None : return( _common.response_error( e_msg = "res none" ) )

    return( _common.response_default( ) )


@ROUTES.route( "/admin_delete_bulk" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "admin" )
@_common.decorator_request_json
def admin_delete_bulk( ) :

    table = request.args.get( "table" , default = "" ) 
    if table.strip( ) == "" : return( _common.response_error( e_msg = "table blank" ) )

    if not "rows" in request.json : return( _common.response_error( e_msg = "request json rows"  ) )

    for row_id in request.json[ "rows" ] :
        _database.delete_fromid( table , row_id )
        # == None : return( _common.response_error( e_msg = f"delete_fromid {table} {row_id}"  ) )

    return( _common.response_default( ) )

@ROUTES.route( "/admin_model_enable" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "admin" )
@_common.decorator_request_json
def admin_model_enable( ) :

    api_token = request.json.get( "api_token" , "" )
    if api_token.strip( ) == "" : return( _common.response_error( e_msg = "no api_token" ) )

    api_row = _database.db_query_select_row( "SELECT id from api WHERE token=%s LIMIT 1" , [ api_token ] )
    if api_row == None : return( _common.response_error( e_msg = "api_row" ) )

    sql = "UPDATE rolemodel SET enable = 1 , updateable = 0 WHERE api_id=%s LIMIT 1"
    params = [ api_row[ "id" ] ]

    _database.db_query_update( sql , params )

    return( _common.response_default( ) )


@ROUTES.route( "/admin_model_updateable" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "admin" )
@_common.decorator_request_json
def admin_model_updateable( ) :

    api_token = request.json.get( "api_token" , "" )
    if api_token.strip( ) == "" : return( _common.response_error( e_msg = "no api_token" ) )

    api_row = _database.db_query_select_row( "SELECT id from api WHERE token=%s LIMIT 1" , [ api_token ] )
    if api_row == None : return( _common.response_error( e_msg = "api_row" ) )

    sql = "UPDATE rolemodel SET enable=0,updateable=1 WHERE api_id=%s LIMIT 1"
    params = [ api_row[ "id" ] ]

    res = _database.db_query_update( sql , params )
    if res == None : return( _common.response_error( e_msg = "db_query_update none" ) )

    return( _common.response_default( ) )


@ROUTES.route( "/admin_group_flush" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "admin" )
@_common.decorator_request_json
def admin_group_flush( ) :

    api_id = _common.request_arg_int( "api_id" )
    if api_id == None : return( _common.response_error( e_msg = "api_id bad" ) )

    _database.db_query_delete( "DELETE FROM api_group WHERE api_id=%s" , [ api_id ] )

    return( _common.response_default( ) )

#####################################################################

@ROUTES.route( "/model_state" , methods = [ "GET" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "model" )
def model_state( ) :

    messages = { }

    messages[ "model" ] = _database.model_state_rolemodel( api_id = _g.api[ "id" ] )
    messages[ "group" ] = _database.model_state_group( api_id = _g.api[ "id" ] )

    return( _common.response_default( messages ) )

@ROUTES.route( "/model_specs" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "model" )
@_common.decorator_request_json
def model_specs( ) :

    if not "name" in request.json : return( _common.response_error( e_msg = "not name"  ) )

    ####

    rolemodel_enable = 0
    if _config.DATA[ "server_security_lax" ] : rolemodel_enable = 1

    ####

    rolemodel_row = _database.db_query_select_row( "SELECT * from rolemodel WHERE api_id=%s LIMIT 1" , [ _g.api[ "id" ] ] )

    if rolemodel_row == None :
        rolemodel_data = {
            "api_id" : _g.api[ "id" ] ,
            "name" : request.json[ "name" ] ,
            "specs" : json.dumps( request.json ) ,
            "category" : request.json.get( "category" ) ,
            "description" : request.json.get( "desc" ) ,
            "type" : request.json.get( "type" ) ,
            "user_api_ip_prefix" : request.json.get( "user_api_ip_prefix" , "127.,192.168.,172.,10." ) ,
            "user_api_email_postfix" : request.json.get( "user_api_email_postfix" , "sparc.gr,esa.int,aeronomie.be" ) ,
            "input_size_max" : request.json.get( "input_size_max" , 10485760 ) ,
            "ignore_pred_fail" : request.json.get( "ignore_pred_fail" ) ,
            "enable" : rolemodel_enable
        }
        rolemodel_id = _database.insert_fromdict( "rolemodel" , rolemodel_data )
    else :
        if rolemodel_row[ "updateable" ] == 0 :
            if not _config.DATA[ "server_security_lax" ]  :
                return( _common.response_error( e_msg = "not updateable"  ) )
        if json.loads( rolemodel_row[ "specs" ] ) == request.json : return( _common.response_default( ) )
        rolemodel_id = rolemodel_row[ "id" ]
        rolemodel_data = {
            "name" : request.json[ "name" ] ,
            "specs" : json.dumps( request.json ) ,
            "category" : request.json.get( "category" ) ,
            "description" : request.json.get( "desc" ) ,
            "type" : request.json.get( "type" ) ,
            "user_api_ip_prefix" : request.json.get( "user_api_ip_prefix" , "127.,192.168.,172.,10." ) ,
            "user_api_email_postfix" : request.json.get( "user_api_email_postfix" , "sparc.gr,esa.int,aeronomie.be" ) ,
            "input_size_max" : request.json.get( "input_size_max" , 10485760 ) ,
            "ignore_pred_fail" : request.json.get( "ignore_pred_fail" ) ,
            "enable" : rolemodel_enable
        }
        _database.update_fromdict( "rolemodel" , rolemodel_id , rolemodel_data )

    ####

    _database.model_flush_ports( rolemodel_id ) 
    # FIXME TODO is this required?
    _database.db_query_delete( f"DELETE from `mport` WHERE rolemodel_id=%s" , [ rolemodel_id ] )    


    interfaces_global = request.json.get( "interfaces_global" , 0 ) == 1

    if "ports" in request.json : _database.model_load_ports( rolemodel_id , request.json[ "ports" ] , interfaces_global = interfaces_global )

    ####

    if "inputs" in request.json :
        for specs_io in request.json[ "inputs" ] :
            if not "name" in specs_io : return( _common.response_error( e_msg = "not name in specs_input"  ) )
            if _database.verify_portpinunit( specs_io ) == None :
                return( _common.response_error( e_msg = f"verify {specs_io['name']}"  ) )

    if "outputs" in request.json :
        for specs_io in request.json[ "outputs" ] :
            if not "name" in specs_io : return( _common.response_error( e_msg = "not name in specs_output"  ) )
            if _database.verify_portpinunit( specs_io ) == None :
                return( _common.response_error( e_msg = f"verify {specs_io['name']}"  ) )

    ####

    if "inputs" in request.json :
        for specs_io in request.json[ "inputs" ] :
            if _database.process_specs_io( specs_io , rolemodel_id , "inputs" ) == None :
                return( _common.response_error( e_msg = f"process_specs_io inputs" ) )

    if "outputs" in request.json :
        for specs_io in request.json[ "outputs" ] :
            if _database.process_specs_io( specs_io , rolemodel_id , "outputs" ) == None :
                return( _common.response_error( e_msg = f"process_specs_io outputs" ) )

    ####

    return( _common.response_default( ) )





@ROUTES.route( "/model_pipeline_failed" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "model" )
@_common.decorator_request_json
def model_pipeline_failed( ) :


    task_uid = _common.request_arg_str( "task_uid" )
    exit_code = _common.request_arg_int( "exit_code" )

    task_row = _database.db_query_select_row( "SELECT * from task WHERE uid=%s LIMIT 1" , [ task_uid ] )

    if task_row[ "status" ] == "RUNNING" :
        _database.update_fromdict( "task" , task_row[ "id" ] , { "status" : "FAILED" , "exit_code" : exit_code } )


    return( _common.response_default( ) )

@ROUTES.route( "/model_schedule" , methods = [ "GET" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "model" )
def model_schedule( ) :

    rolemodel_row = _database.db_query_select_row( "SELECT * from rolemodel WHERE api_id=%s LIMIT 1" , [ _g.api[ "id" ] ] )
    if rolemodel_row == None : return( _common.response_error( e_msg = "rolemodel_row None" ) )

    rolemodel_id = rolemodel_row[ "id" ]

    _database.update_fromdict( "rolemodel" , rolemodel_id , { "heartbeat_at" : datetime.now( ) } )

    schedule_row = _database.db_query_select_row( "SELECT * from schedule WHERE rolemodel_id=%s LIMIT 1" , [ rolemodel_id ] )

    messages = { }

    if schedule_row != None : messages[ "schedule_data_json" ] = schedule_row[ "data" ] 

    return( _common.response_default( messages ) )


@ROUTES.route( "/model_claim_set" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "model" )
@_common.decorator_request_json
def model_claim_set( ) :

    task_uid = _common.request_arg_str( "task_uid" )

    ####

    messages = {
        "claim_uid" : "" ,
        "claim_status" : "NO"
    }

    ####

    # Another claim with status YES?
    claim_row = _database.db_query_select_row( "SELECT * from claim WHERE task_uid=%s AND status=%s LIMIT 1" , [ task_uid , "YES" ] )
    if claim_row != None : return( _common.response_default( messages ) )

    ####

    row_data = { "task_uid" : task_uid }
    claim_id = _database.insert_fromdict( "claim" , row_data )
    if claim_id == None : return( _common.response_error( e_msg = "claim_id none"  ) )

    ####

    claim_row = _database.db_query_select_row( "SELECT * from claim WHERE id=%s LIMIT 1" , [ claim_id ] )

    messages[ "claim_uid" ] = claim_row[ "uid" ]
    messages[ "claim_status" ] = claim_row[ "status" ]

    ####

    return( _common.response_default( messages ) )


@ROUTES.route( "/model_claim_release" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "model" )
@_common.decorator_request_json
def model_claim_release( ) :

    claim_uid = _common.request_arg_str( "claim_uid" )
    _database.db_query_delete( "DELETE from claim WHERE uid=%s LIMIT 1;" , [ claim_uid ] )

    return( _common.response_default( ) )

    ####


@ROUTES.route( "/model_claim_get" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "model" )
@_common.decorator_request_json
def model_claim_get( ) :

    claim_uid = _common.request_arg_str( "claim_uid" )

    ####

    messages = {
        "claim_status" : "NO" ,
        "pipeline" : False
    }

    ####

    claim_row = _database.db_query_select_row( "SELECT * from claim WHERE uid=%s LIMIT 1" , [ claim_uid ] )
    if claim_row == None : return( _common.response_default( messages ) )

    ####

    task_uid = claim_row[ "task_uid" ]

    ####

    check_yes_claim_row = _database.db_query_select_row( "SELECT * from claim WHERE task_uid=%s AND status=%s LIMIT 1" , [ task_uid , "YES" ] )
    # Make sure to check if the claim uid is not the input
    another_yesclaim_exists = ( check_yes_claim_row != None ) and ( check_yes_claim_row[ "uid" ] != claim_uid )
    if another_yesclaim_exists :
        _database.db_query_delete( "DELETE from claim WHERE uid=%s LIMIT 1;" , [ claim_uid ] )
        return( _common.response_default( messages ) )

    ####

    if claim_row[ "status" ] == "WAIT" :
        messages[ "claim_status" ] = claim_row[ "status" ]
        return( _common.response_default( messages ) )

    ####

    task_row = _database.db_query_select_row( "SELECT * from task WHERE uid=%s LIMIT 1" , [ task_uid ] )

    # Check if task is scheduled
    if task_row[ "status" ] != "SCHEDULED" :
        _database.db_query_delete( "DELETE from claim WHERE uid=%s LIMIT 1;" , [ claim_uid ] )
        return( _common.response_default( messages ) )

    ####

    rolemodel_row = _database.db_query_select_row( "SELECT * from rolemodel WHERE api_id=%s LIMIT 1" , [ _g.api[ "id" ] ] )
    if rolemodel_row == None : return( _common.response_error( e_msg = "rolemodel_row None" ) )

    ####

    pipeline = _pipeline.Pipeline( )

    pipeline.task_uid = claim_row[ "task_uid" ]

    pipeline.status = "RUNNING"

    pipeline.current_role_name = _g.api[ "role_name" ]

    pipeline.io_info[ "_" ] = _database.io_info( rolemodel_row[ "name" ] )
    
    pipeline.io_data = _database.io_data( task_row[ "id" ] )

    pipeline.nodes = {
        "_": {
            "name" : "_" ,
            "task_uid" : task_uid
        }
    }

    #####

    _database.update_fromdict( "task" , task_row[ "id" ] , { "status" : "RUNNING" } )

    pipeline_task_row = _database.db_query_select_row( "SELECT * from pipeline_task WHERE task_id=%s OR next_task_id=%s LIMIT 1" , [ task_row[ "id" ] , task_row[ "id" ] ] )
    if pipeline_task_row == None : return( _common.response_error( e_msg = "pipeline_task_row None" ) )

    pipeline_row = _database.db_query_select_row( "SELECT * from pipeline WHERE id=%s LIMIT 1" , [ pipeline_task_row["pipeline_id"] ] )
    if pipeline_row == None : return( _common.response_error( e_msg = "pipeline_row None" ) )

    # Is pipeline scheduled (first task to be running) or not running?
    if pipeline_row[ "status" ] == "SCHEDULED" :
        _database.update_fromdict( "pipeline" , pipeline_row[ "id" ] , { "status" : "RUNNING" } )
    elif pipeline_row[ "status" ] != "RUNNING" :
        _database.db_query_delete( "DELETE from claim WHERE uid=%s LIMIT 1;" , [ claim_uid ] )
        return( _common.response_default( messages ) )

    ####

    messages[ "pipeline" ] = _util.object_encode( pipeline )
    messages[ "claim_status" ] = claim_row[ "status" ]

    ####

    return( _common.response_default( messages ) )



@ROUTES.route( "/model_task_heartbeat" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "model" )
@_common.decorator_request_json
def model_task_heartbeat( ) :

    task_uid = _common.request_arg_str( "task_uid" )

    task_row = _database.db_query_select_row( "SELECT * from task WHERE uid=%s LIMIT 1" , [ task_uid ] )

    if task_row[ "status" ] == "RUNNING" :
        _database.update_fromdict( "task" , task_row[ "id" ] , { "heartbeat_at" : datetime.now( ) } )

    pipeline_task_row = _database.db_query_select_row( "SELECT * from pipeline_task WHERE task_id=%s OR next_task_id=%s LIMIT 1" , [ task_row[ "id" ] , task_row[ "id" ] ] )

    pipeline_row = _database.db_query_select_row( "SELECT * from pipeline WHERE id=%s LIMIT 1" , [ pipeline_task_row[ "pipeline_id" ] ] )


    messages = {
        "pipeline_status" : pipeline_row["status"]
    }

    return( _common.response_default( messages ) )


@ROUTES.route( "/model_ioblock" , methods = [ "GET" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "model" )
def model_ioblock( ) :  

    io_uid = _common.request_arg_str( "io_uid" ) 
    if io_uid == "" : return( _common.response_error( e_msg = "io_uid blank" ) )

    ioblock_block = _common.request_arg_int( "ioblock_block" )
    if ioblock_block == None : return( _common.response_error( e_msg = "ioblock_block bad" ) )

    ####

    io_row = _database.db_query_select_row( "SELECT * from io WHERE uid=%s LIMIT 1" , [ io_uid ] )
    if io_row == None : _common.response_error( e_msg = f"io_row not found" )
    io_id = io_row[ "id" ]

    ioblock_row = _database.db_query_select_row( "SELECT * from ioblock WHERE io_id=%s AND block=%s LIMIT 1" , [ io_id , ioblock_block ] )
    if ioblock_row == None : _common.response_error( e_msg = f"ioblock_row not found" )

    #print(ioblock_row)

    io_hash_filepath = _util.get_io_hash_filepath( ioblock_row[ "hash" ] )
 
    #print( io_hash_filepath )

    return( send_file( io_hash_filepath ) )


@ROUTES.route( "/model_ioblock_status" , methods = [ "GET" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "model" )
def model_ioblock_status( ) :

    io_uid = _common.request_arg_str( "io_uid" )
    if io_uid == "" : return( _common.response_error( e_msg = "io_uid blank" ) )

    io_row = _database.db_query_select_row( "SELECT * from io WHERE uid=%s LIMIT 1" , [ io_uid ] )
    if io_row == None : return( _common.response_error( e_msg = "io_row none" ) )
    io_id = io_row["id"]

    ioblock_row = _database.db_query_select_row( "SELECT * from ioblock WHERE io_id=%s order by block DESC LIMIT 1" , [io_id ] )
    if ioblock_row == None :
        block_current = 0
    else :
        block_current = ioblock_row[ "block" ] + 1

    messages = {
        "blocks_total" : io_row[ "blocks" ] ,
        "blocks_current" : block_current
    }

    return( _common.response_default( messages ) )



@ROUTES.route( "/model_ioblock_upload_block" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "model" )
#@_common.decorator_request_json
def model_ioblock_upload_block( ) :

    io_uid = _common.request_arg_str( "io_uid" )
    if io_uid == "" : return( _common.response_error( e_msg = "io_uid blank" ) )

    # FIXME TODO check all incoming parameters before doing db queries?
    io_row = _database.db_query_select_row( "SELECT * from io WHERE uid=%s LIMIT 1" , [ io_uid ] )
    if io_row == None : return( _common.response_error( e_msg = "io_row none" ) )
    io_id = io_row[ "id" ]

    block_str = request.args.get( "block" , default = "" ) 
    if not block_str.isdigit( ): return( _common.response_error( e_msg = "block_str not isdigit" ) )
    block = int( float( block_str ) )

    file_hash = _common.request_arg_str( "hash" )
    if file_hash == "" : return( _common.response_error( e_msg = "file_hash blank" ) )

    file_compressor = _common.request_arg_str( "compressor" )
    if file_compressor == "" : return( _common.response_error( e_msg = "file_compressor blank" ) )

    #print(request.data)

    request_data_hash = _util.filedata_hash( request.data )
    if request_data_hash != file_hash: return( _common.response_error( e_msg = "hash mismatch" ) )

    file_path = _util.get_io_hash_filepath( file_hash )

    # FIXME TODO what if another process is doing the same file write? Do write then move?
    if not os.path.isfile( file_path ) : 
        with open( file_path , "wb" ) as f : f.write( request.data )

    ioblock_row = {
        "io_id" : io_id ,
        "block" : block ,
        "size" : len(request.data),
        "hash" : file_hash ,
        "compressor" : file_compressor
    }

    _database.insert_fromdict( "ioblock" , ioblock_row )
    if id == None : return( _common.response_error( e_msg = "id none"  ) )

    return( _common.response_default( ) )



@ROUTES.route( "/model_pipeline_submit_io" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "model" )
@_common.decorator_request_json
def model_pipeline_submit_io( ) :    

    task_uid = _common.request_arg_str( "task_uid" )
    if task_uid == "" : return( _common.response_error( e_msg = "task_uid blank" ) )

    #print(request.json)

    messages = {
        "io_uid" : _database.io_insert( task_uid , request.json )
    }

    return( _common.response_default( messages ) )


@ROUTES.route( "/model_pipeline_submit" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "model" )
@_common.decorator_request_json
def model_pipeline_submit( ) :    

    task_uid = _common.request_arg_str( "task_uid" )
    if task_uid == "" : return( _common.response_error( e_msg = "task_uid blank" ) )

    task_row = _database.db_query_select_row( "SELECT * from task WHERE uid=%s AND status=%s LIMIT 1" , [ task_uid , "RUNNING" ] )
    if task_row == None : _common.response_error( e_msg = f"task_row not found" )

    _database.update_fromdict( "task" , task_row[ "id" ] , { "status" : "COMPLETED" , "status_code" : 0 } )

    return( _common.response_default( ) )

#####################################################################

@ROUTES.route( "/user_state" , methods = [ "GET" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "user" )
def user_state( ) :

    messages = { }

    messages[ "model" ] = _database.user_state_model( api_id = _g.api[ "id" ] )
    messages[ "group" ] = _database.user_state_group( api_id = _g.api[ "id" ] )
    messages[ "pipeline" ] = _database.user_state_pipeline( api_id = _g.api[ "id" ] )

    return( _common.response_default( messages ) )


@ROUTES.route( "/user_pipeline" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "user" )
@_common.decorator_request_json
def user_pipeline( ) :

    name = _common.request_arg_str( "name" )
    if name == "" : return( _common.response_error( e_msg = "name blank" ) )

    ####

    pipeline_row = _database.user_pipeline( _g.api[ "id" ] , name )

    ####

    pipeline = _pipeline.Pipeline( name )
    pipeline.current_role_name = _g.api[ "role_name" ]
    pipeline.status = pipeline_row[ "status" ]
    pipeline.done = pipeline_row[ "done" ]
    
    ####

    for model_name in _database.user_state_model( api_id = _g.api[ "id" ] ) :
        pipeline.io_info[ model_name ] = _database.io_info( model_name )

    ####

    if( pipeline_row[ "status" ] != "RESERVED" ) :

        pipeline.nodes = _database.pipeline_nodes( pipeline_row[ "id" ] )

        for i , ( k , v ) in enumerate( pipeline.nodes.items( ) ) :
            pipeline.io_data.update( _database.io_data_from_taskuid( v[ "task_uid" ] ) )

    ####

    messages = { }

    messages[ "pipeline" ] = _util.object_encode( pipeline )

    return( _common.response_default( messages ) )


@ROUTES.route( "/user_pipeline_submit_reserve" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "user" )
@_common.decorator_request_json
def user_pipeline_submit_reserve( ) :


    name = _common.request_arg_str( "name" ).strip( )
    if name == "" : return( _common.response_error( e_msg = "name blank" ) )

    ####

    roleuser = _database.db_query_select_row( "SELECT id from roleuser WHERE api_id=%s LIMIT 1" , [ _g.api[ "id" ] ] )
    if roleuser == None : return( _common.response_error( e_msg = "roleuser" ) )

    pipeline_row = _database.db_query_select_row( "SELECT * from pipeline WHERE roleuser_id=%s AND name=%s AND status=%s AND archived=0 LIMIT 1" , [ roleuser[ "id" ] , name , "RESERVED" ] )
    if pipeline_row == None : return( _common.response_error( e_msg = f"Pipeline [{name}] RESERVED not found. Already submitted?" ) )

    ####

    nodes = request.json.get( "nodes" , None )
    if nodes == None : return( _common.response_error( e_msg = f"No nodes" ) )
    if not isinstance( nodes , dict ) : return( _common.response_error( e_msg = f"nodes not dict" ) )
    nodes_keys = list( nodes.keys( ) )
    if len( nodes_keys ) == 0 :
        messages = {
            "pipeline_uid" : pipeline_row[ "uid" ] ,
            "task_uids" : [ ]
        }
        return( _common.response_default( messages ) )

    ####

    # FIXME TODO creating pipeline and tasks should be in a transaction!

    task_ids = { }

    for i , ( k , v ) in enumerate( nodes.items( ) ) :
        model_name = v[ "name" ]
        rolemodel_row = _database.db_query_select_row( "SELECT * from rolemodel WHERE name=%s LIMIT 1" , [ model_name ] )
        if rolemodel_row == None : _common.response_error( e_msg = f"[{model_name}] not found" )
        task_row = { "rolemodel_id" : rolemodel_row[ "id" ] , "rolemodel_name_alt" : k }
        task_id = _database.insert_fromdict( "task" , task_row )
        if task_id == None : return( _common.response_error( e_msg = "task insert" ) )
        task_ids[ k ] = task_id 

    #_util.debug_json_print( task_ids , "task_ids" )
    
    ###

    edges = request.json.get( "edges" , None )

    pipeline_obj = _pipeline.Pipeline( edges_in = request.json[ "edges" ] )

    if not pipeline_obj.is_valid( ) : return( _common.response_error( e_msg = "bad dag" ) )

    edge_order = copy.deepcopy( pipeline_obj.topological_sort_edges( ) )

    graph_nodes = pipeline_obj.get_node_graph_names( )
    #print(graph_nodes)
    for node in nodes_keys :
        if not node in graph_nodes :
            edge_order.append( [ node , None ] )

    #_util.debug_json_print( edge_order , "edge_order" )

    ###

    for edges in edge_order :
        pipeline_task_row = {
            "pipeline_id" : pipeline_row[ "id" ] ,
            "task_id" : task_ids.get( edges[ 0 ] , None ) ,
            "next_task_id" : task_ids.get( edges[ 1 ] , None )
        }
        pipeline_task_id = _database.insert_fromdict( "pipeline_task" , pipeline_task_row )
        if pipeline_task_id == None : return( _common.response_error( e_msg = "pipeline_task insert" ) )

    ####

    task_uids = { }

    for i , ( k , v ) in enumerate( task_ids.items( ) ) :
        task_row = _database.db_query_select_row( "SELECT * from task WHERE id=%s LIMIT 1" , [ v ] )
        if task_row == None : _common.response_error( e_msg = f"task_row [{v}] not found" )
        task_uids[ k ] = task_row[ "uid" ]

    ####

    messages = {
        "pipeline_uid" : pipeline_row[ "uid" ] ,
        "task_uids" : task_uids
    }

    return( _common.response_default( messages ) )

@ROUTES.route( "/user_pipeline_submit_io" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "user" )
@_common.decorator_request_json
def user_pipeline_submit_io( ) :

    task_uid = _common.request_arg_str( "task_uid" )
    if task_uid == "" : return( _common.response_error( e_msg = "task_uid blank" ) )


    is_local = request.remote_addr == "127.0.0.1"

    messages = {
        "io_uid" : _database.io_insert( task_uid , request.json , is_local = is_local )
    }

    return( _common.response_default( messages ) )


@ROUTES.route( "/user_ioblock_status" , methods = [ "GET" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "user" )
def user_ioblock_status( ) :

    io_uid = _common.request_arg_str( "io_uid" )
    if io_uid == "" : return( _common.response_error( e_msg = "io_uid blank" ) )

    messages = _database.io_block_status( io_uid )

    return( _common.response_default( messages ) )


@ROUTES.route( "/user_ioblock_upload_block" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "user" )
def user_ioblock_upload_block( ) :

    io_uid = _common.request_arg_str( "io_uid" )
    if io_uid == "" : return( _common.response_error( e_msg = "io_uid blank" ) )

    io_row = _database.db_query_select_row( "SELECT * from io WHERE uid=%s LIMIT 1" , [ io_uid ] )
    if io_row == None : return( _common.response_error( e_msg = "io_row none" ) )

    block = _common.request_arg_int( "block" )

    if block >= io_row[ "blocks" ] : return( _common.response_error( e_msg = "block out of range" ) )

    file_hash = _common.request_arg_str( "hash" )
    if file_hash == "" : return( _common.response_error( e_msg = "file_hash blank" ) )

    file_compressor = _common.request_arg_str( "compressor" )
    if file_compressor == "" : return( _common.response_error( e_msg = "file_compressor blank" ) )

    request_data_hash = _util.filedata_hash( request.data )
    if request_data_hash != file_hash: return( _common.response_error( e_msg = "hash mismatch" ) )

    ####

    file_path = _util.get_io_hash_filepath( file_hash )

    file_path_tmp = file_path + ".tmp"

    print(f"{file_path=}")

    # FIXME TODO the tmp file should not exist...?
    if not os.path.isfile( file_path_tmp ) : 
        print(f"{file_path_tmp=}")
        with open( file_path_tmp , "wb" ) as f : f.write( request.data )
        os.rename( file_path_tmp , file_path )

    ####

    ioblock_row = {
        "io_id" : io_row[ "id" ] ,
        "block" : block ,
        "size" : len( request.data ) ,
        "hash" : file_hash ,
        "compressor" : file_compressor
    }

    _database.insert_fromdict( "ioblock" , ioblock_row )
    if id == None : return( _common.response_error( e_msg = "id none"  ) )

    return( _common.response_default( ) )

@ROUTES.route( "/user_pipeline_submit" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "user" )
@_common.decorator_request_json
def user_pipeline_submit( ) :

    name = _common.request_arg_str( "name" ).strip( )
    if name == "" : return( _common.response_error( e_msg = "name blank" ) )

    roleuser_row = _database.db_query_select_row( "SELECT id from roleuser WHERE api_id=%s LIMIT 1" , [ _g.api[ "id" ] ] )
    if roleuser_row == None : return( _common.response_error( e_msg = "roleuser_row" ) )

    pipeline_row = _database.db_query_select_row( "SELECT * from pipeline WHERE roleuser_id=%s AND name=%s AND status=%s AND archived=0 LIMIT 1" , [ roleuser_row[ "id" ] , name , "RESERVED" ] )
    if pipeline_row == None : return( _common.response_error( e_msg = f"Pipeline [{name}] not found" ) )


    pipeline_task_rows = _database.db_query_select_rows( "SELECT * from pipeline_task WHERE pipeline_id=%s" , [ pipeline_row[ "id" ] ] )
    if pipeline_task_rows == None : return( _common.response_error( e_msg = "pipeline_task_rows" ) )


    task_ids = set( )
    for pipeline_task_row in pipeline_task_rows :
        task_ids.update( [ pipeline_task_row[ "task_id" ] ] )
        if pipeline_task_row[ "next_task_id" ] != None :
            task_ids.update( [ pipeline_task_row[ "next_task_id" ] ] )

    ####

    if len( task_ids ) == 0 :
        _database.update_fromdict( "pipeline" , pipeline_row[ "id" ] , { "status" : "COMPLETED" } )
        return( _common.response_default( ) )

    ####

    for task_id in task_ids :

        task_row = _database.db_query_select_row( "SELECT * from task WHERE id=%s AND status=%s LIMIT 1" , [ task_id , "RESERVED" ] )
        if task_row == None : return( _common.response_error( e_msg = f"task_row not found" ) )
        #print(task_row)

        _database.update_fromdict( "task" , task_row[ "id" ] , { "status" : "SUBMITTED" } )

    ####

    _database.update_fromdict( "pipeline" , pipeline_row[ "id" ] , { "status" : "SUBMITTED" } )

    return( _common.response_default( ) )

@ROUTES.route( "/user_pipeline_archive" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "user" )
@_common.decorator_request_json
def user_pipeline_archive( ) :

    name = _common.request_arg_str( "name" )
    if name == "" : return( _common.response_error( e_msg = "name blank" ) )

    roleuser_row = _database.db_query_select_row( "SELECT id from roleuser WHERE api_id=%s LIMIT 1" , [ _g.api[ "id" ] ] )
    if roleuser_row == None : return( _common.response_error( e_msg = "roleuser_row" ) )

    pipeline_row = _database.db_query_select_row( "SELECT * from pipeline WHERE roleuser_id=%s AND name=%s AND archived=0 LIMIT 1" , [ roleuser_row[ "id" ] , name ] )
    if pipeline_row == None : return( _common.response_error( e_msg = "pipeline_row" ) )

    if pipeline_row[ "done" ] == 0 : return( _common.response_error( e_msg = "pipeline_row not done" ) )
    if pipeline_row[ "archived" ] != 0 : return( _common.response_error( e_msg = "pipeline_row already archived" ) )

    #print( pipeline_row )

    _database.update_fromdict( "pipeline" , pipeline_row[ "id" ] , { "archived" : 1 } )

    return( _common.response_default( ) )


@ROUTES.route( "/user_pipeline_cancel" , methods = [ "POST" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "user" )
@_common.decorator_request_json
def user_pipeline_cancel( ) :

    name = _common.request_arg_str( "name" )
    if name == "" : return( _common.response_error( e_msg = "name blank" ) )

    roleuser_row = _database.db_query_select_row( "SELECT id from roleuser WHERE api_id=%s LIMIT 1" , [ _g.api[ "id" ] ] )
    if roleuser_row == None : return( _common.response_error( e_msg = "roleuser_row" ) )

    pipeline_row = _database.db_query_select_row( "SELECT * from pipeline WHERE roleuser_id=%s AND name=%s AND archived=0 LIMIT 1" , [ roleuser_row[ "id" ] , name ] )
    if pipeline_row == None : return( _common.response_error( e_msg = "pipeline_row" ) )

    if pipeline_row[ "archived" ] != 0 : return( _common.response_error( e_msg = "pipeline_row already archived" ) )

    #print( pipeline_row )

    _database.update_fromdict( "pipeline" , pipeline_row[ "id" ] , { "status" : "CANCELLED" } )

    ####
    pipeline_task_rows = _database.db_query_select_rows( "SELECT * from pipeline_task WHERE pipeline_id=%s" , [ pipeline_row[ "id" ] ] )

    task_ids = set( )
    for pipeline_task_row in pipeline_task_rows :
        task_ids.update( [ pipeline_task_row[ "task_id" ] ] )
        if pipeline_task_row[ "next_task_id" ] != None :
            task_ids.update( [ pipeline_task_row[ "next_task_id" ] ] )
    for task_id in task_ids :
        _database.update_fromdict( "task" , task_id , { "status" : "CANCELLED" } )

    ####


    return( _common.response_default( ) )


@ROUTES.route( "/user_ioblock" , methods = [ "GET" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "user" )
def user_ioblock( ) :  

    io_uid = _common.request_arg_str( "io_uid" ) 
    if io_uid == "" : return( _common.response_error( e_msg = "io_uid blank" ) )

    ioblock_block = _common.request_arg_int( "ioblock_block" )
    if ioblock_block == None : return( _common.response_error( e_msg = "ioblock_block bad" ) )

    ####

    io_row = _database.db_query_select_row( "SELECT * from io WHERE uid=%s LIMIT 1" , [ io_uid ] )
    if io_row == None : _common.response_error( e_msg = f"io_row not found" )
    io_id = io_row[ "id" ]

    ioblock_row = _database.db_query_select_row( "SELECT * from ioblock WHERE io_id=%s AND block=%s LIMIT 1" , [ io_id , ioblock_block ] )
    if ioblock_row == None : _common.response_error( e_msg = f"ioblock_row not found" )

    io_hash_filepath = _util.get_io_hash_filepath( ioblock_row[ "hash" ] )
 
    #print( io_hash_filepath )

    return( send_file( io_hash_filepath ) )

#####################################################################

@ROUTES.route( "/dashboard_state" , methods = [ "GET" ] )
@_common.decorator_token_required
@_common.decorator_role_required( "dashboard" )
def dashboard_state( ) :

    messages = { }

    messages[ "psutils" ] = _util.psutil_status( )

    return( _common.response_default( messages ) )

