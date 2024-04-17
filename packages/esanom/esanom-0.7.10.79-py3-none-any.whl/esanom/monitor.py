
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
from esanom import client as _nc , database as _database , config as _config , util as _util

#####################################################################

tick_last = 0
def tick( ) :
    
    global tick_last
    if ( time.time( ) - tick_last ) < 60 : return
    tick_last = time.time( )

    print( "MONITOR" )
    psutil_tick( )

####################################################################

psutil_tick_last = 0
def psutil_tick( ) :
    
    global psutil_tick_last
    if time.time( ) < psutil_tick_last : return

    ####

    psutil_status = _util.psutil_status( )
    #_util.print_debug(psutil_status)

    if psutil_status[ "partition_percent_max" ] > 75.0 :

        # FIXME TODO we cant have this outside since database may not be ready
        api_row = _database.db_query_select_row( "SELECT * from `api` where `name`=%s" , [ "_admin_system_user" ] )
        if api_row is None : return
        if api_row is not None : 
            _config.DATA[ "server_endpoint" ] = "http://127.0.0.1:13031/v3/api"
            _config.DATA[ "server_token" ] = api_row[ "token" ]


        ####

        pipeline = _nc.user_pipeline( f"monitor {time.time()}" )

        ####
        if "email" not in pipeline.io_info :
            print( "MONITOR/psutil_tick no email" )
            return
        ####

        pipeline.add( "email" , "m0" )
        pipeline.io( "/m0/inputs/email:port/1/email:subject/1" , "NoM/monitor/psutil_tick/partition_percent_max" )
        pipeline.io( "/m0/inputs/email:port/1/email:message/1" , f"{psutil_status['partition_percent_max']=}" )
        _nc.user_pipeline_submit( pipeline )

        ####

        psutil_tick_last = time.time( ) + 3600


