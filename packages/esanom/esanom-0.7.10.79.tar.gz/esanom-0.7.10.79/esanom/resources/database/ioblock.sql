
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

CREATE TABLE `ioblock` (

    `id` int UNSIGNED NOT NULL AUTO_INCREMENT,

    `io_id` INT UNSIGNED DEFAULT NULL,

    `block` INT UNSIGNED DEFAULT NULL,
    `size` INT UNSIGNED DEFAULT NULL,
    `hash` varchar(255) DEFAULT "",
    `compressor` varchar(16) DEFAULT NULL,

    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,

    PRIMARY KEY (`id`) ,
    
    KEY `io_id` (`io_id`),
    KEY `block` (`block`),
    
    CONSTRAINT `ioblock_ioid` FOREIGN KEY (`io_id`) REFERENCES `io` (`id`) ON DELETE CASCADE 

) ENGINE=InnoDB,AUTO_INCREMENT=101;
 




