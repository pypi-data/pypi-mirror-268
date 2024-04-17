
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

CREATE TABLE `mport` (

    `id` int UNSIGNED NOT NULL AUTO_INCREMENT,

    `rolemodel_id` INT UNSIGNED DEFAULT NULL,
    `port_id` INT UNSIGNED DEFAULT NULL,

    `size_max` INT UNSIGNED DEFAULT 0,

    `direction` varchar(16) NOT NULL,

    `enable` BOOLEAN DEFAULT 1,
    `cardinal` INT UNSIGNED DEFAULT 1,
    `visible` BOOLEAN DEFAULT 1,
    `pipeline` BOOLEAN DEFAULT 1,
    `download` BOOLEAN DEFAULT 1,
    `read` BOOLEAN DEFAULT 1,
    `write` BOOLEAN DEFAULT 1,

    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,

    PRIMARY KEY (`id`) ,
    
    KEY `rolemodel_id` (`rolemodel_id`),
    KEY `port_id` (`port_id`),
    KEY `direction` (`direction`),
    KEY `enable` (`enable`),
    
    CONSTRAINT `mport_rolemodel_id` FOREIGN KEY (`rolemodel_id`) REFERENCES `rolemodel` (`id`) ON DELETE CASCADE ,
    CONSTRAINT `mport_port_id` FOREIGN KEY (`port_id`) REFERENCES `port` (`id`) ON DELETE CASCADE ,

    CONSTRAINT `mport_unique_rolemodelportdirection` UNIQUE (`rolemodel_id`,`port_id`,`direction`)

) ENGINE=InnoDB,AUTO_INCREMENT=101;
 




