
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

import random
import json

from esanom import database as _database 

####


def tick( ) :

    try :
        process_tasks( )
        update_db_system( )
    except Exception as e :
        print( f"EXCEPTION: {e}" )
    #process_claims( )

####


def process_claims( ) :
    claim_rows = _database.db_query_select_rows( "SELECT * from claim;" )

    # Have we processed before?
    flag_already_claimed_global = False
    for claim_row in claim_rows :
        if claim_row[ "status" ] != "YES" : continue
        _database.db_query_delete( "TRUNCATE TABLE claim;" )
        flag_already_claimed_global = True
        break

    ####

    # TASKS which are still scheduled (not taken)
    if flag_already_claimed_global :
        for claim_row in claim_rows :
            if claim_row[ "status" ] != "YES" : continue
            task_uid = claim_row[ "task_uid" ]

            # FIXME TODO in one sql query?
            task_row = _database.db_query_select_row( "SELECT * from task WHERE uid=%s AND status=%s LIMIT 1;" , [ task_uid , "SCHEDULED" ] )
            if task_row != None :
                _database.update_fromdict( "task" , task_row[ "id" ] , { "status" : "PENDING" } )

        return

    ####

    task_claim = { }

    # init
    for claim_row in claim_rows : task_claim[claim_row[ "task_uid" ] ] = [ ]

    # Fill
    for claim_row in claim_rows : task_claim[ claim_row[ "task_uid" ] ].append( claim_row[ "uid" ] )


    for i , ( task_uid , claim_uids ) in enumerate( task_claim.items( ) ) :
        claim_uid = random.choice( claim_uids )
        print(claim_uid)
        pipeline_status_scheduled( task_uid )
        _database.db_query_update( "UPDATE task SET status=%s WHERE uid=%s LIMIT 1;" , [ "SCHEDULED" , task_uid ] )
        _database.db_query_update( "UPDATE claim SET status=%s WHERE uid=%s LIMIT 1;" , [ "YES" , claim_uid ] )



def pipeline_status_scheduled( task_uid ) :

    task_row = _database.db_query_select_row( "SELECT * from task WHERE uid=%s AND status=%s LIMIT 1;" , [ task_uid , "PENDING" ] )
    if task_row == None : return


    pipeline_task_row = _database.db_query_select_row( "SELECT * from pipeline_task WHERE task_id=%s OR next_task_id=%s LIMIT 1" , [ task_row[ "id" ] , task_row[ "id" ] ] )
    if pipeline_task_row == None : return

    pipeline_row = _database.db_query_select_row( "SELECT * from pipeline WHERE id=%s LIMIT 1" , [ pipeline_task_row[ "pipeline_id" ] ] )
    if pipeline_row == None : return

    # Is pipeline scheduled (first task to be running) or not running?
    if pipeline_row[ "status" ] == "PENDING" :
        _database.update_fromdict( "pipeline" , pipeline_row[ "id" ] , { "status" : "SCHEDULED" } )

def process_tasks( ) :

    latest_schedule_row = _database.db_query_select_row( "SELECT * from schedule ORDER BY id DESC LIMIT 1" )

    ####

    if latest_schedule_row == None :
        process_claims( )
        schedule_init( )
        return

    ####

    cats = round( time.time( ) - latest_schedule_row[ "created_at" ].timestamp( ) )

    if cats < 10 : return

    _database.db_query_delete( "TRUNCATE TABLE schedule;" )

    process_claims( )
    schedule_init( )

    print( f"scheduler: OK" )


def schedule_init( ) :

    pending_task_rows = _database.db_query_select_rows( "SELECT * from task WHERE status=%s LIMIT 5" , [ "PENDING" ] )

    pending_task_rows_len = len( pending_task_rows )

    ####
    if pending_task_rows_len == 0 :
        #print( "scheduler: process_schedule pending_task_rows_len 0 SKIP" )
        return
    print( f"scheduler: process_schedule {pending_task_rows_len=}" )
    ####

    data = { }

    ####

    for task_row in pending_task_rows : data[ task_row[ "rolemodel_id" ] ] = { }

    ####

    for task_row in pending_task_rows :

        data[ task_row[ "rolemodel_id" ] ][ task_row[ "uid" ] ] = {
            "k1" : "v1"
        }

    #### 

    for i , ( k , v ) in enumerate( data.items( ) ) :

        row_data = { "rolemodel_id" : k , "data" : json.dumps( v ) }
        _database.insert_fromdict( "schedule" , row_data )

####

def update_db_system( ) :
    sql = f"update `system` set val_int=%s where `key`=%s limit 1"
    _database.db_query_update( sql , [ round( time.time( ) ) , "scheduler/time" ] )  

