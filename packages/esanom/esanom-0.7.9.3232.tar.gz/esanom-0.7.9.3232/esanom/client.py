
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

from . import roleadmin as _roleadmin , rolemodel as _rolemodel , roleuser as _roleuser , config as _config , util as _util

####

#_config.DATA[ "fs_storage_path" ] = _config.DATA[ "fs_storage_path" ] + "/client"

####

def exit( msg = None ) :
    if msg is not None : print( msg )
    sys.exit( )

def load_json( fp_json ) :
    with open( fp_json ) as f :
        return( json.loads( f.read( ) ) )

def get_uid( ) :
    return( _util.get_test_uid( ) )

def admin_state( ) :

    return( _roleadmin.state( ) )

def admin_state_table( table = None ) :

    return( _roleadmin.state_table( table ) )

def admin_state_table_row( table = None , row_id = None ) :

    return( _roleadmin.state_table_row( table , row_id ) )

def admin_create( table , data ) :

    return( _roleadmin.create( table , data ) )

def admin_create_bulk( table , data ) :

    return( _roleadmin.create_bulk( table , data ) )

def admin_update( table , data , row_id ) :

    return( _roleadmin.update( table , data, row_id ) )

def admin_delete( table , row_id ) :

    return( _roleadmin.delete( table , row_id ) )

def admin_create_user( options ) :

    return( _roleadmin.create_user( options ) )


def admin_create_api_with_rolegroup( options ) :

    return( _roleadmin.create_api_with_rolegroup( options ) )

def admin_create_model( options ) :

    return( _roleadmin.create_model( options ) )

def admin_delete_testdata( table , k = "name" , v = "test_" ) :

    if len( v.strip( ) ) < 2 : return

    bulk_rows = [ ]

    rows = admin_state_table( table )
    for row in rows :
        if row[ k ].startswith( v ) :
            bulk_rows.append( row[ "id" ] )

    if len( bulk_rows ) > 0 : 
        _roleadmin.delete_bulk( table , bulk_rows )

def admin_model_enable( api_token ) :
    return( _roleadmin.model_enable( api_token ) )

def admin_model_updateable( api_token ) :
    return( _roleadmin.model_updateable( api_token ) )

def admin_group_flush( api_id ) :
    return( _roleadmin.group_flush( api_id ) )

def admin_sample_data( ) :
    return( _roleadmin.sample_data( ) )

####


def model_state( ) :

    return( _rolemodel.state( ) )


def model_specs( specs_in = None ) :

    if specs_in is not None : return( _rolemodel.specs( specs_in ) )

    ####

    specs_fp = "nom_model_specs.json"

    if not os.path.isfile( specs_fp ) : raise Exception( f"Specs file [{specs_fp}] not found" )

    with open( specs_fp ) as f : specs = json.loads( f.read( ) )

    return( _rolemodel.specs( specs ) )



def model_pipeline( ) :
    return( _rolemodel.model_pipeline( ) )


def model_pipeline_submit( pipeline ) :

    task_uid = pipeline.task_uid

    ####

    for i , ( k , v ) in enumerate( pipeline.io_data.items( ) ) :

        if k.startswith( "_" ) : continue
        if "io" in v : continue

        messages = _util.request_post( "/model_pipeline_submit_io" , params = { "task_uid" : task_uid } , data = v )
        if not "io_uid" in messages : raise Exception( "io_uid not found" )

        #print( v )

        _util.ioblock_upload( v , messages[ "io_uid" ] , "model" ) 

    ####

    _util.request_post( "/model_pipeline_submit" , params = { "task_uid" : task_uid } )

    pipeline.status = "COMPLETED"

    

def model_pipeline_failed( pipeline , exit_code = 254 ) :

    _roleadmin.pipeline_failed( pipeline , exit_code )


####

def user_state( ) :

    return( _roleuser.state( ) )


def user_pipeline( in_pipeline_name = None ) :

    pipeline_name = in_pipeline_name

    if pipeline_name == None : pipeline_name = _util.get_test_uid( prefix = "pipeline" )
    
    if pipeline_name.strip( ) == "" : raise Exception( f"ERROR pipeline_name" )

    return( _roleuser.pipeline( pipeline_name ) )

def user_pipeline_submit( pipeline ) :

    if pipeline.submitted : raise Exception( "Already submitted" )

    user_pipeline_submit_reserve_messages = _roleuser.pipeline_submit_reserve( pipeline )

    print( user_pipeline_submit_reserve_messages )

    task_uids = user_pipeline_submit_reserve_messages[ "task_uids" ]

    pipeline_io_uids = _roleuser.pipeline_submit_io( pipeline , task_uids )

    print(f"{pipeline_io_uids=}")

    _roleuser.pipeline_submit_io_blocks( pipeline , pipeline_io_uids )

    _roleuser.pipeline_submit( pipeline )

    pipeline.submitted = True

    #pipeline_uid = messages[ "pipeline_uid" ]
    #print( f"pipeline_uid {pipeline_uid}")
    #messages = _roleuser.pipeline_submit_io( pipeline_uid )
    #print(messages)

    return( True )

def user_pipeline_await( pipeline ) :

    pipeline_name = pipeline.name
    t0=time.time()

    while not pipeline.done :
        dt=int(time.time()-t0)
        print( f"[{dt}] awaiting {pipeline_name}")
        time.sleep(1)
        pipeline = user_pipeline( pipeline_name )

    return( pipeline )


def user_pipeline_archive( pipeline_name ) :

    return( _roleuser.pipeline_archive( pipeline_name ) )


def user_pipeline_cancel( pipeline_name ) :

    return( _roleuser.pipeline_cancel( pipeline_name ) )

def user_sample_workload( ) :

    pipeline = user_pipeline( f"sample_workload {time.time()}" )

    pipeline.add( "test_model0" , "m0" )

    for i in range( 1 , 10 ) :
        pipeline.add( f"test_model0" , f"m{i}" )
        pipeline.connect( f"m{i}" , "m0" )
        pipeline.io( f"/m{i}/inputs/test_model0:p1/0/test_model0:q1/0" , f"M{i}_{time.time()}" )

    user_pipeline_submit( pipeline )


