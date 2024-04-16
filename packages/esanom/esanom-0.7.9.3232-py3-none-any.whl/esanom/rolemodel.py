
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

import time
import os
import json
from multiprocessing import Process
import signal
import random
import atexit
from esanom import util as _util , pipeline as _pipeline

def state( ) :

    return( _util.request_get( "/model_state" ) )


def specs( specs_in ) :

    res = _util.request_post( "/model_specs" , data = specs_in )
    return( isinstance( res , dict ) )

def model_pipeline( ) :

    model_schedule_messages = _util.request_get( "/model_schedule" )
    #print(model_schedule_messages)

    if not "schedule_data_json" in model_schedule_messages :
        raise Exception( "not schedule_data_json in messages" )

    schedule_data = json.loads( model_schedule_messages[ "schedule_data_json" ] )

    task_uids = list( schedule_data.keys( ) )

    if len( task_uids ) == 0 : raise Exception( "no schedule data" )

    random.shuffle( task_uids )

    task_uid = task_uids[ 0 ]

    ####
    model_claim_set_messages = _util.request_post( "/model_claim_set" , params = { "task_uid" : task_uid } )
    #_util.print_debug( model_claim_set_messages )
    if model_claim_set_messages[ "claim_status" ] == "NO" : raise Exception( "claim_status NO" )
    ####

    claim_uid = model_claim_set_messages[ "claim_uid" ]
    for i in range( 6 ) :
        time.sleep( 5 )
        model_claim_get_messages = _util.request_post( "/model_claim_get" , params = { "claim_uid" : claim_uid } )
        _util.print_debug( model_claim_get_messages )
        if model_claim_get_messages[ "claim_status" ] == "NO" : raise Exception( "claim_status NO" )
        if model_claim_get_messages[ "claim_status" ] == "YES" : break
        print(f"model_pipeline model_claim_get WAIT {i}/15")

    if model_claim_get_messages[ "claim_status" ] != "YES" :
        _util.request_post( "/model_claim_release" , params = { "claim_uid" : claim_uid } )
        raise Exception( "claim_status NO... Claim released." )

    ####

    if not "pipeline" in model_claim_get_messages : raise Exception( "no pipeline in model_claim_get_messages" )

    pipeline = _util.object_decode( model_claim_get_messages[ "pipeline" ] )
    if not isinstance( pipeline , _pipeline.Pipeline) : raise Exception( "not Pipeline object" )

    ####


    #def exit_handler( ) :
    #    print("exit_handler")
    #    _nc.model_pipeline_failed( pipeline )

    atexit.register( lambda : pipeline_failed( pipeline , 255 ) )

    heartbeat_process = Process( target = task_heartbeat , daemon = True , args = [ os.getpid( ) , task_uid ] )
    heartbeat_process.start( )

    ####

    return( pipeline )


def pipeline_failed( pipeline , exit_code ) :

    # Check if pipeline has been completed - mainly for short curcuiting atexit
    if pipeline.status == "COMPLETED" : return

    task_uid = pipeline.task_uid

    _util.request_post( "/model_pipeline_failed" , params = { "task_uid" : task_uid , "exit_code" : exit_code } )


def task_heartbeat( pid , task_uid ) :

    while True :

        time.sleep( 5 )

        print( f"task_heartbeat {pid} {task_uid}" )

        try :
            messages = _util.request_post( "/model_task_heartbeat" , params = { "task_uid" : task_uid } )
            if messages.get( "pipeline_status" , None ) == "CANCELLED" :
                print( messages )
                os.kill( pid , signal.SIGTERM )
                return

        except Exception as e :
            print( f"{e}" )
            continue






