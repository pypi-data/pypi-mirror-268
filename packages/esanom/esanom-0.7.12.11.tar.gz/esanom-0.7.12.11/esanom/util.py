
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
import hashlib
import secrets
import json
import pickle
import time
import re

import psutil
import requests
import base64

import zstandard

from esanom import config as _config 

requests.packages.urllib3.disable_warnings( requests.packages.urllib3.exceptions.InsecureRequestWarning )

def psutil_status( ) :

    task_results = { }
    task_results[ "fs" ] = { }
    partitions = psutil.disk_partitions( )

    partition_percent_max = 0

    for partition in partitions :
        partition_data = { }
        partition_data[ "path" ] = partition[ 1 ]
        partition_data[ "percent" ] = psutil.disk_usage( partition[ 1 ] ).percent
        partition_data[ "total" ] = psutil.disk_usage( partition[ 1 ] ).total
        partition_data[ "free" ] = psutil.disk_usage( partition[ 1 ] ).free
        partition_data[ "used" ] = psutil.disk_usage( partition[ 1 ] ).used

        task_results[ "fs" ][ partition_data[ "path" ] ] = partition_data

        if partition_data[ "percent" ] > partition_percent_max: partition_percent_max = partition_data[ "percent" ]

    task_results[ "partition_percent_max" ] = partition_percent_max
    task_results[ "virtual_memory" ] = psutil.virtual_memory( )
    task_results[ "swap_memory" ] = psutil.swap_memory( )
    task_results[ "cpu_percent" ] = psutil.cpu_percent( interval = 1 , percpu = False )
    task_results[ "getloadavg" ] = psutil.getloadavg( )
    task_results[ "boot_time" ] = psutil.boot_time( )

    proc_iter = psutil.process_iter( attrs = [ "pid" , "name" , "cmdline" , "cpu_percent" , "memory_percent" ] )
    proc_iter_data = [ ]

    for p in proc_iter :
        proc_iter_data.append( p.info )

    task_results[ "process_iter" ] = proc_iter_data
    task_results[ "process_iter_len" ] = len( proc_iter_data )

    return( task_results )

def get_test_uid( prefix = "test" , postfix = "test" ) :
    h = generate_rhash( )
    return( f"{prefix}_{h}_{postfix}" )

def generate_rhash( ) :
    return( secrets.token_hex( ) )

####

def rows_scan_pluck( rows , k , v , c ) :

    for row in rows :
        if row[ k ] == v :
            if c in row : return( row[ c ] )

    return( None )

def dict_scan( pdict , plist ) :
    res = { }
    for p in plist :
        if p in pdict : res[ p ] = pdict[ p ]

    return( res )


####

def server_endpoint_url( path ) :

    return( _config.get( "server_endpoint" ) + f"{path}" )

def server_request_headers( content_type = None ) :

    token = _config.get( "server_token" )
    if token == None : raise Exception( "token None" )

    server_headers = {
        "Authorization" : f"Bearer {_config.get('server_token')}"
    }

    if content_type == "json" : server_headers[ "content-type" ] = "application/json"

    server_host = _config.get( "server_host" )
    if server_host != None : server_headers[ "Host" ] = server_host

    return( server_headers )

def request_get( path , content_type = "json" , params = None ) :

    endpoint = server_endpoint_url( path )
    headers = server_request_headers( content_type = content_type  )

    ####

    response = requests.get( endpoint , headers = headers , params = params , verify = False )

    time.sleep( float( response.headers.get( "NoM_Client_Wait" , 10 ) ) )

    if response.headers[ "content-type" ] != "application/json" : raise Exception( f"content-type != application/json" )

    data = response.json( )

    if response.status_code != 200 : raise Exception( f"status_code!=200 ({response.status_code}) {data}" )

    if not "STATUS" in data  : raise Exception( f"STATUS not found {data}" )

    if data[ "STATUS" ] != "OK" : raise Exception( f"STATUS != OK (data['STATUS']) {data}")

    if not "MESSAGES" in data  : raise Exception( f"MESSAGES not found {data}" )

    return( data[ "MESSAGES" ] )


def request_get_file( path , params = None ) :
    
    endpoint = server_endpoint_url( path )
    headers = server_request_headers( content_type = "text/html; charset=utf-8")

    ####

    response = requests.get( endpoint , headers = headers , params = params , verify = False )

    time.sleep( float( response.headers.get( "NoM_Client_Wait" , 10 ) ) )

    if response.headers[ "content-type" ] != "application/octet-stream" : raise Exception( f"content-type != application/octet-stream" )

    return( response.content )

def request_post( path , content_type = "json" , params = None , data = None ) :

    endpoint = server_endpoint_url( path )
    headers = server_request_headers( content_type = content_type  )

    ####

    data_str = "{}"
    if data != None : data_str = json.dumps( data )

    ####

    try :
        response = requests.post( endpoint , headers = headers , params = params , data = data_str , verify = False )
    except requests.exceptions.RequestException as e :
        raise Exception( f"requests.exceptions.RequestException {e}")

    time.sleep( float( response.headers.get( "NoM_Client_Wait" , 10 ) ) )

    if response.headers[ "content-type" ] != "application/json" : raise Exception( f"content-type != application/json" )

    data = response.json( )

    if response.status_code != 200 : raise Exception( f"status_code!=200 ({response.status_code}) {data}" )

    if not "STATUS" in data  : raise Exception( f"STATUS not found {data}" )

    if data[ "STATUS" ] != "OK" : raise Exception( f"STATUS != OK (data['STATUS']) {data}")

    if not "MESSAGES" in data  : raise Exception( f"MESSAGES not found {data}" )

    return( data[ "MESSAGES" ] )

def request_post_binary( path , content_type = "json" , params = None , data = None ) :

    endpoint = server_endpoint_url( path )
    headers = server_request_headers( content_type = content_type  )

    ####

    response = requests.post( endpoint , headers = headers , params = params , data = data , verify = False )

    time.sleep( float( response.headers.get( "NoM_Client_Wait" , 10 ) ) )

    if response.headers[ "content-type" ] != "application/json" : raise Exception( f"content-type != application/json" )

    data = response.json( )

    if response.status_code != 200 : raise Exception( f"status_code!=200 ({response.status_code}) {data}" )

    if not "STATUS" in data  : raise Exception( f"STATUS not found {data}" )

    if data[ "STATUS" ] != "OK" : raise Exception( f"STATUS != OK (data['STATUS']) {data}")

    if not "MESSAGES" in data  : raise Exception( f"MESSAGES not found {data}" )

    return( data[ "MESSAGES" ] )

####

def hash_str( s ) :
    return( hashlib.sha256( s.encode( "utf-8" ) ).hexdigest( ) )

def object_encode( obj ) :
    obj_ser = pickle.dumps( obj )
    return( base64.b64encode(obj_ser).decode('ascii') )

def object_decode( s ) :

    a = base64.b64decode( s )

    obj = pickle.loads( a )
    return( obj )

def print_debug( j , label = "" ) :
    print( label , end = "=" )
    print( json.dumps( j , indent = 4 , sort_keys = True , default = str) )


# FIXME TODO move this out to roleuser
def ioblock_upload( dinfo , io_uid , role  ) :
    #print(dinfo)
    #print(io_uid)
    while True :
        messages = request_get( f"/{role}_ioblock_status" , params = { "io_uid" : io_uid } )
        if not "blocks_total" in messages : raise Exception( f"ioblock_upload" )
        if not "blocks_current" in messages : raise Exception( f"ioblock_upload" )
        if messages[ "blocks_current" ] == messages[ "blocks_total" ] : break
        if messages[ "blocks_current" ] > messages[ "blocks_total" ] : raise Exception( f"blocks_current>blocks_total" )
        print( f"UPLOADING {messages}" )
        ioblock_upload_block( dinfo , io_uid , messages[ "blocks_current" ] , role )


# FIXME TODO move this out to roleuser
def ioblock_upload_block( dinfo , io_uid , blocks_current , role ) :

    #print( dinfo )

    # FIXME TODO avoid mkdirs all the time?
    if dinfo[ "type" ].startswith( "." ) :
        file_path = dinfo[ "file_path" ]
    else :
        file_path = get_io_hash_filepath( dinfo[ "hash" ] ) 

    with open( file_path , "rb" ) as f :
        f.seek( blocks_current * 8388608 , 0 )
        file_data = f.read( 8388608 )

    if len( file_data ) > 1024 :
        cctx = zstandard.ZstdCompressor( threads = -1 , write_checksum = True )
        file_data = cctx.compress( file_data ) 
        file_compressor = "ZSTD"
    else :
        file_compressor = "NONE"


    params = {
        "io_uid" : io_uid ,
        "block" : blocks_current ,
        "hash" : filedata_hash( file_data ) ,
        "compressor" : file_compressor
    }

    request_post_binary( f"/{role}_ioblock_upload_block" , params = params , data = file_data )
    

def filepath_hash( filepath ) :
    h  = hashlib.sha256( )
    b  = bytearray( 128 * 1024 )
    mv = memoryview( b )
    with open( filepath , "rb" , buffering = 0 ) as f :
        while n := f.readinto( mv ) : h.update( mv[ :n ] )
    return( h.hexdigest( ) )

def filedata_hash( fdata ) :
    h  = hashlib.sha256( )
    h.update( fdata )
    return( h.hexdigest( ) )

def get_io_hash_filepath( h ) :
    dir_output = _config.DATA.get( "fs_storage_path" )
    file_dir = f"{dir_output}/io/{h[0:2]}/{h[2:4]}"
    os.makedirs( file_dir , exist_ok = True )
    return( f"{file_dir}/{h}" )

def save_model_tid_file( data ) :

    # FIXME TODO make this more general
    NOM_MODEL_TID = os.getenv( "NOM_MODEL_TID" , None )
    if NOM_MODEL_TID != None :
        #data = {
        #    "task_uid" : pipeline.name
        #}
        dir_output = _config.DATA.get( "fs_storage_path" )
        tid_dir = f"{dir_output}/model"
        os.makedirs( tid_dir , exist_ok = True )
        tid_fp = f"{tid_dir}/{NOM_MODEL_TID}.json"
        with open( tid_fp , "w" ) as f : f.write( json.dumps( data ) )

def load_model_tid_file( ) :

    data = { }
    # FIXME TODO make this more general
    NOM_MODEL_TID = os.getenv( "NOM_MODEL_TID" , None )
    if NOM_MODEL_TID != None :
        dir_output = _config.DATA.get( "fs_storage_path" )
        tid_dir = f"{dir_output}/model"
        tid_fp = f"{tid_dir}/{NOM_MODEL_TID}.json"
        if os.path.isfile( tid_fp ) :
            with open( tid_fp ) as f : data = json.loads( f.read( ) )

    return( data )




def validate_pipeline_submit_io( req ) :

    mport_direction = req.get( "mport_direction" , None )
    if mport_direction == None : raise Exception( f"No mport_direction" )

    port_name = req.get( "port_name" , None )
    if port_name == None : raise Exception( f"No port_name" ) 

    pin_name = req.get( "pin_name" , None )
    if pin_name == None : raise Exception( f"No pin_name" ) 

    port_ordinal = req.get( "port_ordinal" , None )
    if port_ordinal == None : raise Exception( f"No port_ordinal" ) 

    pin_ordinal = req.get( "pin_ordinal" , None )
    if pin_ordinal == None : raise Exception( f"No pin_ordinal" ) 

    fsize = req.get( "size" , None )
    if fsize == None : raise Exception( f"No fsize" ) 

    dtype = req.get( "type" , None )
    if dtype == None : raise Exception( f"No dtype" ) 

    fhash = req.get( "hash" , None )
    if fhash == None : raise Exception( f"No fhash" ) 

    current_role_name = req.get( "current_role_name" , "" )
    if current_role_name not in [ "user" , "model" , "orchestrator" ] : raise Exception( f"invalid current_role_name" ) 

####

email_check_pattern = re.compile( r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' )
def email_check( email ) :
    res = email_check_pattern.findall( email )
    return( len( res ) == 1 )

