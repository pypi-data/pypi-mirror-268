
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
from esanom import orchestrator as _no , scheduler as _ns , monitor as _mon , database as _database

#####################################################################

_database.wait_until_ready( ) 

while True :
    print( f"{time.time()},ENGINE" )
    _no.tick( )
    _ns.tick( )
    _mon.tick( )
    time.sleep( 10 )
