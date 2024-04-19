
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

from datetime import datetime
import time

from esanom import database as _database 


####

def handle_pipeline_status_submitted( ) :

    pipeline_rows = _database.db_query_select_rows( "SELECT * from pipeline WHERE archived=0 AND status=%s" , [ "SUBMITTED" ] )
    pipeline_rows_len = len( pipeline_rows )
    if pipeline_rows_len == 0 :
        #print( "orchestrator: handle_pipeline_status_submitted 0 SKIP" )
        return

    print( f"orchestrator: handle_pipeline_status_submitted {pipeline_rows_len}" )

    ####

    pipeline_ids = [ ]

    # Loop pipelines
    for pipeline_row in pipeline_rows :

        pipeline = _database.pipeline_object( pipeline_row )

        # Handle standalone nodes SUBMITTED -> PENDING
        nodes = pipeline.get_standalone_nodes( )
        print( f"{nodes=}" )

        for node in nodes :

            if pipeline.nodes[ node ][ "task_status" ] != "SUBMITTED" : continue 

            task_uid = pipeline.nodes[ node ][ "task_uid" ]

            _database.handle_overrides( task_uid )

            sql = f"update `task` set status=%s where uid=%s limit 1"
            _database.db_query_update( sql , [ "PENDING" , task_uid ] )

            pipeline.nodes[ node ][ "task_status" ] = "PENDING"
        #

        # Handle graph nodes with no preds
        nodes = pipeline.get_node_graph_names( )
        print( f"{nodes=}" )

        for node in nodes :

            if pipeline.nodes[ node ][ "task_status" ] != "SUBMITTED" : continue 

            if len( pipeline.predecessors( node ) ) > 0 : continue

            task_uid = pipeline.nodes[ node ][ "task_uid" ]

            _database.handle_overrides( task_uid )

            sql = f"update `task` set status=%s where uid=%s limit 1"
            _database.db_query_update( sql , [ "PENDING" , task_uid ] )

            pipeline.nodes[ node ][ "task_status" ] = "PENDING"
        #

        ####

        pipeline_ids.append( pipeline_row[ "id" ] )
        print( f"PIPELINE SUBMITTED {pipeline_row['name']} -> PENDING" )
    #

    if len( pipeline_ids ) > 0 : _database.pipeline_bulk_update_status( pipeline_ids , "PENDING" )

####

def handle_pipeline_status_running( ) :

    pipeline_rows = _database.db_query_select_rows( "SELECT * from pipeline WHERE archived=0 AND status=%s" , [ "RUNNING" ] )
    pipeline_rows_len = len( pipeline_rows )
    if pipeline_rows_len == 0 :
        #print( "orchestrator: handle_pipeline_status_running 0 SKIP" )
        return

    print( f"orchestrator: handle_pipeline_status_running {pipeline_rows_len}" )

    ####

    # Loop pipelines
    for pipeline_row in pipeline_rows :

        print(f"handle_pipeline_status_running {pipeline_row['name']=}")

        pipeline = _database.pipeline_object( pipeline_row )
        pipeline.current_role_name = "orchestrator"

        # Handle graph nodes with preds
        nodes = pipeline.get_node_graph_names( )
        print( f"{len(nodes)=}" )

        for node in nodes :

            print(f"{node=}")

            if pipeline.nodes[ node ][ "task_status" ] != "SUBMITTED" : continue 

            node_preds = pipeline.predecessors( node )
            if len( node_preds ) == 0 : continue
            #print(f"{node_preds=}")

            flag_preds_done = True
            flag_preds_failed = False

            for node_pred in node_preds :
                if pipeline.nodes[ node_pred ][ "task_done" ] == 0 :
                    flag_preds_done = False
                if pipeline.nodes[ node_pred ][ "task_done" ] == 1 :
                    if pipeline.nodes[ node_pred ][ "task_status" ] != "COMPLETED" :
                        flag_preds_failed = True


            ######

            if flag_preds_failed and pipeline.nodes[node][ "ignore_pred_fail" ] != 1 :

                task_uid = pipeline.nodes[ node ][ "task_uid" ]

                sql = f"update `task` set status=%s where uid=%s limit 1"
                _database.db_query_update( sql , [ "CANCELLED" , task_uid ] )

                pipeline.nodes[ node ][ "task_status" ] = "CANCELLED"
                pipeline.nodes[ node ][ "task_done" ] = 1

                continue

            ######

            # Wire up node with its preds
            if flag_preds_done :
                try :
                    handle_wiring( pipeline , node , node_preds )
                except Exception as e :
                    sql = f"update `task` set status=%s where uid=%s limit 1"
                    _database.db_query_update( sql , [ "FAILED" , pipeline.nodes[ node ][ "task_uid" ] ] )
                    pipeline.nodes[ node ][ "task_status" ] = "FAILED"
                    print(f"zzzEXCEPTION {e}")
                    continue

            # task status SUBMITTED -> PENDING
            if flag_preds_done :

                print(f"{pipeline.descendants(node)=}")

                task_uid = pipeline.nodes[ node ][ "task_uid" ]
                _database.handle_overrides( task_uid )

                sql = f"update `task` set status=%s where uid=%s limit 1"
                _database.db_query_update( sql , [ "PENDING" , task_uid ] )
                pipeline.nodes[ node ][ "task_status" ] = "PENDING"
            #

####

def handle_pipeline_status_running_completed( ) :

    pipeline_rows = _database.db_query_select_rows( "SELECT * from pipeline WHERE archived=0 AND status=%s" , [ "RUNNING" ] )
    pipeline_rows_len = len( pipeline_rows )
    if pipeline_rows_len == 0 :
        #print( "orchestrator: handle_pipeline_status_running_completed 0 SKIP" )
        return

    print( f"orchestrator: handle_pipeline_status_running_completed {pipeline_rows_len}" )

    ####

    # Loop pipelines
    for pipeline_row in pipeline_rows :

        pipeline = _database.pipeline_object( pipeline_row )

        flag_done = True

        for node in pipeline.nodes.keys( ) :
            if pipeline.nodes[ node ][ "task_done" ] == 0 : flag_done = False

        if flag_done :
            sql = f"UPDATE `pipeline` SET status=%s WHERE id=%s LIMIT 1"
            _database.db_query_update( sql , [ "COMPLETED" , pipeline_row[ "id" ] ] )

        #


###

def handle_wiring( pipeline , node , node_preds ) :

    model_name = pipeline.nodes[ node ][ "name" ]
    model_inputs = pipeline.io_info[ model_name ][ "inputs" ]

    ####

    for model_input in model_inputs :

        if not "pins" in model_input : continue

        node_port_ordinal = 1

        for model_input_pin in model_input[ "pins" ] :

            for node_pred in node_preds :


                pred_io_data_sorted = pred_io_data_rows( pipeline , model_input[ "name" ] , model_input_pin[ "name" ] , node_pred )

                if len( pred_io_data_sorted ) == 0 : continue

                ####

                for pred_io_datum in pred_io_data_sorted :

                    port_name = pred_io_datum[ "port_name" ]
                    port_ordinal = pred_io_datum[ "port_ordinal" ]
                    pin_name = pred_io_datum[ "pin_name"]
                    pin_ordinal = pred_io_datum[ "pin_ordinal" ]

                    source = f"/{node_pred}/outputs/{port_name}/{port_ordinal}/{pin_name}/{pin_ordinal}"

                    target = f"/{node}/inputs/{port_name}/{node_port_ordinal}/{pin_name}/{pin_ordinal}"

                    #pipeline.print_debug( )

                    #print( f"{node_pred}" )
                    #print( f"{source}" )
                    #print( f"{target}" )

                    handle_wiring_io( pipeline , source , target )

                    node_port_ordinal = node_port_ordinal + 1

def pred_io_data_rows( pipeline , model_input_name , model_input_pin_name , node_pred ) :

    pred_io_data = [ ]

    for i , ( k , io_datum ) in enumerate( pipeline.io_data.items( ) ) :
        if io_datum_outputs_match( io_datum , model_input_name , model_input_pin_name , node_pred ) :
            pred_io_data.append( io_datum )

    pred_io_data_sorted = sorted( pred_io_data , key = lambda d : d[ 'port_ordinal' ] )

    return( pred_io_data_sorted )


def io_datum_outputs_match( io_datum , model_input_name , model_input_pin_name , node_pred ) :
    return(
        ( io_datum[ "port_name" ] == model_input_name )
        and ( io_datum[ "pin_name" ] == model_input_pin_name )
        and ( io_datum[ "mport_direction" ] == "outputs" ) 
        and ( io_datum[ "rolemodel_name_alt" ] == node_pred )
    ) 


def handle_wiring_io( pipeline , source , target ) :

    pipeline.io_wire( source , target )

    rolemodel_name_alt = pipeline.io_data[ target ][ "rolemodel_name_alt" ]

    node_task_uid = pipeline.nodes[ rolemodel_name_alt ][ "task_uid" ]
    pred_io_uid = pipeline.io_data[ source ][ "io" ][ "io_uid" ]

    _database.io_insert( node_task_uid , pipeline.io_data[ target ] , pred_io_uid = pred_io_uid )

####

def update_db_system( ) :
    sql = f"update `system` set val_int=%s where `key`=%s limit 1"
    _database.db_query_update( sql , [ round( time.time( ) ) , "orchestrator/time" ] )  

####

def tick( ) :

    try : handle_pipeline_status_submitted( )
    except Exception as e : print( f"EXCEPTION: handle_pipeline_status_submitted {e}" )

    try : handle_pipeline_status_running( )
    except Exception as e : print( f"EXCEPTION: handle_pipeline_status_running {e}" )

    try : handle_pipeline_status_running_completed( )
    except Exception as e : print( f"EXCEPTION: handle_pipeline_status_running_completed {e}" )

    try : update_db_system( )
    except Exception as e : print( f"EXCEPTION: update_db_system {e}" )

