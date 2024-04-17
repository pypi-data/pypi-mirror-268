
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

CREATE TABLE `port_pin` (

    `id` int NOT NULL AUTO_INCREMENT,
    
    `port_id` int UNSIGNED DEFAULT NULL,
    `pin_id` int UNSIGNED DEFAULT NULL,
    `cardinal` INT UNSIGNED DEFAULT 1,

    PRIMARY KEY (`id`),

    KEY `port_id` (`port_id`),
    KEY `pin_id` (`pin_id`),

    CONSTRAINT `port_pin_port_id` FOREIGN KEY (`port_id`) REFERENCES `port` (`id`) ON DELETE CASCADE,
    CONSTRAINT `port_pin_pin_id` FOREIGN KEY (`pin_id`) REFERENCES `pin` (`id`) ON DELETE CASCADE ,

    CONSTRAINT `port_pin_unique_portidpinid` UNIQUE (`port_id`,`pin_id`) 

) ENGINE=InnoDB,AUTO_INCREMENT=101;
