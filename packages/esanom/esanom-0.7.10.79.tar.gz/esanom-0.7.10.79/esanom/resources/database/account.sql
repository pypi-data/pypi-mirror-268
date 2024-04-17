
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

CREATE TABLE `account` (

    `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
    
    `email` varchar(255) NOT NULL CHECK (`email` <> ""),
    `password` varchar(255) DEFAULT NULL,
    `name` varchar(255) DEFAULT NULL,

    `enable` BOOLEAN DEFAULT 0,

    `email_confirmsent_at` DATETIME DEFAULT NULL,
    `email_confirmed` BOOLEAN DEFAULT 0,
    `email_confirmed_at` DATETIME DEFAULT NULL,
    
    `api_max` int UNSIGNED DEFAULT 2,
    
    `uid` varchar(255) NOT NULL CHECK (`uid` <> ""),

    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    `accessed_at` DATETIME DEFAULT NULL,

    PRIMARY KEY (`id`) ,
    UNIQUE KEY `email` (`email`) ,
    UNIQUE KEY `uid` (`uid`) ,
    KEY `enable` (`enable`) 

) ENGINE=InnoDB,AUTO_INCREMENT=101;
 




