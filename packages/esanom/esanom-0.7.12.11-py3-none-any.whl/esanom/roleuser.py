
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

from esanom import util as _util , pipeline as _pipeline

def state( ) :

    messages = _util.request_get( "/user_state" )

    return( messages )

def pipeline( pipeline_name ) :

    messages = _util.request_post( "/user_pipeline" , params = { "name" : pipeline_name } )

    if not "pipeline" in messages : raise Exception( "no pipeline in messages" )

    obj = _util.object_decode( messages[ "pipeline" ] )
    if not isinstance( obj , _pipeline.Pipeline ) : raise Exception( "not pipeline object" )

    return( obj )


def pipeline_submit_reserve( pipeline ) :
    
    if not pipeline.is_valid( ) : raise Exception( "pipeline not valid" )

    data = {
        "nodes" : pipeline.nodes ,
        "edges" : pipeline.edges( ) 
    }

    messages = _util.request_post( "/user_pipeline_submit_reserve" , params = { "name" : pipeline.name } , data = data )

    if not "pipeline_uid" in messages : raise Exception( "pipeline_uid not found" )
    if not "task_uids" in messages : raise Exception( "task_uids not found" )

    #print( messages )

    return( messages )

def pipeline_submit( pipeline ) :
    
    _util.request_post( "/user_pipeline_submit" , params = { "name" : pipeline.name } )

    return( True )


def pipeline_submit_io( pipeline , task_uids ) :

    #_util.debug_json_print(pipeline.io_data )

    pipeline_io_uid = { }

    for i , ( k , v ) in enumerate( pipeline.io_data.items( ) ) :

        k_parts = k.split( "/" )

        #model_name_alt = v[ "model_name_alt" ]
        model_name_alt = k_parts[ 1 ]


        if not model_name_alt in task_uids : raise Exception( f"{model_name_alt} not found task_uids" )
        #task_uid = task_uids[ model_name_alt ]
        #print( f"pipeline_submit_io {model_name_alt} -> {task_uid}" )

        messages = _util.request_post( "/user_pipeline_submit_io" , params = { "task_uid" : task_uids[ model_name_alt ] } , data = v )

        if not "io_uid" in messages : raise Exception( "io_uid not found" )

        pipeline_io_uid[ k ] = messages[ "io_uid" ]

    return( pipeline_io_uid )

def pipeline_submit_io_blocks( pipeline , pipeline_io_uid ) :

    for i , ( k , v ) in enumerate( pipeline.io_data.items( ) ) :
        if not k in pipeline_io_uid : raise Exception( f"pipeline_submit_io_blocks {k} not found" )
        _util.ioblock_upload( v , pipeline_io_uid[ k ] , "user" ) 

def pipeline_archive( pipeline_name ) :
    
    _util.request_post( "/user_pipeline_archive" , params = { "name" : pipeline_name } )

    return( True )

def pipeline_cancel( pipeline_name ) :
    
    _util.request_post( "/user_pipeline_cancel" , params = { "name" : pipeline_name } )

    return( True )



