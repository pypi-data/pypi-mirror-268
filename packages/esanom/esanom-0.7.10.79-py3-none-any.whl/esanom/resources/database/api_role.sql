
/*
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
*/

CREATE TABLE `api_role` (

    `id` int NOT NULL AUTO_INCREMENT,

    `api_id` int UNSIGNED DEFAULT NULL,
    `role_id` int UNSIGNED DEFAULT NULL,

    PRIMARY KEY (`id`),

    KEY `api_id` (`api_id`),
    KEY `role_id` (`role_id`),

    CONSTRAINT `api_role_ibfk_1` FOREIGN KEY (`api_id`) REFERENCES `api` (`id`) ON DELETE CASCADE,
    CONSTRAINT `api_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE CASCADE,
    
    CONSTRAINT `api_role_unique` UNIQUE ( `api_id` )

) ENGINE=InnoDB,AUTO_INCREMENT=101;
