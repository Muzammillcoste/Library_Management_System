--------------------------------------------------------
--  File created - Tuesday-July-18-2023   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table AUTHENTICATION_SYSTEM
--------------------------------------------------------

  CREATE TABLE "LMS"."AUTHENTICATION_SYSTEM" 
   (	"ADMIN_ID" NUMBER, 
	"PASSWORD" VARCHAR2(30 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSAUX" ;
REM INSERTING into LMS.AUTHENTICATION_SYSTEM
SET DEFINE OFF;
Insert into LMS.AUTHENTICATION_SYSTEM (ADMIN_ID,PASSWORD) values (2023003,'dbmsproject3');
Insert into LMS.AUTHENTICATION_SYSTEM (ADMIN_ID,PASSWORD) values (2023001,'dbmsproject1');
Insert into LMS.AUTHENTICATION_SYSTEM (ADMIN_ID,PASSWORD) values (2023002,'dbmsproject2');
--------------------------------------------------------
--  DDL for Index AUTHEN_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "LMS"."AUTHEN_PK" ON "LMS"."AUTHENTICATION_SYSTEM" ("ADMIN_ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSAUX" ;
--------------------------------------------------------
--  Constraints for Table AUTHENTICATION_SYSTEM
--------------------------------------------------------

  ALTER TABLE "LMS"."AUTHENTICATION_SYSTEM" MODIFY ("ADMIN_ID" NOT NULL ENABLE);
  ALTER TABLE "LMS"."AUTHENTICATION_SYSTEM" MODIFY ("PASSWORD" NOT NULL ENABLE);
  ALTER TABLE "LMS"."AUTHENTICATION_SYSTEM" ADD CONSTRAINT "AUTHEN_PK" PRIMARY KEY ("ADMIN_ID")
  USING INDEX "LMS"."AUTHEN_PK"  ENABLE;
