--------------------------------------------------------
--  File created - Tuesday-July-18-2023   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table MEMBERS
--------------------------------------------------------

  CREATE TABLE "LMS"."MEMBERS" 
   (	"MEMBER_ID" NUMBER(10,0), 
	"FIRST_NAME" VARCHAR2(50 BYTE), 
	"LAST_NAME" VARCHAR2(50 BYTE), 
	"RESIDENTIAL_ADDRESS" VARCHAR2(100 BYTE), 
	"CONTACT_NUMBER" NUMBER(30,0), 
	"EMAIL_ADDRESS" VARCHAR2(100 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSAUX" ;
REM INSERTING into LMS.MEMBERS
SET DEFINE OFF;
Insert into LMS.MEMBERS (MEMBER_ID,FIRST_NAME,LAST_NAME,RESIDENTIAL_ADDRESS,CONTACT_NUMBER,EMAIL_ADDRESS) values (1,'Ali','Ahmed','189-B sadiqabad karachi',3347634564,'aliahmed@gmail.com');
Insert into LMS.MEMBERS (MEMBER_ID,FIRST_NAME,LAST_NAME,RESIDENTIAL_ADDRESS,CONTACT_NUMBER,EMAIL_ADDRESS) values (2,'inaam','Aijaz','145-G clifton karachi',3335609871,'kareemaijaz@gmail.com');
Insert into LMS.MEMBERS (MEMBER_ID,FIRST_NAME,LAST_NAME,RESIDENTIAL_ADDRESS,CONTACT_NUMBER,EMAIL_ADDRESS) values (3,'Wasay','Zulfiqar','199-A malir colony karachi',33298126530976,'wasayzulfiqar@gmail.com');
Insert into LMS.MEMBERS (MEMBER_ID,FIRST_NAME,LAST_NAME,RESIDENTIAL_ADDRESS,CONTACT_NUMBER,EMAIL_ADDRESS) values (4,'Shahid','Afridi','144-H jacobabad karachi',3315009876,'Shahidafridi@gmail.com');
Insert into LMS.MEMBERS (MEMBER_ID,FIRST_NAME,LAST_NAME,RESIDENTIAL_ADDRESS,CONTACT_NUMBER,EMAIL_ADDRESS) values (5,'Waseem','Khan','111-T block johar karachi',33240987123456,'waseemkhan@gmail.com');
Insert into LMS.MEMBERS (MEMBER_ID,FIRST_NAME,LAST_NAME,RESIDENTIAL_ADDRESS,CONTACT_NUMBER,EMAIL_ADDRESS) values (9,'Raim','jamshad','Model',3084739478,'raim@gmail.com');
Insert into LMS.MEMBERS (MEMBER_ID,FIRST_NAME,LAST_NAME,RESIDENTIAL_ADDRESS,CONTACT_NUMBER,EMAIL_ADDRESS) values (7,'Qaim','Ahmed','17-B Johar karachi',3584938230923,'qaim@gmail.com');
Insert into LMS.MEMBERS (MEMBER_ID,FIRST_NAME,LAST_NAME,RESIDENTIAL_ADDRESS,CONTACT_NUMBER,EMAIL_ADDRESS) values (8,'Kumar','Afridi','University Road',33894843432,'Kumaar@gmail.com');
Insert into LMS.MEMBERS (MEMBER_ID,FIRST_NAME,LAST_NAME,RESIDENTIAL_ADDRESS,CONTACT_NUMBER,EMAIL_ADDRESS) values (10,'fatima','ali','block johar',340232323,'fatima@gmail.com');
Insert into LMS.MEMBERS (MEMBER_ID,FIRST_NAME,LAST_NAME,RESIDENTIAL_ADDRESS,CONTACT_NUMBER,EMAIL_ADDRESS) values (11,'feroz','zulfiqar','Malir JT',335353973,'feroz@gmail.com');
Insert into LMS.MEMBERS (MEMBER_ID,FIRST_NAME,LAST_NAME,RESIDENTIAL_ADDRESS,CONTACT_NUMBER,EMAIL_ADDRESS) values (6,'qasim','ali','malir JT',3302647872,'muz@gmail.com');
--------------------------------------------------------
--  DDL for Index MEMBERS_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "LMS"."MEMBERS_PK" ON "LMS"."MEMBERS" ("MEMBER_ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSAUX" ;
--------------------------------------------------------
--  Constraints for Table MEMBERS
--------------------------------------------------------

  ALTER TABLE "LMS"."MEMBERS" MODIFY ("MEMBER_ID" NOT NULL ENABLE);
  ALTER TABLE "LMS"."MEMBERS" ADD CONSTRAINT "MEMBERS_PK" PRIMARY KEY ("MEMBER_ID")
  USING INDEX "LMS"."MEMBERS_PK"  ENABLE;
