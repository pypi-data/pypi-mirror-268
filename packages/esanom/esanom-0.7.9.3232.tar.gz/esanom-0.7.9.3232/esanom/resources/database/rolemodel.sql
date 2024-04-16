
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

CREATE TABLE `rolemodel` (
    
    `id` int UNSIGNED NOT NULL AUTO_INCREMENT,

    `api_id` INT UNSIGNED DEFAULT NULL,

    `name` varchar(255) NOT NULL CHECK (`name` <> ""),
    
    `type` varchar(255) DEFAULT "model",

    `category` varchar(255) DEFAULT NULL ,

    `specs` TEXT NOT NULL CHECK (`specs` <> ""),
    `description` TEXT DEFAULT NULL ,

    `enable` BOOLEAN DEFAULT 0,
    `updateable` BOOLEAN DEFAULT 0,
    
    `ignore_pred_fail` BOOLEAN DEFAULT 0,

    `user_api_ip_prefix` varchar(255) DEFAULT "127.,192.168.,172.,10.",
    `user_api_email_postfix` varchar(255) DEFAULT "sparc.gr,esa.int,aeronomie.be",
    `input_size_max` BIGINT UNSIGNED DEFAULT 10485760,
    `task_batch_size` INT UNSIGNED DEFAULT 1,

    `lease_expire` int UNSIGNED DEFAULT 60 ,
    
    `uid` varchar(255) NOT NULL CHECK (`uid` <> "") ,

    `heartbeats` int UNSIGNED DEFAULT 0,
    `heartbeat_at` DATETIME DEFAULT NULL ,

    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,

    PRIMARY KEY (`id`),
    
    UNIQUE KEY `api_id` (`api_id`) ,
    UNIQUE KEY `name` (`name`),
    UNIQUE KEY `uid` (`uid`),
    KEY `enable` (`enable`),
    KEY `updateable` (`updateable`),

    CONSTRAINT `rolemodel_api_id` FOREIGN KEY (`api_id`) REFERENCES `api` (`id`) ON DELETE CASCADE

) ENGINE=InnoDB,AUTO_INCREMENT=101;





