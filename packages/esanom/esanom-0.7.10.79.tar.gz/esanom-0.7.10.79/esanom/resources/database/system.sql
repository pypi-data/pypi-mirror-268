
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

CREATE TABLE `system` (

    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,

    `key` varchar(255) NOT NULL ,

    `val_str` varchar(255) DEFAULT NULL ,
    `val_int` INT DEFAULT NULL ,
    `val_num` DOUBLE DEFAULT NULL ,

    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    
    PRIMARY KEY (`id`) ,

    UNIQUE KEY `key` (`key`) 

) ENGINE=InnoDB,AUTO_INCREMENT=101;
