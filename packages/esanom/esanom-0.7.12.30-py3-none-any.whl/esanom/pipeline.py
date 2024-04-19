
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
import networkx 
from datetime import date, timezone
from cbor2 import dumps , load
from hashlib import sha256
import copy
from esanom import util as _util 
import zstandard

class Pipeline :

    def __init__( self , name = "" , edges_in = [ ] ) :

        self.uid = ""

        self.name = name
        self.current_role_name = ""

        self.nodes = { }

        self.io_info = { }
        self.io_data = { } 

        #self.io_metadata = { }

        self.status = ""
        self.done = 0
        self.archived = 0

        self.graph = networkx.DiGraph( [ tuple( i ) for i in edges_in ] )

        self.submitted = False


    def print_debug( self ) :

        _util.print_debug( self.io_info , "pipeline.io_info" )
        _util.print_debug( self.io_data , "pipeline.io_data" )

        _util.print_debug( self.nodes , "pipeline.nodes" )

        _util.print_debug( list( self.graph.edges ) , "graph.edges" )
        _util.print_debug( list( self.graph.nodes ) , "graph.nodes" )
        
        _util.print_debug( self.status , "pipeline.status" )
        _util.print_debug( self.current_role_name , "pipeline.current_role_name" )
        _util.print_debug( self.name , "pipeline.name" )

    def add( self , node_name , node_alt_name = None ) :

        # FIXME TODO cache this
        nodes_available = list( self.io_info.keys( ) )

        if not node_name in nodes_available : raise Exception( f"{node_name} not available")

        node_key = node_name

        if node_alt_name != None : node_key = node_alt_name

        if node_key in self.nodes : raise Exception( f"{node_key} node already added" )

        self.nodes[ node_key ] = { "name" : node_name }

    def connect( self , node1 , node2 ) :
        nodes_keys = list( self.nodes.keys( ) )

        if node1.strip( ) == node2.strip( ) : raise Exception( f"cannot connect {node1=} {node2=} the same")

        if not node1 in nodes_keys : raise Exception( f"{node1=} not found")
        if not node2 in nodes_keys : raise Exception( f"{node2=} not found")

        self.graph.add_edges_from( [ ( node1 , node2 ) ] )

    def get_node_names( self ) :
        return( list( self.nodes.keys( ) ) ) 

    def get_node_graph_names( self ) :
        ln = list( self.graph.nodes )
        return( ln )

    def get_standalone_nodes( self ) :

        node_names = self.get_node_names( )
        get_node_graph_names = self.get_node_graph_names( )
        node_diffs = list( set( node_names ) - set( get_node_graph_names ) )
        
        return( node_diffs )



    def edges( self ) :
        return( list( self.graph.edges ) )

    def topological_sort( self ) :
        return( list( networkx.topological_sort( self.graph ) ) )

    def topological_sort_edges( self ) :
        return( list( networkx.topological_sort( networkx.line_graph( self.graph ) ) ) )

    def predecessors( self , n ) :
        return( list( self.graph.predecessors( n ) ) )

    def descendants( self , n ) :
        return( list( networkx.descendants( self.graph , n ) ) )


    def iokey_parts( self , cmd_key ) :
        cmd_key_parts = cmd_key.split( "/" )
        if cmd_key_parts[ 0 ] != "" : raise Exception( f"io: must start with /" )
        cmd_key_parts.pop( 0 )
        if len( cmd_key_parts ) != 6 : raise Exception( f"io: wrong number of parts" )
        return( cmd_key_parts )

        ####

        model_name_alt , direction , port_name , port_ordinal_str , pin_name , pin_ordinal_str = cmd_key_parts

    def io( self , cmd_key , cmd_val = None ) :

        model_name_alt , direction , port_name , port_ordinal_str , pin_name , pin_ordinal_str = self.iokey_parts( cmd_key )

        #print(model_name_alt , direction , port_name , port_ordinal_str , pin_name , pin_ordinal_str)
        #raise Exception( f"io: testing" )

        ####

        #print(self.io_info)

        if not port_ordinal_str.isdigit( ) : raise Exception( f"io: invalid port ordinal {direction} {port_ordinal_str}" )
        port_ordinal = int( float( port_ordinal_str ) )

        if not pin_ordinal_str.isdigit( ) : raise Exception( f"io: invalid pin ordinal {direction} {pin_ordinal_str}" )
        pin_ordinal = int( float( pin_ordinal_str ) )
        
        #print(f"{port_name=} {port_ordinal=} {pin_name=} {pin_ordinal=}")

        ####

        if model_name_alt != "_" :

            if not model_name_alt in self.nodes : raise Exception( f"io: {model_name_alt} not found" )
            if not self.nodes[ model_name_alt ][ "name" ] in self.io_info : raise Exception( f"io: {model_name_alt}/name not found in pipeline.io_info" )

            model_name = self.nodes[ model_name_alt ][ "name" ]

        else :
            model_name = model_name_alt

        ####

        if not direction in self.io_info[ model_name ] : raise Exception( f"io: invalid direction {direction}" )

        ####

        flag_found = False

        for io_port in self.io_info[ model_name ][ direction ] :

            if io_port[ "name" ] == port_name :

                if io_port[ "cardinal" ] > 0 :
                    if port_ordinal > io_port[ "cardinal" ] : raise Exception( f"io: port {port_name} ordinal {port_ordinal}" )

                if not "pins" in io_port : raise Exception( f"io: no pins for port {port_name}" )

                for q in io_port[ "pins" ] :
                    if q[ "name" ] == pin_name :
                        if q[ "cardinal" ] == 0 : flag_found = True
                        if pin_ordinal <= q[ "cardinal" ] : flag_found = True
                        
        if not flag_found : raise Exception( f"io: invalid port/pin {port_name}/{port_ordinal}/{pin_name}/{pin_ordinal}" )

        ####

        # Don't stuff with other key vals! Must match api structure
        dinfo = {
            "mport_direction" : direction ,
            "port_name" : port_name ,
            "port_ordinal" : port_ordinal ,
            "pin_name" : pin_name ,
            "pin_ordinal" : pin_ordinal 
        }

        ####

        if cmd_val is not None :
            self.io_set( dinfo , cmd_val , model_name_alt = model_name_alt )
        else : 
            return( self.io_get( dinfo , model_name_alt = model_name_alt ) )


    def io_set( self , dinfo , cmd_val , model_name_alt ) :

        ####
        #self.print_debug()
        #print(dinfo)
        #{'mport_direction': 'outputs', 'port_name': 'test_rebound:files', 'port_ordinal': 0, 'pin_name': 'test_rebound:orbit', 'pin_ordinal': 0}

        rolemodel_name = self.nodes[ model_name_alt ][ "name" ]

        pin_type = None
        ports = self.io_info[rolemodel_name][dinfo["mport_direction"]]
        for port in ports :
            if port["name"]==dinfo["port_name"] :
                for pin in port["pins"] :
                    if pin["name"]==dinfo["pin_name"]:
                        pin_type=pin["type"]

        if pin_type == None : raise Exception( f"pin_type None" )

        ####

        is_file = pin_type.startswith( "." )


        if is_file :
            _root , dtype = os.path.splitext( cmd_val )
        else :
            dtype = type( cmd_val ).__name__ 

        if dtype != pin_type : raise Exception( f"Not matching {pin_type=} {dtype=}" )

        ####

        if not is_file :

            if dtype=="datetime" :
                file_data = dumps( cmd_val , timezone = timezone.utc , date_as_datetime = True )
            else :
                file_data = dumps( cmd_val )

            file_hash = sha256( file_data ).hexdigest( ) 

            file_path = _util.get_io_hash_filepath( file_hash )

            #print(file_path)

            with open( f"{file_path}" , "wb" ) as f : f.write( file_data )

        else :

            file_path = cmd_val
            if not os.path.isfile( file_path ) : raise Exception( f"io: not file_path {file_path}" )
            file_hash = _util.filepath_hash( file_path )

        ####

        file_size = os.path.getsize( file_path )

        ####

        cmd_key = f"/{model_name_alt}/{dinfo['mport_direction']}/{dinfo['port_name']}/{dinfo['port_ordinal']}/{dinfo['pin_name']}/{dinfo['pin_ordinal']}"
        #print(cmd_key)

        self.io_data[ cmd_key ] = dinfo | {
            "file_path" : file_path ,
            "current_role_name" : self.current_role_name ,
            "type" : dtype ,
            "size" : file_size ,
            "hash" : file_hash
        }

        #print(self.io_data[ cmd_key ] )

    def io_get( self , dinfo , model_name_alt ) :

        #print(dinfo)

        io_dinfo = self.get_io_dinfo( dinfo , model_name_alt )
        #print(io_dinfo["io_uid"])

        #print(io_dinfo)

        io_uid = io_dinfo[ "io" ][ "io_uid" ] 
        ioblock_rows = io_dinfo[ "io" ][ "ioblock_rows" ]
        #print(ioblock_rows)

        if len( ioblock_rows ) != io_dinfo[ "io" ][ "io_blocks" ] : raise Exception( f"Not enough ioblock_rows..?" )

        fp_raw = _util.get_io_hash_filepath( io_dinfo[ "hash" ] )

        with open( fp_raw , "wb" ) as f :

            for ioblock_row in ioblock_rows :

                params = {
                    "io_uid" : io_uid ,
                    "ioblock_block" : ioblock_row[ "block" ]
                }

                #content =_util.request_get_file( "/model_ioblock" , params = params )
                content = _util.request_get_file( f"/{self.current_role_name}_ioblock" , params = params )

                #print(content)

                if len( content ) != ioblock_row[ "size" ] : raise Exception( f"io_input: len content mismatch {len(content)} {ioblock_row['size']}" )

                if _util.filedata_hash( content ) != ioblock_row[ "hash" ] : raise Exception( f"io_input: hash mismatch" )

                if ioblock_row[ "compressor" ] == "ZSTD" :
                    cctx = zstandard.ZstdDecompressor( )
                    content = cctx.decompress( content ) 

                f.write( content )

        ####

        if io_dinfo[ "type" ].startswith( "." ) :
            fp_new = fp_raw + io_dinfo[ "type" ]
            os.rename( fp_raw , fp_new )

            return( fp_new )

        ####

        if not os.path.isfile( fp_raw ) : raise Exception( f"Not found {fp_raw}" )

        with open( fp_raw , "rb" ) as fp : obj = load( fp )

        if type( obj ).__name__ != io_dinfo[ "type" ] : raise Exception( f"io_input: bad type" )

        #print(obj)

        return( obj )


    ####

    def io_wire( self , cmd_key1 , cmd_key2 ) :

        #print(f"{cmd_key1} -> {cmd_key2}")
        # self.io_wire( "/m1/outputs/_test_model0:portA/0/_test_model0:pinA1/0" , node )

        if not cmd_key1 in self.io_data : raise Exception( f"Not found {cmd_key1}")
        if cmd_key2 in self.io_data : raise Exception( f"Found {cmd_key2}")

        ####

        io = copy.deepcopy( self.io_data[ cmd_key1 ] )
        #print( io )
        model_name_alt , direction , port_name , port_ordinal_str , pin_name , pin_ordinal_str = self.iokey_parts( cmd_key2 )
        
        if not port_ordinal_str.isdigit( ) : raise Exception( f"io_wire: invalid port ordinal {direction} {port_ordinal_str}" )
        port_ordinal = int( float( port_ordinal_str ) )

        io[ "current_role_name" ] = self.current_role_name
        io[ "mport_direction" ] = direction
        io[ "rolemodel_name_alt" ] = model_name_alt
        io[ "port_ordinal" ] = port_ordinal

        #print(io)

        self.io_data[ cmd_key2 ] = io

        #print(f"{self.io_data=}")

    ####

    def get_io_dinfo( self , dinfo , rolemodel_name_alt ) :

        #print( dinfo )
        #print(self.io_metadata)

        #for i2 , ( k2 , v2 ) in enumerate( self.io_metadata.items( ) ) :
        for i2 , ( k2 , v2 ) in enumerate( self.io_data.items( ) ) :

            flag = True

            if v2[ "rolemodel_name_alt" ] != rolemodel_name_alt : continue

            for i1 , ( k1 , v1 ) in enumerate( dinfo.items( ) ) :

                if not k1 in v2 :
                    flag = False 
                    continue

                if v2[ k1 ] != v1 :
                    flag = False 
                    continue

            if flag == True : return( v2 )

        raise Exception( f"io: get_io_metadata ?" )


    def is_valid( self ) :
        return( networkx.is_directed_acyclic_graph( self.graph ) )





