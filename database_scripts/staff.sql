--------------------------------------------------------
--  File created - Tuesday-July-18-2023   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table STAFF
--------------------------------------------------------

  CREATE TABLE "LMS"."STAFF" 
   (	"STAFF_ID" NUMBER, 
	"STAFF_NAME" VARCHAR2(40 BYTE), 
	"DESIGNATION" VARCHAR2(40 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSAUX" ;
REM INSERTING into LMS.STAFF
SET DEFINE OFF;
Insert into LMS.STAFF (STAFF_ID,STAFF_NAME,DESIGNATION) values (8,'hasnain','book manager');
Insert into LMS.STAFF (STAFF_ID,STAFF_NAME,DESIGNATION) values (9,'raza','member manager');
Insert into LMS.STAFF (STAFF_ID,STAFF_NAME,DESIGNATION) values (1,'niazi','Librarian');
Insert into LMS.STAFF (STAFF_ID,STAFF_NAME,DESIGNATION) values (2,'gull mehar','Library Assistant');
Insert into LMS.STAFF (STAFF_ID,STAFF_NAME,DESIGNATION) values (3,'saljan','Circulation Desk Staff');
Insert into LMS.STAFF (STAFF_ID,STAFF_NAME,DESIGNATION) values (4,'ali','Reference Librarian');
Insert into LMS.STAFF (STAFF_ID,STAFF_NAME,DESIGNATION) values (5,'nawaz','Periodicals and Serials Staff');
Insert into LMS.STAFF (STAFF_ID,STAFF_NAME,DESIGNATION) values (6,'muzammil','admin');
Insert into LMS.STAFF (STAFF_ID,STAFF_NAME,DESIGNATION) values (7,'vinod','manager');
--------------------------------------------------------
--  DDL for Index STAFF_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "LMS"."STAFF_PK" ON "LMS"."STAFF" ("STAFF_ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSAUX" ;
--------------------------------------------------------
--  Constraints for Table STAFF
--------------------------------------------------------

  ALTER TABLE "LMS"."STAFF" MODIFY ("STAFF_ID" NOT NULL ENABLE);
  ALTER TABLE "LMS"."STAFF" ADD CONSTRAINT "STAFF_PK" PRIMARY KEY ("STAFF_ID")
  USING INDEX "LMS"."STAFF_PK"  ENABLE;
