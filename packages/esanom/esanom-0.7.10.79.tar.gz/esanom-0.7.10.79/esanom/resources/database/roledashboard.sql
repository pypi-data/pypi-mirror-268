
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

CREATE TABLE `roledashboard` (

    `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
    
    `api_id` INT UNSIGNED DEFAULT NULL,

    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,

    PRIMARY KEY (`id`) ,
    UNIQUE KEY `api_id` (`api_id`) ,
    
    CONSTRAINT `roledashboard_api_id` FOREIGN KEY (`api_id`) REFERENCES `api` (`id`) ON DELETE CASCADE

) ENGINE=InnoDB,AUTO_INCREMENT=101;
 




