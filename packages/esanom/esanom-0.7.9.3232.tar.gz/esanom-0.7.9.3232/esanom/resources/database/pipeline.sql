
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

CREATE TABLE `pipeline` (

    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,

    `status` varchar(255) DEFAULT "RESERVED" ,
    
    `uid` varchar(255) NOT NULL CHECK (`uid` <> ""),
    
    `roleuser_id` INT UNSIGNED DEFAULT NULL,

    `name` varchar(255) NOT NULL CHECK (`name` <> "") ,

    `status_code` INT UNSIGNED DEFAULT 0,

    `done` BOOLEAN DEFAULT 0,

    `archived` BOOLEAN DEFAULT 0,

    `entered_state_at` DATETIME DEFAULT NULL,
    
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,

    `accessed_at` DATETIME DEFAULT NULL,
    `retrieved_at` DATETIME DEFAULT NULL ,
    `archived_at` DATETIME DEFAULT NULL ,
    
    PRIMARY KEY (`id`) ,

    UNIQUE KEY `uid` (`uid`) ,
    
    KEY `roleuser_id` (`roleuser_id`),
    KEY `status` (`status`) ,
    KEY `archived` (`archived`) ,
    KEY `name` (`name`) ,

    CONSTRAINT `pipeline_roleuser_id` FOREIGN KEY (`roleuser_id`) REFERENCES `roleuser` (`id`) ON DELETE CASCADE 


) ENGINE=InnoDB,AUTO_INCREMENT=101;
