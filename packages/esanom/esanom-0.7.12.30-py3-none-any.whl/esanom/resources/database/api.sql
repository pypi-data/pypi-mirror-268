
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

CREATE TABLE `api` (

    `id` int UNSIGNED NOT NULL AUTO_INCREMENT,

    `account_id` INT UNSIGNED DEFAULT NULL,
    
    `token` varchar(255) NOT NULL CHECK (`token` <> ""),

    `name` varchar(255) DEFAULT NULL,

    `ip_update` BOOLEAN DEFAULT 0,
    `ip` varchar(255) DEFAULT "127.,192.168.,172.,10.",

    `enable` BOOLEAN DEFAULT 0,

    `io_size_max` int UNSIGNED DEFAULT 10485760,

    `limiter_minute` int UNSIGNED DEFAULT 60,
    
    `uid` varchar(255) NOT NULL CHECK (`uid` <> ""),
    
    `expires_at` DATETIME DEFAULT (NOW() + INTERVAL 3 MONTH) ,

    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    `accessed_at` DATETIME DEFAULT NULL,

    PRIMARY KEY (`id`) ,

    UNIQUE KEY `token` (`token`) ,
    UNIQUE KEY `uid` (`uid`) ,
    KEY `enable` (`enable`) ,
    KEY `account_id` (`account_id`),
    CONSTRAINT `api_account` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`) ON DELETE CASCADE

) ENGINE=InnoDB,AUTO_INCREMENT=101;
 




