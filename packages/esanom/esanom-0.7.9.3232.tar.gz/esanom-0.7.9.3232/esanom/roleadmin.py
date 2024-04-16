
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

from esanom import util as _util  


def state( ) :

    return( _util.request_get( "/admin_state" ) )

def state_table( table = None ) :

    if table == None or table.strip( ) == "" : raise Exception( "table none" )

    messages = _util.request_get( "/admin_state" , params = { "table" : table } )

    if not table in messages : raise Exception( "no table in messages" )

    return( messages[ table ] )

def state_table_row( table = None , row_id = None ) :

    if table == None or table.strip( ) == "" : raise Exception( "table none" )
    if row_id == None : return( None )

    messages = _util.request_get( "/admin_state" , params = { "table" : table , "row_id" : row_id } )

    if not table in messages : return( None )

    if len( messages[ table ] ) != 1 : return( None )

    return( messages[ table ][ 0 ] )

def create( table , data ) :

    messages = _util.request_post( "/admin_create" , params = { "table" : table } , data = data )

    if not "id" in messages  : raise Exception( f"id not found" )

    return( messages[ "id" ] ) 

def create_bulk( table , data_rows ) :

    data = {
        "rows" : data_rows
    }



    messages = _util.request_post( "/admin_create_bulk" , params = { "table" : table } , data = data )

    if not "ids" in messages  : raise Exception( f"ids not found" )
    if len( messages[ "ids" ] ) != len( data_rows )  : raise Exception( f"len ids != len data" )

    return( messages[ "ids" ] ) 

def delete_bulk( table , data_rows ) :

    data = {
        "rows" : data_rows
    }

    _util.request_post( "/admin_delete_bulk" , params = { "table" : table } , data = data )

    return( True ) 

def update( table , data , row_id ) :

    _util.request_post( "/admin_update" , params = { "table" : table , "id" : row_id } , data = data )

    return( True ) 

def delete( table , row_id ) :

    _util.request_post( "/admin_delete" , params = { "table" : table , "id" : row_id } )

    return( True ) 


def create_user( options ) :

    if not "api" in options : return( None )
    if not "name" in options[ "api" ] : return( None )

    ####

    role_id = _util.rows_scan_pluck( state_table( "role" ) , "name" , "user" , "id" )
    if role_id == None : return( None )

    ####

    group_ids = [ ]
    if "group" in options :
        groups = state_table( "group" )
        for group in options[ "group" ] :
            group_id = _util.rows_scan_pluck( groups , "name" , group , "id" )
            if group_id == None : return( None )
            group_ids.append( group_id )

    ####

    api_id = create( "api" , options[ "api" ] )
    if api_id == None : return( None )

    ####

    api_role_id = create( "api_role" , { "api_id" : api_id , "role_id" : role_id } )
    if api_role_id == None : return( None )

    ####

    for group_id in group_ids :
        api_group_id = create( "api_group" , { "api_id" : api_id , "group_id" : group_id } )
        if api_group_id == None : return( None )

    ####

    options_roleuser = { }
    if "roleuser" in options : options_roleuser = options[ "roleuser" ]

    roleuser_id = create( "roleuser" , { "api_id" : api_id , **options_roleuser } )
    if roleuser_id == None : return( None )

    ####

    user_api_row = state_table_row( "api" , row_id = api_id ) 
    if user_api_row == None : return( None )

    return( user_api_row[ "token" ] )

def create_api_with_rolegroup( options ) :

    if not "api" in options : raise Exception( f"No api given" )
    if not "name" in options[ "api" ] : raise Exception( f"No api name given" )

    ####

    if not "role" in options : raise Exception( f"No role given" )

    role_id = _util.rows_scan_pluck( state_table( "role" ) , "name" , options.get( "role" ) , "id" )
    if role_id == None : raise Exception( f"role not found" )

    ####

    group_ids = [ ]
    if "group" in options :
        groups = state_table( "group" )
        for group in options[ "group" ] :
            group_id = _util.rows_scan_pluck( groups , "name" , group , "id" )
            if group_id == None : raise Exception( f"group not found {group}" )
            group_ids.append( group_id )

    ####

    api_id = create( "api" , options[ "api" ] )

    ####

    create( "api_role" , { "api_id" : api_id , "role_id" : role_id } )

    ####

    for group_id in group_ids :
        create( "api_group" , { "api_id" : api_id , "group_id" : group_id } )

    ####

    if options.get( "role" ) == "user" :
        options_roleuser = { }
        if "roleuser" in options : options_roleuser = options[ "roleuser" ]

        create( "roleuser" , { "api_id" : api_id , **options_roleuser } )

    ####

    user_api_row = state_table_row( "api" , row_id = api_id ) 
    if user_api_row == None : return( None )

    return( user_api_row[ "token" ] )





def create_model( options ) :

    if not "api" in options : return( None )
    if not "name" in options[ "api" ] : return( None )

    ####

    role_id = _util.rows_scan_pluck( state_table( "role" ) , "name" , "model" , "id" )
    if role_id == None : return( None )

    ####

    group_ids = [ ]
    if "group" in options :
        groups = state_table( "group" )
        for group in options[ "group" ] :
            group_id = _util.rows_scan_pluck( groups , "name" , group , "id" )
            if group_id == None : return( None )
            group_ids.append( group_id )

    ####

    api_id = create( "api" , options[ "api" ] )
    if api_id == None : return( None )

    ####

    api_role_id = create( "api_role" , { "api_id" : api_id , "role_id" : role_id } )
    if api_role_id == None : return( None )

    ####

    for group_id in group_ids :
        api_group_id = create( "api_group" , { "api_id" : api_id , "group_id" : group_id } )
        if api_group_id == None : return( None )

    ####

    #options_rolemodel = { }
    #if "rolemodel" in options : options_rolemodel = options[ "rolemodel" ]

    #roleuser_id = create( "rolemodel" , { "api_id" : api_id , **options_rolemodel } )
    #if roleuser_id == None : return( None )

    ####
    
    api_row = state_table_row( "api" , row_id = api_id ) 
    if api_row == None : return( None )

    return( api_row[ "token" ] )


def model_enable( api_token ) :

    data = {
        "api_token" : api_token
    }

    _util.request_post( "/admin_model_enable" , data = data )

    return( True ) 

def model_updateable( api_token ) :

    data = {
        "api_token" : api_token
    }

    _util.request_post( "/admin_model_updateable" , data = data )

    return( True ) 

def group_flush( api_id ) :
    return( _util.request_post( "/admin_group_flush" , params = { "api_id" : api_id } ) )


def delete_testdata( table , k = "name" , v = "test_" ) :

    if len( v.strip( ) ) < 2 : return

    bulk_rows = [ ]

    rows = state_table( table )

    for row in rows :
        if row[ k ].startswith( v ) : bulk_rows.append( row[ "id" ] )

    if len( bulk_rows ) > 0 :
        delete_bulk( table , bulk_rows )


def sample_data( ) :

    delete_testdata( "account" )
    delete_testdata( "api" )

    delete_testdata( "group" )

    delete_testdata( "port" )
    delete_testdata( "pin" )
    delete_testdata( "unit" )

    ####

    config = { }

    # GROUPS
    for i in range( 10 ) :
        config[ f"group{i}_name" ] = _util.get_test_uid( postfix = f"{i}_GROUP" )
        row_data = { "name" : config[ f"group{i}_name" ] , "enable" : 1 }
        create( "group" , row_data )

    ####

    # USERS
    for i in range( 10 ) :
        account_id = create( "account" , { "name" : _util.get_test_uid( postfix = f"{i}_USER" ) , "enable" : 1 , "email" :  f"nom_user_test{i}@sparc.space" , "password" : f"{i}_USER" , "email_confirmed" : 1 } )
        
        options = {
            "api" : { "account_id" : account_id , "name" : _util.get_test_uid( postfix = f"{i}_USER" ) , "enable" : 1 } ,
            "group" : [ config[ f"group0_name" ] ] 
        } 
        create_user( options )

    ####
    # MODELS
    for i in range( 10 ) :
        account_id = create( "account" , { "name" : _util.get_test_uid( postfix = f"{i}_MODEL" ) , "enable" : 1 , "email" :  f"nom_model_test{i}@sparc.space" , "password" : f"{i}_MODEL" , "email_confirmed" : 1 } )
        
        options = {
            "api" : { "account_id" : account_id , "name" : _util.get_test_uid( postfix = f"{i}_MODEL" ) , "enable" : 1 } ,
            "group" : [ config[ f"group0_name" ] ] 
        } 
        create_model( options )


    # DASHBOARD (Single)
    account_id = create( "account" , { "name" : _util.get_test_uid( postfix = f"0_DASHBOARD" ) , "enable" : 1 , "email" :  f"nom_dashboard_test0@sparc.space" , "password" : f"0_DASHBOARD" , "email_confirmed" : 1 } )
    
    options = {
        "api" : { "account_id" : account_id , "name" : _util.get_test_uid( postfix = f"0_DASHBOARD" ) , "enable" : 1 } ,
        "group" : [ ] ,
        "role" : "dashboard"
    } 
    create_api_with_rolegroup( options )
