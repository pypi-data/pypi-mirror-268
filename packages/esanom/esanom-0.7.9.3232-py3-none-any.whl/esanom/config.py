
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

import os
import sys
import json
import time
from . import util as _util

#####################################################################

NOM_CONFIG_PATH = "nom_config.json"

DATA = { }

#####################################################################

def init( ) :

    global NOM_CONFIG_PATH
    global DATA

    if "NOM_CONFIG_PATH" in os.environ :
        NOM_CONFIG_PATH = os.environ[ "NOM_CONFIG_PATH" ]
        print( f"CONFIG LOADING FROM ENV {NOM_CONFIG_PATH}")

    ####
    
    cwd_fp = os.getcwd( )

    ####

    config_fp = f"{NOM_CONFIG_PATH}"
    if not NOM_CONFIG_PATH.startswith( "/" ) :
        config_fp = f"{cwd_fp}/{NOM_CONFIG_PATH}"

    ####

    if load_from_filepath( config_fp ) == None : load_from_env( )
    if "_load_from_env" not in DATA : DATA[ "_load_from_env" ] = False 

    ####

    DATA[ "_package_fp" ] = os.path.abspath( os.path.dirname( __file__ ) )
    DATA[ "_cwd_fp" ] = cwd_fp
    DATA[ "_time_created" ] = time.time( )

    if "fs_storage_path" not in DATA : DATA[ "fs_storage_path" ] = "/tmp/nom"
    if DATA[ "fs_storage_path" ] == "" : DATA[ "fs_storage_path" ] = "/tmp/nom"
    DATA[ "fs_storage_path" ].rstrip( "/" )

    ####

    # Flag for flask server debug

    config_init_default_boolean( "server_debug" )
    config_init_default_boolean( "server_security_lax" )
    config_init_default_boolean( "database_disable_init" )

    ####

    _util.print_debug( DATA )

    return

#####################################################################

def config_init_default_boolean( k , v = False ) :
    global DATA

    if k not in DATA :
        DATA[ k ] = v
        return

    if DATA[ k ] == "y" :
        DATA[ k ] = True
    else :
        DATA[ k ] = False

#####################################################################

def load_from_filepath( config_fp ) :
    global DATA

    if not os.path.isfile( config_fp ) :
        print( f"WARNING CONFIG FILE NOT FOUND {config_fp=}" )
        return( None )

    ####

    with open( config_fp ) as f :
        try :
            DATA = json.loads( f.read( ) )
            print( f"Config loaded from file config_fp = {config_fp}" )
            return( True )
        except json.decoder.JSONDecodeError as e :
            print( f"ERROR JSONDecodeError {e.msg}" )
            sys.exit( 4 )


def env_get( k ) :
    v = os.environ.get( k , "" ).strip( )
    if v.startswith( "__" ) : return( "" )
    return( v )

def load_from_env( ) :

    global DATA

    DATA = {

        "_load_from_env" : True ,

        "database" : {
            "host" : env_get( "DB_HOST" ) ,
            "port" : env_get( "DB_PORT" ) ,
            "user" : env_get( "DB_USER" ) ,
            "passwd" : env_get( "DB_PASSWD" ) ,
            "database" : env_get( "DB_DATABASE" ) 
        } ,

        "server_endpoint" : env_get( "NOM_CONFIG_SERVER_ENDPOINT" ) ,
        "server_token" : env_get( "NOM_CONFIG_SERVER_TOKEN" ) ,

        "admin_account_email" : env_get( "NOM_CONFIG_ADMIN_ACCOUNT_EMAIL" ),
        "admin_account_password" : env_get( "NOM_CONFIG_ADMIN_ACCOUNT_PASSWORD" ),

        "fs_storage_path" : env_get( "NOM_CONFIG_FS_STORAGE_PATH" ),
        "database_disable_init" : env_get( "NOM_CONFIG_DATABASE_DISABLE_INIT" ),
        "server_debug" : env_get( "NOM_CONFIG_SERVER_DEBUG" ),
        "server_security_lax" : env_get( "NOM_CONFIG_SERVER_SECURITY_LAX" ) 

    }

    print("CONFIG loaded from ENV")

    #_util.print_debug( DATA , "Config loaded from ENV" )


    #if db_host == None or db_port == None : return( None )
    #if db_user == None or db_passwd == None : return( None )
    #if db_database == None : return( None )

    #if admin_api_email == None : return( None )

    return


def update( fp ) :
    global DATA

    if not os.path.isfile( fp ) : raise Exception( f"FILE NOT FOUND {fp}" )

    with open( fp ) as f :
        try :
            data = json.loads( f.read( ) )
            DATA.update( data )
            print( f"Config updated" )
        except json.decoder.JSONDecodeError as e :
            raise Exception( f"ERROR JSONDecodeError {e.msg}" )



#####################################################################

def val( k ) :
    return( f"{k}...bar" )

def get( k ) :
    return( DATA.get( k , None ) )

def print_debug( ) :
    _util.debug_json_print( DATA )

