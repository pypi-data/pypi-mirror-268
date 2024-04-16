
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

__version__ = "0.7.9"

#####################################################################

from importlib.metadata import version

print( f"NoM v{version('esanom')} Copyright 2024 © European Space Agency. All rights reserved." )

#####################################################################

from esanom import config as _config 

#####################################################################

_config.init( ) 

#####################################################################

def zversion( ) :
    return( __version__ )

#####################################################################


