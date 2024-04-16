
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

import sys
import os
import json
import math
import time
from cbor2 import dumps , load
import zstandard
from hashlib import sha256
from importlib.metadata import version
import mysql.connector as mysql
from mysql.connector import errorcode, Error , errors
from esanom import config as _config , util as _util , pipeline as _pipeline

#####################################################################

NOMTABLES = [
    "account" ,
    "api" , "role" , "group" ,
    "api_role" , "api_group" ,
    "roleadmin" , "roleuser" , "rolemodel" , "roledashboard" ,
    "port" , "pin" , "unit" , "port_pin" ,
    "mport" , "mpin" ,
    "task" ,
    "io" , "ioblock" ,
    "pipeline" , "pipeline_task" ,
    "schedule" , "claim" ,
    "session" ,
    "log" , "system" 
]

def init( ) :

    if not "database" in _config.DATA : return

    if _config.DATA[ "database_disable_init" ] : return

    # FIXME TODO find a better way to detect that we don't want database init
    if _config.DATA[ "database" ][ "port" ].startswith( "_" ) : return
    if _config.DATA[ "database" ][ "host" ] == "" : return

    print( "ATTEMPT DB INIT" )
    time.sleep(10)

    try :
        db = mysql.connect( **_config.DATA[ "database" ] )
        cursor = db.cursor( )
    except Exception as e :
        print( f"database create_tables connect exception {e}" )
        sys.exit( 4 )

    ####

    # FIXME TODO keep account as first table to create otherwise it fails (see below)
    sql_files = NOMTABLES + [ "triggers" ]

    for sql_file in sql_files :

        sql_fp = _config.DATA[ "_package_fp" ] + f"/resources/database/{sql_file}.sql"

        ####

        if not os.path.isfile( sql_fp ) :

            cursor.close( )
            db.close( )
            print( f"create_tables not isfile {sql_fp}")
            sys.exit( 4 )

        ####

        with open( sql_fp , "r" ) as f : sql = f.read( )

        try :

            cursor.execute( sql )

        except Error as err :

            cursor.close( )
            db.close( )

            # FIXME TODO check if this is "client" run and bypass database stuff
            # FIXME TODO keep account as first table to create otherwise it fails
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR and sql_file == "account" :
                #print( "DATABASE SETUP SKIPPING" )
                return

            print( f"create_tables {sql_file} {err.msg}" )
            sys.exit( 4 )

        ####

    cursor.close( )
    db.close( )

    init_tables( )

    insert_fromdict( "system" , { "key" : "database/version" , "val_str" : version( "esanom" ) } )

    insert_fromdict( "system" , { "key" : "orchestrator/time" , "val_int" : 0 } )
    insert_fromdict( "system" , { "key" : "scheduler/time" , "val_int" : 0 } )

    insert_fromdict( "system" , { "key" : "system/mailer/token" } )

    print( "DB INIT OK" )

#####################################################################

def init_tables( ) :

    # Default group
    insert_fromdict( "group" , { "name" : "default" , "enable" : 1 } )
    system_group_id = insert_fromdict( "group" , { "name" : "system" , "enable" : 1 } )

    admin_role_id = insert_fromdict( "role" , { "name" : "admin" , "enable" : 1 } )
    user_role_id = insert_fromdict( "role" , { "name" : "user" , "enable" : 1 } )

    ####

    if _config.get( "admin_account_email" ) != "" :

        admin_account_password = _config.get( "admin_account_password" ) 
        if admin_account_password == "" :
            admin_account_password = _util.generate_rhash( )
            print( f"{admin_account_password=}" )

        admin_account_id = insert_fromdict( "account" , { "email" :  _config.get( "admin_account_email" ) , "password" : admin_account_password , "name" : "_admin" , "enable" : 1 , "email_confirmed" : 1 } )

        # Give admin a role admin api
        admin_api_id = insert_fromdict( "api" , { "account_id" : admin_account_id , "name" : "_admin" , "ip" : _config.get( "admin_api_ip" ) , "enable" : 1  } )
        insert_fromdict( "api_role" , { "api_id" : admin_api_id , "role_id" : admin_role_id } )

        # Give admin a role user api and create roleruser row
        admin_api_id = insert_fromdict( "api" , { "account_id" : admin_account_id , "name" : "_admin_system_user" , "ip" : "127." , "enable" : 1  } )
        insert_fromdict( "api_role" , { "api_id" : admin_api_id , "role_id" : user_role_id } )
        insert_fromdict( "api_group" , { "api_id" : admin_api_id , "group_id" : system_group_id } )
        insert_fromdict( "roleuser" , { "api_id" : admin_api_id  } )

    #####

    # model/dashboard role
    insert_fromdict( "role" , { "name" : "model" , "enable" : 1 } )
    insert_fromdict( "role" , { "name" : "dashboard" , "enable" : 1 } )

#####################################################################

def wait_until_ready( retries = 20 ) :

    counter_databaseready_retries = retries
    while ready_check( ) == None :
        print( "Waiting for database ready" )
        counter_databaseready_retries = counter_databaseready_retries - 1
        if counter_databaseready_retries == 0 : raise Exception( "database.ready" )
        time.sleep( 3 )
    print( "Database ready" )
    time.sleep( 3 )
    return( True )

def ready_check( ) :

    try :
        rows = db_query_select_rows( "SHOW TABLES LIKE 'api';" )
        if rows == None : return( None )
        if len( rows ) != 1 : return( None )
        return( True )
    except Exception as e :
        print(f"database ready_check {e}")
        return( None )

#####################################################################

def insert_fromdict( table , data ) :

    if not table in NOMTABLES : return( None )

    data_keys = list( data.keys( ) )

    cols = [  ]
    vals = [  ]
    qu = [  ]

    for data_key in data_keys :
        cols.append( f"`{data_key}`" )
        vals.append( data[ data_key ] )
        qu.append( "%s" )

    q_table = f"`{table}`"
    q_cols = ",".join( cols )
    q_places = ",".join( qu )

    sql = f"INSERT INTO {q_table} ( {q_cols} ) VALUES( {q_places} )" 

    #print(sql)

    return( db_query_insert( sql , vals ) )

def update_fromdict( table , id , data , cid = "id" ) :

    if not table in NOMTABLES : return( None )

    kset = [ ]
    vals = [ ]

    data_keys = list( data.keys( ) )
    for data_key in data_keys :
        kset.append( f"`{data_key}`=%s" )
        vals.append( data[ data_key ] )

    vals.append( id )

    kset_str = ",".join( kset )

    sql = f"UPDATE `{table}` SET {kset_str} WHERE `{cid}`=%s LIMIT 1"

    db_query_update( sql , vals )

def delete_fromid( table , id ) :
    
    if not table in NOMTABLES : return( None )

    sql = f"DELETE from `{table}` WHERE id=%s LIMIT 1"
    vals = [ id ]

    return( db_query_delete( sql , vals ) )

#####################################################################

def db_query_insert( sql , params = None ) :

    #print(sql)
    #print(params)

    # FIXME TODO test for failure! Check other db_* functions
    db = mysql.connect( **_config.DATA[ "database" ] , autocommit = True )
    cursor = db.cursor( )

    lid = None

    try : 
        if params == None : params = ( )
        cursor.execute( sql , params )
        lid = cursor.lastrowid
    except errors.IntegrityError as e :
        cursor.close( )
        db.close( )
        raise Exception( f"database query_insert IntegrityError {e}" )
    except mysql.Error as e :
        cursor.close( )
        db.close( )
        raise Exception( f"database query_insert Error {e}" )

    cursor.close( )
    db.close( )

    return( lid )

def db_query_update( sql , params = None ) :

    db = mysql.connect( **_config.DATA[ "database" ] , autocommit = True )
    cursor = db.cursor( )

    try :
        if params == None : params = ( )
        cursor.execute( sql , params )
    except mysql.Error as e :
        cursor.close( )
        db.close( )
        raise Exception( f"{e}" )

    cursor.close( )
    db.close( )

def db_query_select_row( sql , params = None , rdict = True ) :

    db = mysql.connect( **_config.DATA[ "database" ] )
    cursor = db.cursor( buffered = False , dictionary = rdict )

    if params == None : params = ( )

    try :
        cursor.execute( sql , params )
    except mysql.Error as e :
        cursor.close( )
        db.close( )
        raise Exception( f"{e}" )

    rows = cursor.fetchall( )

    cursor.close( )
    db.close( )

    if len( rows ) != 1 : return( None )

    return( rows[ 0 ] )

def db_query_select_rows( sql , params = None , rdict = True ) :

    db = mysql.connect( **_config.DATA[ "database" ] )
    cursor = db.cursor( buffered = False , dictionary = rdict )

    if params == None : params = ( )

    try :
        cursor.execute( sql , params )
    except mysql.Error as e :
        cursor.close( )
        db.close( )
        raise Exception( f"{e}" )

    rows = cursor.fetchall( )

    cursor.close( )
    db.close( )

    return( rows )


def db_query_delete(  sql , params = ( ) ) :

    db = mysql.connect( **_config.DATA[ "database" ] , autocommit = True )
    cursor = db.cursor( )

    try :
        cursor.execute( sql , params )
    except mysql.Error as e :
        cursor.close( )
        db.close( )
        raise Exception( f"{e}" )

    cursor.close( )
    db.close( )

            
#####################################################################

def api_getbytoken( token ) :

    sql = "SELECT api.*,role.name AS role_name FROM api,api_role,role WHERE api.token=%s AND api_role.api_id=api.id AND api_role.role_id=role.id LIMIT 1"

    params = ( token , )

    return( db_query_select_row( sql , params ) )

def api_getbytoken_lax( token ) :

    api_name_like = f"%{token}"

    sql = "SELECT api.*,role.name AS role_name FROM api,api_role,role WHERE api.name LIKE %s AND api_role.api_id=api.id AND api_role.role_id=role.id LIMIT 1"

    params = ( api_name_like , )

    return( db_query_select_row( sql , params ) )



#####################################################################

def admin_state( db , row_id = None ) :

    if not db in NOMTABLES : return( None )

    if row_id == None :
        return( db_query_select_rows( f"SELECT * from `{db}`" ) )
    else :
        return( db_query_select_rows( f"SELECT * from `{db}` where id=%s LIMIT 1" , [row_id]) )


#####################################################################

def model_state_rolemodel( api_id ) :
    rolemodel = db_query_select_row(
        "SELECT name,type,specs,enable,updateable,user_api_ip_prefix,heartbeats,created_at,updated_at,heartbeat_at from rolemodel where api_id=%s LIMIT 1" ,
        ( api_id , )
    )

    return( rolemodel )

def model_state_group( api_id ) :
    
    sql = "SELECT group.name FROM `api`,`group`,`api_group` WHERE api.id=%s AND api.id=api_group.api_id AND `group`.id=api_group.group_id"
    params = [ api_id ]
    rows = db_query_select_rows( sql , params )

    names = [ ]

    for row in rows : names.append( row[ "name" ] )

    return( names )

def model_specs_updateable( api_id ) :

    if not _config.DATA[ "server_security_lax" ] : return( True )

    # Test if allowed to insert/update rolemodel
    row = db_query_select_row(
        "SELECT enable,updateable from rolemodel where api_id=%s LIMIT 1" ,
        ( api_id , )
    )

    if row == None : return( True )
    if row[ "updateable" ] == 1 : return( True )
    return( False )


def model_specs( api_id , specs ) :

    #name/stype

    row = db_query_select_row(
        "SELECT id,name,enable,updateable,specs from rolemodel where api_id=%s LIMIT 1" ,
        ( api_id , )
    )

    ####

    if row == None :

        # FIXME TODO we are setting the specs_type to default model - this is already defined in schema
        rolemodel_id = db_query_insert(
            "INSERT INTO rolemodel (api_id, name , type, specs) VALUES(%s,%s,%s,%s)" ,
            ( api_id , specs.get( "name" ) , specs.get( "type" , "model" ) , json.dumps( specs ) ) 
        )

        return( rolemodel_id )

    ####

    rolemodel_id = row[ "id" ]

    if json.loads( row[ "specs" ] ) == specs : return( rolemodel_id )

    ####
    if not _config.DATA[ "server_security_lax" ] :
        if row[ "enable" ] == 1 :
            raise Exception( f"NOP ENABLED {api_id}" )

        if row[ "updateable" ] == 0 :
            raise Exception( f"NOP NOT UPDATEABLE {api_id}" )
    ####

    #if row[ "name" ] != specs.get( "name" ) :
    #    print( f"NAME MISMATCH {row['name']} -> {specs.get('name')}" )
    #    return( None )

    sql = "UPDATE rolemodel SET name=%s,updateable=0,specs=%s WHERE id=%s LIMIT 1"
    vals = ( specs[ "name" ] , json.dumps( specs ) , rolemodel_id )

    db_query_update( sql , vals )

    return( rolemodel_id )

#####################################################################

def user_state_model( api_id ) :

    models = api_model( api_id ) 

    names = [ ] 
    
    for model in models : names.append( model[ "name" ] )

    return( names )

def user_state_group( api_id ) :
    sql = "SELECT group.name FROM `api`,`group`,`api_group` WHERE api.id=%s AND api.id=api_group.api_id AND `group`.id=api_group.group_id"
    params = [ api_id ]
    rows = db_query_select_rows( sql , params )
    names = [ ]
    for row in rows :
        names.append( row[ "name" ] )
    return( names )

def user_state_pipeline( api_id ) :

    sql = "SELECT id FROM roleuser WHERE api_id=%s LIMIT 1"
    row = db_query_select_row( sql , [ api_id ] ) 
    if row == None : return( None )
    roleuser_id = row[ "id" ]  

    ####

    sql = "SELECT name , status , archived FROM pipeline WHERE roleuser_id=%s AND archived=0 LIMIT 1"
    rows = db_query_select_rows( sql , [ roleuser_id ] ) 
    if row == None : return( None )

    return( rows )



def user_specs( api_id , name ) :

    groups = db_query_select_rows(
        "SELECT group_id from api_group where api_id=%s" ,
        [ api_id ] 
    )
    if len( groups ) == 0 : return( [ ] )
    #print(groups)

    g_ids = [ ]
    for r in groups : g_ids.append( r[ "group_id" ] )

    ####

    in1 = ",".join( map( str , g_ids ) )
    groups_users = db_query_select_rows(
        f"SELECT api_id from api_group where api_id!=%s AND group_id IN ({in1})" ,
        [ api_id ] 
    )
    if len( groups_users ) == 0 : return( [ ] )
    #print(groups_users)
    a_ids = [ ]
    for r in groups_users : a_ids.append( r[ "api_id" ] )

    ####

    in1 = ",".join( map( str , a_ids ) )
    where1 = "api_role.api_id=api.id AND role.id=api_role.role_id AND role.name='model'"
    model_api_ids = db_query_select_rows(
        f"SELECT api.id from api,role,api_role where api.id IN (%s) AND {where1}" ,
        [ in1 ]
    )
    if len( model_api_ids ) == 0 : return( [ ] )
    #print(model_api_ids)

    ####

    rows = db_query_select_rows(
        f"SELECT specs from rolemodel where name=%s AND api_id IN (%s)" ,
        [ name , in1 ]
    )

    if len( rows ) != 1 :
        print( f"multiple rows...? {api_id} {name}" )
        return( [ ] )


    return( rows[ 0 ][ "specs" ] )


def user_model_id( api_id , model_name ) :

    groups = db_query_select_rows(
        "SELECT group_id from api_group where api_id=%s" ,
        [ api_id ] 
    )
    if len( groups ) == 0 : return( [ ] )
    #print(groups)

    g_ids = [ ]
    for r in groups : g_ids.append( r[ "group_id" ] )

    ####

    in1 = ",".join( map( str , g_ids ) )
    groups_users = db_query_select_rows(
        f"SELECT api_id from api_group where api_id!=%s AND group_id IN ({in1})" ,
        [ api_id ] 
    )
    if len( groups_users ) == 0 : return( [ ] )
    #print(groups_users)
    a_ids = [ ]
    for r in groups_users : a_ids.append( r[ "api_id" ] )

    ####

    in1 = ",".join( map( str , a_ids ) )
    where1 = "api_role.api_id=api.id AND role.id=api_role.role_id AND role.name='model'"
    model_api_ids = db_query_select_rows(
        f"SELECT api.id from api,role,api_role where api.id IN (%s) AND {where1}" ,
        [ in1 ]
    )
    if len( model_api_ids ) == 0 : return( [ ] )
    #print(model_api_ids)

    ####

    rows = db_query_select_rows(
        f"SELECT id from rolemodel where name=%s AND api_id IN ({in1})" ,
        [ model_name ]
    )

    if len( rows ) != 1 :
        print( f"rows!=1 {api_id} {model_name}" )
        return( None )

    return( rows[ 0 ][ "id" ] )


#####################################################################

def api_model( api_id ) :

    # Select group ids api belongs to
    groups = db_query_select_rows(
        "SELECT group_id from api_group where api_id=%s" ,
        [ api_id  ]
    )
    if len( groups ) == 0 : return( [ ] )
    #print( f"groups {groups}" )

    g_ids = [ ]
    for r in groups : g_ids.append( r[ "group_id" ] )
    #print( f"g_ids {g_ids}" )

    ####

    # Select api ids that belong to groups ids (not including this one)
    in1 = ",".join( map( str , g_ids ) )
    groups_users = db_query_select_rows(
        f"SELECT api_id from api_group where api_id!=%s AND group_id IN ({in1})" ,
        [ api_id ] 
    )
    if len( groups_users ) == 0 : return( [ ] )
    #print(f"groups_users {groups_users}")

    a_ids = [ ]
    for r in groups_users : a_ids.append( r[ "api_id" ] )

    ####

    in1 = ",".join( map( str , a_ids ) )
    where1 = "api_role.api_id=api.id AND role.id=api_role.role_id AND role.name='model'"
    model_api_ids = db_query_select_rows(
        f"SELECT api.id from api,role,api_role where api.id IN ({in1}) AND {where1}" 
    )
    if len( model_api_ids ) == 0 : return( [ ] )
    #print(f"model_api_ids {model_api_ids}")
    #print(f"in1 {in1}")

    ####

    rows = db_query_select_rows(
        f"SELECT name,specs from rolemodel where enable=1 AND api_id IN ({in1})"
    )
    #print(f"rows {rows}")

    return( rows )

##########################

def model_truncate( model_api_id ) :

    row = db_query_select_row( f"SELECT id from `rolemodel` where api_id=%s LIMIT 1" , [ model_api_id ] )
    if row == None : return

    rolemodel_id = row[ "id" ]

    db_query_delete( f"DELETE from `mport` WHERE rolemodel_id=%s" , [ rolemodel_id ] )    

def port_all_names( ) :

    port_names = [ ]
    rows = db_query_select_rows( f"SELECT name from `port`" )
    if rows == None : return( port_names )

    for row in rows : port_names.append( row[ "name" ] )

    return( port_names )

def verify_portpinunit( specs_io ) :

    if not "name" in specs_io : return( None )

    ####

    row = db_query_select_row( f"SELECT id from `port` where name=%s LIMIT 1" , [ specs_io[ "name" ] ] )
    if row == None :
        print( f"no port found {specs_io['name']}" )
        return( None )
    port_id = row[ "id" ]

    ####

    if not "pins" in specs_io : return( True )

    ####

    for pin in specs_io[ "pins" ] :

        if not "name" in pin :
            print( f"not name in pin {specs_io['name']}" )
            return( None )

        row = db_query_select_row( f"SELECT id from `pin` where name=%s LIMIT 1" , [ pin[ "name" ] ] )
        if row == None :
            print( f"no pin row {specs_io['name']} -> {pin['name']}" )
            return( None )
        pin_id = row[ "id" ]

        row = db_query_select_row( f"SELECT id from `port_pin` where port_id=%s AND pin_id=%s LIMIT 1" , [ port_id , pin_id ] )
        if row == None :
            print( f"no port_pin row {specs_io['name']} -> {pin['name']}" )
            return( None )

        if not "unit" in pin : continue

        row = db_query_select_row( f"SELECT id from `unit` where pin_id=%s and name=%s LIMIT 1" , [ pin_id , pin[ "unit" ] ] )
        if row == None :
            print( f"no unit row {specs_io['name']} -> {pin['name']} -> {pin['unit']}" )
            return( None )

    return( True )


def unit_get_bypin( pin_id , unit_name = None ) :

    units = db_query_select_rows( f"SELECT `id`,`name`,`default` FROM `unit` WHERE pin_id={pin_id}" )

    if len( units ) == 0 : return( None )

    ####

    for unit in units :
        if unit[ "name" ] == unit_name :
            return( unit[ "id" ] )

    for unit in units :
        if unit[ "default" ] == 1 :
            return( unit[ "id" ] )

    return( None )


def process_specs_io( specs_io , rolemodel_id , direction ) :
            
    if not "name" in specs_io : return( None )

    port_row = db_query_select_row( "SELECT id,name from port where name=%s" , [ specs_io[ "name" ] ] )
    if port_row == None :
        print( f"port_row None {specs_io['name']}")
        return( None )

    ####

    row_data = { "rolemodel_id" : rolemodel_id , "port_id" : port_row[ "id" ] , "direction" : direction }

    row_data.update( _util.dict_scan( specs_io , [ "enable" , "visible" , "cardinal" , "pipeline" , "download" , "read" , "write" ] ) )

    mport_id = insert_fromdict( "mport" , row_data )
    if mport_id == None :
        print( f"process_specs_io mport_id None {port_row['name']} {row_data}" )
        return( None )

    ####

    pins = db_query_select_rows( f"SELECT pin.id as pin_id , pin.name as pin_name FROM port_pin,pin WHERE port_id={port_row['id']} AND port_pin.pin_id = pin.id" )

    for pin in pins :

        # Init with default unit (if any)
        # FIXME TODO maybe use a faster query rather than the same generic one when unit name is given
        pin_unit = unit_get_bypin( pin[ "pin_id" ] )
        if pin_unit == None :
            print( "no unit?" )
            return( None )

        mpin_row = {
            "mport_id" : mport_id , "pin_id" : pin[ "pin_id" ] , "unit_id" : pin_unit 
        } 

        ####

        if "pins" in specs_io :
            for spec_pin in specs_io[ "pins" ] :
                if spec_pin[ "name" ] == pin[ "pin_name" ] :
                    mpin_row.update( _util.dict_scan( spec_pin , [ "override" , "enable" , "visible" , "pipeline" , "download" , "read" , "write" ] ) )

                    pin_unit = unit_get_bypin( pin[ "pin_id" ] , spec_pin.get( "unit" , None ) )
                    if pin_unit == None :
                        print( "no unit?" )
                        return( None )

                    mpin_row[ "unit_id" ] = pin_unit

                    break

        ####

        insert_fromdict( "mpin" , mpin_row )


    return( True )

def io_info( model_name ) :

    data = { "inputs" : [ ] , "outputs" : [ ] }

    ####

    rolemodel_row = db_query_select_row( "SELECT * from rolemodel WHERE name=%s LIMIT 1" , [ model_name ] )
    if rolemodel_row == None :
        print( f"rolemodel_row {model_name}" ) 
        return( None )

    ####

    mport_rows = db_query_select_rows( "SELECT * from mport WHERE rolemodel_id=%s" , [ rolemodel_row[ "id" ] ] )
    if mport_rows == None :
        print( f"mport_rows {model_name=}" ) 
        return( None )

    ####

    for mport_row in mport_rows :
       

        port_id = mport_row[ "port_id" ]

        port_row = db_query_select_row( "SELECT * from port WHERE id=%s LIMIT 1" , [ port_id ] )
        if port_row == None :
            print( f"port_row" ) 
            return( None )

        port_data = { "name" : port_row[ "name" ] , "cardinal" : mport_row[ "cardinal" ] } 

        #### 

        port_pin_rows = db_query_select_rows( "SELECT * from port_pin WHERE port_id=%s" , [ port_id ] )
        if port_pin_rows == None :
            print( f"port_pin_rows" )
            return( None )

        ####

        #print(port_pin_rows)

        pins = [ ]
        for port_pin_row in port_pin_rows :
            pin_row = db_query_select_row( "SELECT * from pin WHERE id=%s LIMIT 1" , [ port_pin_row[ "pin_id" ] ] )
            if pin_row == None :
                print( f"io_info pin_row" )
                return( None )

            pin_data = { "name" : pin_row[ "name" ] , "cardinal" : port_pin_row[ "cardinal" ] , "type" : pin_row[ "type" ] }

            ####

            mpin_row = db_query_select_row( "SELECT * from mpin WHERE mport_id=%s AND pin_id=%s LIMIT 1" , [ mport_row[ "id" ] , port_pin_row[ "pin_id" ] ] )

            if mpin_row != None and mpin_row[ "override" ] != None :
                pin_data[ "override" ] = mpin_row[ "override" ]

            ####

            pins.append( pin_data )


        port_data[ "pins" ] = pins

        #### 

        data[ mport_row[ "direction" ] ].append( port_data )

        ####

    return( data )

def io_data_from_taskuid( task_uid ) :
    task_row = db_query_select_row( "SELECT * from task WHERE uid=%s LIMIT 1" , [ task_uid ] )

    return( io_data( task_row[ "id" ] , task_rolemodel_name_alt = task_row["rolemodel_name_alt"] ) )


def io_data( task_id , task_rolemodel_name_alt = "_" ) :

    data = { }

    ####

    io_rows = db_query_select_rows( "SELECT * from io WHERE task_id=%s" , [ task_id ] )
    if io_rows == None :
        print( f"io_rows" )
        return( None )

    #### 

    for io_row in io_rows :

        mpin_row = db_query_select_row( "SELECT * from mpin WHERE id=%s" , [ io_row[ "mpin_id" ] ] )
        if mpin_row == None :
            print( f"mpin_row" ) 
            return( None )

        ####

        mport_row = db_query_select_row( "SELECT * from mport WHERE id=%s" , [ mpin_row[ "mport_id" ] ] )
        if mport_row == None :
            print( f"mport_row" ) 
            return( None )

        ####

        port_row = db_query_select_row( "SELECT * from port WHERE id=%s" , [ mport_row[ "port_id" ] ] )
        if port_row == None :
            print( f"port_row" ) 
            return( None )

        ####

        unit_row = db_query_select_row( "SELECT * from unit WHERE id=%s" , [ mpin_row[ "unit_id" ] ] )
        if unit_row == None :
            print( f"unit_row" ) 
            return( None )

        ####

        pin_row = db_query_select_row( "SELECT * from pin WHERE id=%s" , [ unit_row[ "pin_id" ] ] )
        if pin_row == None :
            print( f"pin_row" )
            return( None )

        ####

        ioblock_rows = db_query_select_rows( "SELECT block,size,hash,compressor from ioblock WHERE io_id=%s ORDER BY block ASC" , [ io_row[ "id" ] ] )
        if ioblock_rows == None :
            print( f"ioblock_rows" ) 
            return( None )

        ####

        cmd_key = f"/{task_rolemodel_name_alt}/{mport_row['direction']}/{port_row['name']}/{io_row['port_ordinal']}/{pin_row['name']}/{io_row['pin_ordinal']}"

        #data[ io_row[ "uid" ] ] = {
        data[ cmd_key ] = {

            "io" : {
                "io_uid" : io_row[ "uid" ] ,
                "io_blocks" : io_row[ "blocks" ] ,
                "ioblock_rows" : ioblock_rows 
            } ,

            "rolemodel_name_alt" : task_rolemodel_name_alt ,

            "current_role_name" : io_row[ "current_role_name" ] ,
            "mport_direction" : mport_row[ "direction" ] ,
            "port_name" : port_row[ "name" ] ,
            "port_ordinal" : io_row[ "port_ordinal" ] ,
            "pin_name" : pin_row[ "name" ] ,
            "pin_ordinal" : io_row[ "pin_ordinal" ] ,

            "size" : io_row[ "size" ] ,
            "hash" : io_row[ "hash" ] ,
            "type" : pin_row[ "type" ]
        }

        ####

    return( data )



def io_insert( task_uid , rdata , pred_io_uid = None , is_local = False ) :

    print(f"{rdata=}")

    task_row = db_query_select_row( "SELECT * from task WHERE uid=%s LIMIT 1" , [ task_uid ] )
    if task_row == None : raise Exception( f"task_row not found" )

    task_id = task_row[ "id" ]
    rolemodel_id = task_row[ "rolemodel_id" ]

    ####

    _util.validate_pipeline_submit_io( rdata )

    ####

    port_row = db_query_select_row( "SELECT * from port WHERE name=%s LIMIT 1" , [ rdata.get( "port_name" ) ] )
    if port_row == None : raise Exception( f"port_row not found" )

    port_id = port_row[ "id" ]

    mport_row = db_query_select_row( "SELECT * from mport WHERE rolemodel_id=%s AND port_id=%s AND direction=%s LIMIT 1" , [ rolemodel_id , port_id , rdata.get( "mport_direction" ) ] )
    if mport_row == None : raise Exception( f"mport_row not found" )

    ####

    if mport_row[ "cardinal" ] > 0 and rdata.get( "port_ordinal" ) > mport_row[ "cardinal" ] : raise Exception( f"port_ordinal to big" )

    ####

    pin_row = db_query_select_row( "SELECT * from pin WHERE name=%s LIMIT 1" , [ rdata.get( "pin_name" , None ) ] )
    if pin_row == None : raise Exception( f"pin_row not found" )

    pin_id = pin_row[ "id" ]

    ####

    port_pin_row = db_query_select_row( "SELECT * from port_pin WHERE port_id=%s AND pin_id=%s LIMIT 1" , [ port_id , pin_id ] )
    if port_pin_row == None : raise Exception( f"port_pin_row not found" )

    if port_pin_row[ "cardinal" ] > 0 and rdata.get( "pin_ordinal" ) > port_pin_row[ "cardinal" ] : raise Exception( f"pin_ordinal to big" )

    ####

    unit_row = db_query_select_row( "SELECT * from unit WHERE pin_id=%s AND `default`=1 LIMIT 1" , [ pin_id ] )
    if unit_row == None : raise Exception( f"unit_row not found" )

    mpin_row = db_query_select_row( "SELECT * from mpin WHERE mport_id=%s AND unit_id=%s LIMIT 1" , [ mport_row[ "id" ] , unit_row[ "id" ] ] )
    if mpin_row == None : raise Exception( f"mpin_row not found" )

    if not is_local :
        if mpin_row.get( "override" ) is not None : raise Exception( f"mpin_row override set" )

    ####

    io_row = {
        "task_id" : task_id ,
        "mpin_id" : mpin_row[ "id" ] ,
        "current_role_name" : rdata.get( "current_role_name" ) ,
        "port_ordinal" : rdata.get( "port_ordinal" ) ,
        "pin_ordinal" : rdata.get( "pin_ordinal" ),
        "size" : rdata.get( "size" ) ,
        "hash" : rdata.get( "hash" ) ,
        "blocks" : math.ceil( rdata.get( "size" ) / 8388608 ) 
    }

    io_id = insert_fromdict( "io" , io_row )
    if io_id == None : raise Exception( "io_id none"  ) 

    io_row = db_query_select_row( "SELECT * from io WHERE id=%s LIMIT 1" , [ io_id ] )
    if io_row == None : raise Exception( f"io_row not found" )

    ####
    if pred_io_uid != None :
        pred_io_row = db_query_select_row( "SELECT * from io WHERE uid=%s LIMIT 1" , [ pred_io_uid ] )
        if pred_io_row == None : raise Exception( f"pred_io_row not found" )
        pred_io_row_id = pred_io_row[ "id" ]

        #print(f"{pred_io_row_id}")

        pred_ioblock_rows = db_query_select_rows( "SELECT * from ioblock WHERE io_id=%s LIMIT 1" , [ pred_io_row_id ] )
        #print(pred_ioblock_rows)
        if len( pred_ioblock_rows ) == 0 : raise Exception( f"no pred_ioblock_rows...?" )
        for pred_ioblock_row in pred_ioblock_rows :

            pred_ioblock_row.pop( "id" )
            pred_ioblock_row.pop( "created_at" )
            pred_ioblock_row.pop( "updated_at" )
            pred_ioblock_row[ "io_id" ] = io_id

            insert_fromdict( "ioblock" , pred_ioblock_row )



    ####

    return( io_row[ "uid" ] )


def io_block_status( io_uid ) :

    io_row = db_query_select_row( "SELECT * from io WHERE uid=%s LIMIT 1" , [ io_uid ] )
    if io_row == None : raise Exception( f"io_row none" ) 

    ioblock_row = db_query_select_row( "SELECT * from ioblock WHERE io_id=%s order by block DESC LIMIT 1" , [ io_row[ "id" ] ] )
    if ioblock_row == None :
        block_current = 0
    else :
        block_current = ioblock_row[ "block" ] + 1

    data = {
        "blocks_total" : io_row[ "blocks" ] ,
        "blocks_current" : block_current
    }

    return( data )


def user_pipeline( api_id , name ) :

    roleuser_row = db_query_select_row( "SELECT id from roleuser WHERE api_id=%s LIMIT 1" , [ api_id ] )
    if roleuser_row == None : raise Exception( f"roleuser_row not found" )

    ####

    pipeline_row = db_query_select_row( "SELECT * from pipeline WHERE roleuser_id=%s AND name=%s AND archived=0 LIMIT 1" , [ roleuser_row[ "id" ] , name ] )

    if pipeline_row == None :

        r = { "name" : name , "roleuser_id" : roleuser_row[ "id" ] }

        pipeline_id = insert_fromdict( "pipeline" , r )
        if pipeline_id == None : raise Exception( f"pipeline insert" )

        pipeline_row = db_query_select_row( "SELECT * from pipeline WHERE roleuser_id=%s AND name=%s AND archived=0 LIMIT 1" , [ roleuser_row[ "id" ] , name ] )

    return( pipeline_row )

def pipeline_nodes( pipeline_id ) :
    #pipeline.nodes["m1"]={"name":"model_test_simple0"}

    nodes = { }
        
    pipeline_task_rows = db_query_select_rows( "SELECT * from pipeline_task WHERE pipeline_id=%s" , [ pipeline_id ] )
    if len( pipeline_task_rows ) == 0 : return( { } )

    task_ids = set( )
    for pipeline_task_row in pipeline_task_rows :
        task_ids.update( [ pipeline_task_row[ "task_id" ] ] )
        if pipeline_task_row[ "next_task_id" ] != None : task_ids.update( [ pipeline_task_row[ "next_task_id" ] ] )

    nodes = { }
    for task_id in task_ids :
        task_row = db_query_select_row( "SELECT * from task WHERE id=%s" , [ task_id ] )
        rolemodel_row = db_query_select_row( "SELECT * from rolemodel WHERE id=%s" , [ task_row[ "rolemodel_id" ] ] )
        nodes[ task_row[ "rolemodel_name_alt" ] ] = {
            "name" : rolemodel_row[ "name" ] ,
            "task_uid" : task_row[ "uid" ] ,
            "task_done" : task_row[ "done" ] ,
            "task_status" : task_row[ "status" ] ,
            "ignore_pred_fail" : rolemodel_row[ "ignore_pred_fail" ] 
        }

    return( nodes )

def pipeline_bulk_update_status( pipeline_ids , status ) :

    sql = f"UPDATE `pipeline` SET status=%s where id=%s LIMIT 1"
    for pipeline_id in pipeline_ids :
        db_query_update( sql , [ status , pipeline_id ] )


def pipeline_object( pipeline_row ) :

    pipeline = _pipeline.Pipeline( pipeline_row[ "name" ] )
    pipeline.status = pipeline_row[ "status" ]
    pipeline.done = pipeline_row[ "done" ]
    pipeline.archived = pipeline_row[ "archived" ]
    
    ####

    for model_name in user_state_model( api_id = pipeline_row[ "roleuser_id" ] ) :
        pipeline.io_info[ model_name ] = io_info( model_name )

    ####
    pipeline.nodes = pipeline_nodes( pipeline_row[ "id" ] )

    if pipeline_row[ "status" ] != "RESERVED" :

        for i , ( k , v ) in enumerate( pipeline.nodes.items( ) ) :
            pipeline.io_data.update( io_data_from_taskuid( v[ "task_uid" ] ) )
            pipeline.io_info[ v[ "name" ] ] = io_info( v[ "name" ] ) 

    ####

    pipeline_task_rows = db_query_select_rows( "SELECT * from pipeline_task where pipeline_id=%s" , [ pipeline_row[ "id" ] ] )

    for pipeline_task_row in pipeline_task_rows :
        if pipeline_task_row[ "next_task_id" ] == None : continue
        task_row = db_query_select_row( "SELECT * FROM task where id=%s LIMIT 1" , [ pipeline_task_row[ "task_id" ] ] )
        next_task_row = db_query_select_row( "SELECT * FROM task where id=%s LIMIT 1" , [ pipeline_task_row[ "next_task_id" ] ] )
        pipeline.connect( task_row[ "rolemodel_name_alt" ] , next_task_row[ "rolemodel_name_alt" ] )

    ####

    return( pipeline )


def model_flush_ports( rolemodel_id ) :

    sql = f"DELETE from `pin` WHERE rolemodel_id=%s;"
    db_query_delete( sql , [ rolemodel_id ] )

    sql = f"DELETE from `port` WHERE rolemodel_id=%s; "
    db_query_delete( sql , [ rolemodel_id ] )



def model_load_ports( rolemodel_id , ports , interfaces_global = False ) :

    #print( ports )

    rolemodel_row = db_query_select_row( "SELECT * from rolemodel WHERE id=%s LIMIT 1" , [ rolemodel_id ] )
    if rolemodel_row == None : raise Exception("rolemodel_row None" ) 

    interface_namespace = f"{rolemodel_row['name']}:"
    if interfaces_global : interface_namespace = ""

    for port_data in ports :
        if "name" not in port_data : raise Exception( f"name not in port" )
        if "pins" not in port_data : raise Exception( f"pins not in port" )

        port_name = f"{interface_namespace}{port_data['name']}"

        port_row = db_query_select_row( "SELECT * from port where name=%s LIMIT 1" , [ port_name ] )
        if port_row != None : raise Exception( f"port {port_name} already exists" )

        port_id = insert_fromdict( "port" , { "name" : port_name , "rolemodel_id" : rolemodel_id , "visible" : 0 } )

        print( f"{port_name=} {port_id=}" )

        for pin_data in port_data[ "pins" ] :
            if "name" not in pin_data : raise Exception( f"name not in pin" )
            if "units" not in pin_data : raise Exception( f"units not in pin" )

            ####
            
            pin_name_global = f"{pin_data['name']}"
            pin_row_global = db_query_select_row( "SELECT * from pin where name=%s LIMIT 1" , [ pin_name_global ] )

            ####

            if pin_row_global == None :
                pin_name = f"{interface_namespace}{pin_data['name']}"
                pin_row = db_query_select_row( "SELECT * from pin where name=%s LIMIT 1" , [ pin_name ] )

                if pin_row != None : 
                    pin_id = pin_row[ "id" ]
                else :
                    pin_id = insert_fromdict( "pin" , { "name" : pin_name , "rolemodel_id" : rolemodel_id , "type" : pin_data.get( "type" , "" ) , "visible" : 0 } )
            else :
                pin_id = pin_row_global["id"]

            #print( f"{pin_name=} {pin_id=}" )
            ####

            insert_fromdict( "port_pin" , { "port_id" : port_id , "pin_id" : pin_id , "cardinal" : pin_data.get( "cardinal" , 1 ) } )


            ####
            flag_unit_default_found = False
            for unit_data in pin_data[ "units" ] :
                if "name" not in pin_data : raise Exception( f"name not in pin" )
                if "default" in pin_data and pin_data[ "default" ] == 1 :
                    flag_unit_default_found = True
                    break
            ####

            for unit_data in pin_data[ "units" ] :
                default = 0
                if not flag_unit_default_found :
                    default = 1
                    flag_unit_default_found = True
                if "default" in pin_data : default = pin_data["default"]
                unit_name = f"{unit_data['name']}"
                insert_fromdict( "unit" , { "name" : unit_name , "pin_id" : pin_id , "default" : default , "visible" : 0 } )

####

def handle_overrides( task_uid ) :
    #print( f"handle_overrides {task_uid=}" )
    task_row = db_query_select_row( "SELECT * from task where uid=%s LIMIT 1" , [ task_uid ] )

    rolemodel_id = task_row[ "rolemodel_id" ]
    mport_rows = db_query_select_rows( "SELECT * from mport where rolemodel_id=%s" , [ rolemodel_id ] )

    for mport_row in mport_rows :
        mpin_rows = db_query_select_rows( "SELECT * from mpin where mport_id=%s and override IS NOT NULL" , [ mport_row[ "id" ] ] )
        for mpin_row in mpin_rows :
            io_row = db_query_select_row( "SELECT * from io where task_id=%s AND mpin_id=%s LIMIT 1" , [ task_row["id"],mpin_row["id"] ] )
            if io_row is None : handle_override( task_row[ "id" ] , mpin_row[ "id" ] , mpin_row[ "override" ] )


def handle_override( task_id , mpin_id , mpin_override ) :

    override_sections = mpin_override.split( "," )

    ####

    for override_section in override_sections :

        override_parts = override_section.split( "/" )

        ####

        port_ordinal = int( float( override_parts[ 0 ] ) )
        pin_ordinal = int( float( override_parts[ 1 ] ) )
        override_key = override_parts[ 2 ] 

        # FIXME TODO must check if ordinals are within in range!

        ####

        cmd_val = pin_override_map( override_key , task_id ) 
        if cmd_val is None : continue

        ####

        file_data = dumps( cmd_val )
        file_hash = sha256( file_data ).hexdigest( ) 
        file_path = _util.get_io_hash_filepath( file_hash )
        with open( file_path , "wb" ) as f : f.write( file_data )
        file_size = os.path.getsize( file_path )
        #dtype = type( cmd_val ).__name__ 

        print(f"{file_path=}")

        ####
        # FIXME TODO handle if data is > than block limit (8MB)

        io_data = {
            "task_id" : task_id ,
            "mpin_id" : mpin_id ,
            "current_role_name" : "nom" ,
            "port_ordinal" : port_ordinal ,
            "pin_ordinal" : pin_ordinal ,
            "blocks" : 1 ,
            "size" : file_size ,
            "hash" : file_hash
        }

        io_id = insert_fromdict( "io" , io_data )

        ####

        if len( file_data ) > 1024 :
            cctx = zstandard.ZstdCompressor( threads = -1 , write_checksum = True )
            file_data = cctx.compress( file_data ) 
            file_compressor = "ZSTD"
        else :
            file_compressor = "NONE"

        ####

        ioblock_data = {
            "io_id" : io_id ,
            "block" : 0 ,
            "size" : file_size ,
            "hash" : file_hash ,
            "compressor" : file_compressor
        }

        insert_fromdict( "ioblock" , ioblock_data )


def pin_override_map( override_key , task_id ) :

    if override_key == "account_email" :

        pipeline_task_row = db_query_select_row( "SELECT * from pipeline_task WHERE task_id=%s OR next_task_id=%s LIMIT 1" , [ task_id , task_id ] )
        pipeline_row = db_query_select_row( "SELECT * from pipeline WHERE id=%s LIMIT 1" , [ pipeline_task_row[ "pipeline_id" ] ] )
        roleuser_row = db_query_select_row( "SELECT * from roleuser WHERE id=%s LIMIT 1" , [ pipeline_row[ "roleuser_id" ] ] )
        api_row = db_query_select_row( "SELECT * from api WHERE id=%s LIMIT 1" , [ roleuser_row[ "api_id" ] ] )

        account_row = db_query_select_row( "SELECT * from account WHERE id=%s LIMIT 1" , [ api_row[ "account_id" ] ] )

        #print(api_row[ "email" ])
        v = account_row[ "email" ]
        #print(f"{v=}")
        return( v )
        #api_row = db_query_select_row( "SELECT * from api where id=%s LIMIT 1" , [ api_id ] )
        #return( api_row[ "email" ] )

    ####

    if override_key == "api_name" :

        pipeline_task_row = db_query_select_row( "SELECT * from pipeline_task WHERE task_id=%s OR next_task_id=%s LIMIT 1" , [ task_id , task_id ] )
        pipeline_row = db_query_select_row( "SELECT * from pipeline WHERE id=%s LIMIT 1" , [ pipeline_task_row[ "pipeline_id" ] ] )
        roleuser_row = db_query_select_row( "SELECT * from roleuser WHERE id=%s LIMIT 1" , [ pipeline_row[ "roleuser_id" ] ] )
        api_row = db_query_select_row( "SELECT * from api WHERE id=%s LIMIT 1" , [ roleuser_row[ "api_id" ] ] )

        v = api_row['name']
        #print(f"{v=}")
        return( v )
        #return( pipeline_row[ "name" ] )

    ####

    if override_key == "pipeline_status" :

        pipeline_task_row = db_query_select_row( "SELECT * from pipeline_task WHERE task_id=%s OR next_task_id=%s LIMIT 1" , [ task_id , task_id ] )
        pipeline_row = db_query_select_row( "SELECT * from pipeline WHERE id=%s LIMIT 1" , [ pipeline_task_row[ "pipeline_id" ] ] )

        v = pipeline_row['name']
        #print(f"{v=}")
        return( v )
        #return( pipeline_row[ "name" ] )

    return( None )

####

