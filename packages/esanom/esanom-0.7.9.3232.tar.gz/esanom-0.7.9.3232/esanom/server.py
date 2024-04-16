
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

from flask import Flask , redirect , url_for
from flask_compress import Compress
from werkzeug.middleware.proxy_fix import ProxyFix
import logging
from . import config as _config , database as _database

#####################################################################

_database.init( )

#####################################################################

app = Flask( __name__ )

#####################################################################

app.wsgi_app = ProxyFix( app.wsgi_app , x_for = 1 , x_host = 1 , x_port = 1 , x_proto = 1 , x_prefix = 1 )
Compress( app )

#####################################################################

app.config[ "SEND_FILE_MAX_AGE_DEFAULT" ] = 31622400
app.config[ "MAX_CONTENT_LENGTH" ] = 16 * 1024 * 1024

#####################################################################

from esanom.routes.v3.api import ROUTES as routes_v3_api
app.register_blueprint( routes_v3_api , name = "routes_v3_api" , url_prefix = "/v3/api" )

from esanom.routes.v3.web import ROUTES as routes_v3_web
app.register_blueprint( routes_v3_web , name = "routes_v3_web" , url_prefix = "/v3/web" )

#####################################################################

@app.route( "/" )
def index( ) :
    return redirect( url_for( "routes_v3_web.page_index" ) )

@app.errorhandler( 404 )
def error_404( e ):
    return redirect( url_for( "routes_v3_web.page_error_404" ) )

@app.errorhandler( 500 )
def error_500( e ):
    return redirect( url_for( "routes_v3_web.page_error_500" ) )

#####################################################################

#_config.DATA[ "fs_storage_path" ] = _config.DATA[ "fs_storage_path" ] + "/server"

#####################################################################

if __name__ == "__main__" :

    app.run( host = "0.0.0.0" , port = 13031 , debug = _config.DATA[ "server_debug" ] )
    #app.run( host = "0.0.0.0" , port = 13031 , debug = False )

else :

    gunicorn_logger = logging.getLogger( "gunicorn.error" )
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel( gunicorn_logger.level )

