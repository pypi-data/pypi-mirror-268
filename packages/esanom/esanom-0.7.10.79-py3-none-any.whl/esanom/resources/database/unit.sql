
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

CREATE TABLE `unit` (

    `id` int UNSIGNED NOT NULL AUTO_INCREMENT,

    `pin_id` INT UNSIGNED DEFAULT NULL,
    
    `visible` BOOLEAN DEFAULT 1,

    `name` varchar(255) DEFAULT "",
    `description` TEXT ,
    `symbol` varchar(255) DEFAULT "",

    `default` BOOLEAN DEFAULT 0,

    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,

    PRIMARY KEY (`id`) ,

    KEY `pin_id` (`pin_id`),
    KEY `default` (`default`),

    CONSTRAINT `unit_pin_id` FOREIGN KEY (`pin_id`) REFERENCES `pin` (`id`) ON DELETE CASCADE 
    
) ENGINE=InnoDB,AUTO_INCREMENT=101;
 




