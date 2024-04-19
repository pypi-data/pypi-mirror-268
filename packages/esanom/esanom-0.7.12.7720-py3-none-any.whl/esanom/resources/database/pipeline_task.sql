
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

CREATE TABLE `pipeline_task` (

    `id` int NOT NULL AUTO_INCREMENT,

    `pipeline_id` int UNSIGNED DEFAULT NULL,

    `task_id` int UNSIGNED DEFAULT NULL,
    `next_task_id` int UNSIGNED DEFAULT NULL,

    PRIMARY KEY (`id`),

    KEY `pipeline_id` (`pipeline_id`),
    KEY `task_id` (`task_id`),
    KEY `next_task_id` (`next_task_id`),

    CONSTRAINT `pipeline_task_pipelineid` FOREIGN KEY (`pipeline_id`) REFERENCES `pipeline` (`id`) ON DELETE CASCADE,
    CONSTRAINT `pipeline_task_taskid` FOREIGN KEY (`task_id`) REFERENCES `task` (`id`) ON DELETE CASCADE,
    CONSTRAINT `pipeline_task_nexttaskid` FOREIGN KEY (`next_task_id`) REFERENCES `task` (`id`) ON DELETE CASCADE

) ENGINE=InnoDB,AUTO_INCREMENT=101;
