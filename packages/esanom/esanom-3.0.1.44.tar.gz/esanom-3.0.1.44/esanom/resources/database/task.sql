
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

CREATE TABLE `task` (
    
    `id` int UNSIGNED NOT NULL AUTO_INCREMENT,

    `status` varchar(255) DEFAULT "RESERVED" ,
    `uid` varchar(255) NOT NULL CHECK (`uid` <> "") ,
    
    `rolemodel_id` INT UNSIGNED DEFAULT NULL,
    `rolemodel_name_alt` varchar(255) DEFAULT NULL ,

    `status_code` INT UNSIGNED DEFAULT 0,
    `done` BOOLEAN DEFAULT 0,

    `inputs_size` INT UNSIGNED DEFAULT 0,
    `outputs_size` INT UNSIGNED DEFAULT 0,

    `exit_code` int UNSIGNED DEFAULT 0,

    `heartbeats` INT UNSIGNED DEFAULT 0,

    `scheduled_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `running_at` DATETIME DEFAULT NULL ,

    `heartbeat_at` DATETIME DEFAULT NULL ,

    `entered_state_at` DATETIME DEFAULT NULL,

    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,

    PRIMARY KEY (`id`),
    
    UNIQUE KEY `uid` (`uid`) ,
    KEY `rolemodel_id` (`rolemodel_id`),
    KEY `status` (`status`) ,

    CONSTRAINT `task_rolemodel_id` FOREIGN KEY (`rolemodel_id`) REFERENCES `rolemodel` (`id`) ON DELETE CASCADE 

) ENGINE=InnoDB,AUTO_INCREMENT=101;


