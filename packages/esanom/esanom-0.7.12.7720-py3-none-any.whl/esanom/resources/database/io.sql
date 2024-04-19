
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

CREATE TABLE `io` (

    `id` int UNSIGNED NOT NULL AUTO_INCREMENT,

    `uid` varchar(255) NOT NULL CHECK (`uid` <> ""),
    
    `task_id` INT UNSIGNED DEFAULT NULL,
    `mpin_id` INT UNSIGNED DEFAULT NULL,

    `current_role_name` varchar(255) DEFAULT NULL ,

    `port_ordinal` INT UNSIGNED DEFAULT 0,
    `pin_ordinal` INT UNSIGNED DEFAULT 0,

    `blocks` INT UNSIGNED DEFAULT NULL,

    `size` BIGINT UNSIGNED DEFAULT NULL,
    `hash` varchar(255) DEFAULT NULL,

    `download` BOOLEAN DEFAULT 1,

    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    `accessed_at` DATETIME DEFAULT NULL,

    PRIMARY KEY (`id`) ,
    UNIQUE KEY `uid` (`uid`) ,
    
    KEY `task_id` (`task_id`),
    KEY `mpin_id` (`mpin_id`),
    
    CONSTRAINT `io_task_id` FOREIGN KEY (`task_id`) REFERENCES `task` (`id`) ON DELETE CASCADE ,
    CONSTRAINT `io_mpinid` FOREIGN KEY (`mpin_id`) REFERENCES `mpin` (`id`) ON DELETE CASCADE 

) ENGINE=InnoDB,AUTO_INCREMENT=101;
 




