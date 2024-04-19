
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

CREATE TABLE `roleuser` (

    `id` int UNSIGNED NOT NULL AUTO_INCREMENT,

    `api_id` INT UNSIGNED DEFAULT NULL,

    `pipeline_pause` BOOLEAN DEFAULT 0,

    `pipeline_max` int UNSIGNED DEFAULT 2,
    `pipeline_task_max` int UNSIGNED DEFAULT 3,
    `task_max` int UNSIGNED DEFAULT 4,
    `task_priority` int UNSIGNED DEFAULT 100,

    `task_debounce` int UNSIGNED DEFAULT 10,
    `task_runtime` int UNSIGNED DEFAULT 30,
    `task_deadline` int UNSIGNED DEFAULT 86400,

    `fs_size_max` int UNSIGNED DEFAULT 104857600,

    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,

    PRIMARY KEY (`id`) ,
    
    UNIQUE KEY `api_id` (`api_id`) ,
    
    CONSTRAINT `roleuser_ibfk_1` FOREIGN KEY (`api_id`) REFERENCES `api` (`id`) ON DELETE CASCADE

) ENGINE=InnoDB,AUTO_INCREMENT=101;
 




