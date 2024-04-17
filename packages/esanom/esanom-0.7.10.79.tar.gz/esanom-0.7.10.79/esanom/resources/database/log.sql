
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

CREATE TABLE `log` (

    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,

    `source` varchar(255) DEFAULT "",
    `event` varchar(255) DEFAULT "" ,
    `level` varchar(255) DEFAULT "DEBUG",
    `msg` varchar(255) DEFAULT "",

    `pipeline_id` INT UNSIGNED DEFAULT NULL,
    `task_id` INT UNSIGNED DEFAULT NULL,

    `data` TEXT DEFAULT NULL,

    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (`id`) ,

    KEY `level` (`level`) ,
    KEY `source` (`source`) ,
    KEY `pipeline_id` (`pipeline_id`) ,
    KEY `task_id` (`task_id`) ,

    CONSTRAINT `log_pipelineid` FOREIGN KEY (`pipeline_id`) REFERENCES `pipeline` (`id`) ON DELETE CASCADE ,
    CONSTRAINT `log_taskid` FOREIGN KEY (`task_id`) REFERENCES `task` (`id`) ON DELETE CASCADE 

) ENGINE=InnoDB,AUTO_INCREMENT=101;
