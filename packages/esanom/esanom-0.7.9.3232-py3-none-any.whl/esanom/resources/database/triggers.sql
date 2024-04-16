
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

CREATE TRIGGER account_insert BEFORE INSERT ON account FOR EACH ROW BEGIN

    IF ( NEW.email_confirmed = 1 ) THEN
        SET NEW.email_confirmsent_at = NOW( ) ;
        SET NEW.email_confirmed_at = NOW( ) ;
    END IF ;

    SET NEW.password = SHA2( NEW.password , 256 ) ;

    SET NEW.uid = SHA2( CONCAT( NOW( ) , RAND( ) , UUID( ) , NEW.id , "7F6I12APOL" ) , 256 ) ;

END ;

/******************************************************************/

CREATE TRIGGER api_insert BEFORE INSERT ON api FOR EACH ROW BEGIN

    SET NEW.token = CONCAT( "NOM" , SUBSTRING( SHA2( CONCAT( NOW( ) , RAND( ) , UUID( ) , NEW.id , "7F6I12APOL" ) , 256 ) , 4 , 64 ) ) ;
    SET NEW.uid = SHA2( CONCAT( NOW( ) , RAND( ) , UUID( ) , NEW.id , "7F6I12APOL" ) , 256 ) ;

END ;

/******************************************************************/

CREATE TRIGGER pipeline_insert BEFORE INSERT ON pipeline FOR EACH ROW BEGIN

    SET NEW.uid = SHA2( CONCAT( NOW( ) , RAND( ) , UUID( ) , NEW.id , "7F6I12APOL" ) , 256 ) ;

END ;

CREATE TRIGGER pipeline_update BEFORE UPDATE ON pipeline FOR EACH ROW BEGIN

    SET NEW.status = UPPER( NEW.status ) ;

    IF OLD.done = 1 THEN
        SET NEW.status = OLD.status ;
    END IF ;

    IF NEW.status <> OLD.status THEN
        SET NEW.entered_state_at = NOW( ) ;
    END IF ;

    IF NEW.status = "COMPLETED" OR NEW.status = "FAILED" OR NEW.status = "CANCELLED" THEN
        SET NEW.done = 1 ;
    ELSE
        SET NEW.done = 0 ;
    END IF ;

    IF OLD.archived = 0 AND NEW.archived = 1 THEN
        SET NEW.archived_at = NOW( ) ;
    END IF ;

END ;

/******************************************************************/

CREATE TRIGGER task_insert BEFORE INSERT ON task FOR EACH ROW BEGIN

    SET NEW.uid = SHA2( CONCAT( NOW( ) , RAND( ) , UUID( ) , NEW.id , "7F6I12APOL" ) , 256 ) ;

END ;

CREATE TRIGGER task_update BEFORE UPDATE ON task FOR EACH ROW BEGIN

    SET NEW.status = UPPER( NEW.status ) ;
    
    IF OLD.done = 1 THEN
        SET NEW.status = OLD.status ;
    END IF ;

    IF NEW.status <> OLD.status THEN
        SET NEW.entered_state_at = NOW( ) ;
    END IF ;

    IF NEW.status = "COMPLETED" OR NEW.status = "FAILED" OR NEW.status = "CANCELLED" THEN
        SET NEW.done = 1 ;
    ELSE
        SET NEW.done = 0 ;
    END IF ;

    IF NEW.status = "RUNNING" THEN
        SET NEW.running_at = NOW( ) ;
    END IF ;

    IF NEW.heartbeat_at IS NOT NULL AND OLD.heartbeat_at IS NULL THEN
        SET NEW.heartbeats = OLD.heartbeats + 1 ;
    END IF ;

    IF NEW.heartbeat_at <> OLD.heartbeat_at THEN
        SET NEW.heartbeats = OLD.heartbeats + 1 ;
    END IF ;

END ;

/******************************************************************/

CREATE TRIGGER io_insert BEFORE INSERT ON io FOR EACH ROW BEGIN

    SET NEW.uid = SHA2( CONCAT( NOW( ) , RAND( ) , UUID( ) , NEW.id , "7F6I12APOL" ) , 256 ) ;

END ;

/******************************************************************/

CREATE TRIGGER rolemodel_insert BEFORE INSERT ON rolemodel FOR EACH ROW BEGIN

    SET NEW.uid = SHA2( CONCAT( NOW( ) , RAND( ) , UUID( ) , NEW.id , "7F6I12APOL" ) , 256 ) ;

END ;

CREATE TRIGGER rolemodel_update BEFORE UPDATE ON rolemodel FOR EACH ROW BEGIN

    IF NEW.heartbeat_at IS NOT NULL AND OLD.heartbeat_at IS NULL THEN
        SET NEW.heartbeats = OLD.heartbeats + 1 ;
    END IF ;
    
    IF NEW.heartbeat_at <> OLD.heartbeat_at THEN
        SET NEW.heartbeats = OLD.heartbeats + 1 ;
    END IF ;

END ;

/******************************************************************/

CREATE TRIGGER claim_insert BEFORE INSERT ON claim FOR EACH ROW BEGIN

    SET NEW.uid = SHA2( CONCAT( NOW( ) , RAND( ) , UUID( ) , NEW.id , "7F6I12APOL" ) , 256 ) ;

END ;

/******************************************************************/

CREATE TRIGGER port_insert BEFORE INSERT ON port FOR EACH ROW BEGIN

    SET NEW.uid = SHA2( CONCAT( NOW( ) , RAND( ) , UUID( ) , NEW.id , "7F6I12APOL" ) , 256 ) ;

END ;

