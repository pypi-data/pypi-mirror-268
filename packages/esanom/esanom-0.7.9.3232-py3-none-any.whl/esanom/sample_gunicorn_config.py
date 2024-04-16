
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
import multiprocessing

# FIXME TODO should all come from config?

#_scale_processes = 0.5
#_scale_threads = 0.5
_scale_processes = 2
_scale_threads = 10

workers = int( os.environ.get( "GUNICORN_PROCESSES" , multiprocessing.cpu_count( ) * _scale_processes + 1 ) )
threads = int( os.environ.get( "GUNICORN_THREADS" , multiprocessing.cpu_count( ) * _scale_threads + 1 ) )

# FIXME TODO should come from config
timeout = int( os.environ.get( "GUNICORN_TIMEOUT" , "30" ) )

# FIXME TODO port should come from config
bind = os.environ.get( "GUNICORN_BIND" , "0.0.0.0:13031" )

# FIXME TODO should all come from config
loglevel = "info"
accesslog = "/local_data/container/access.log"
acceslogformat = "%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"
errorlog = "/local_data/container/error.log"
pidfile = "/local_data/container/gunicorn.pid"

preload_app = True

forwarded_allow_ips = '*'

