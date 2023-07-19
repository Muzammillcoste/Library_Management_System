--------------------------------------------------------
--  File created - Tuesday-July-18-2023   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table LOGIN
--------------------------------------------------------

  CREATE TABLE "LMS"."LOGIN" 
   (	"ADMIN_ID" NUMBER, 
	"STAFF_ID" NUMBER
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSAUX" ;
REM INSERTING into LMS.LOGIN
SET DEFINE OFF;
Insert into LMS.LOGIN (ADMIN_ID,STAFF_ID) values (2023003,9);
Insert into LMS.LOGIN (ADMIN_ID,STAFF_ID) values (2023001,1);
Insert into LMS.LOGIN (ADMIN_ID,STAFF_ID) values (2023002,8);
--------------------------------------------------------
--  Constraints for Table LOGIN
--------------------------------------------------------

  ALTER TABLE "LMS"."LOGIN" MODIFY ("ADMIN_ID" NOT NULL ENABLE);
  ALTER TABLE "LMS"."LOGIN" MODIFY ("STAFF_ID" NOT NULL ENABLE);
--------------------------------------------------------
--  Ref Constraints for Table LOGIN
--------------------------------------------------------

  ALTER TABLE "LMS"."LOGIN" ADD CONSTRAINT "LOGIN_FK" FOREIGN KEY ("ADMIN_ID")
	  REFERENCES "LMS"."AUTHENTICATION_SYSTEM" ("ADMIN_ID") ENABLE;
  ALTER TABLE "LMS"."LOGIN" ADD CONSTRAINT "LOGIN_STAFF_FK" FOREIGN KEY ("STAFF_ID")
	  REFERENCES "LMS"."STAFF" ("STAFF_ID") ENABLE;
