--------------------------------------------------------
--  File created - Tuesday-July-18-2023   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table BORROW
--------------------------------------------------------

  CREATE TABLE "LMS"."BORROW" 
   (	"BOOK_ID" NUMBER, 
	"MEMBER_ID" NUMBER, 
	"BOOK_FEE" NUMBER, 
	"ISSUE_DATE" DATE, 
	"DUE_DATE" DATE, 
	"RETURN_DATE" DATE, 
	"FINE" NUMBER
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSAUX" ;
REM INSERTING into LMS.BORROW
SET DEFINE OFF;
Insert into LMS.BORROW (BOOK_ID,MEMBER_ID,BOOK_FEE,ISSUE_DATE,DUE_DATE,RETURN_DATE,FINE) values (4,3,400,to_date('16-JUN-23','DD-MON-RR'),to_date('20-JUN-23','DD-MON-RR'),null,null);
Insert into LMS.BORROW (BOOK_ID,MEMBER_ID,BOOK_FEE,ISSUE_DATE,DUE_DATE,RETURN_DATE,FINE) values (1,1,500,to_date('12-JUN-23','DD-MON-RR'),to_date('12-JUL-23','DD-MON-RR'),to_date('13-JUL-23','DD-MON-RR'),500);
Insert into LMS.BORROW (BOOK_ID,MEMBER_ID,BOOK_FEE,ISSUE_DATE,DUE_DATE,RETURN_DATE,FINE) values (2,2,600,to_date('13-JUN-23','DD-MON-RR'),to_date('13-JUL-23','DD-MON-RR'),null,500);
Insert into LMS.BORROW (BOOK_ID,MEMBER_ID,BOOK_FEE,ISSUE_DATE,DUE_DATE,RETURN_DATE,FINE) values (3,3,700,to_date('14-JUN-23','DD-MON-RR'),to_date('14-JUL-23','DD-MON-RR'),null,500);
Insert into LMS.BORROW (BOOK_ID,MEMBER_ID,BOOK_FEE,ISSUE_DATE,DUE_DATE,RETURN_DATE,FINE) values (4,4,800,to_date('15-JUN-23','DD-MON-RR'),to_date('15-JUL-23','DD-MON-RR'),null,500);
Insert into LMS.BORROW (BOOK_ID,MEMBER_ID,BOOK_FEE,ISSUE_DATE,DUE_DATE,RETURN_DATE,FINE) values (5,5,900,to_date('16-JUN-23','DD-MON-RR'),to_date('16-JUL-23','DD-MON-RR'),null,500);
Insert into LMS.BORROW (BOOK_ID,MEMBER_ID,BOOK_FEE,ISSUE_DATE,DUE_DATE,RETURN_DATE,FINE) values (2,1,200,to_date('12-JUL-23','DD-MON-RR'),to_date('20-JUL-23','DD-MON-RR'),null,null);
Insert into LMS.BORROW (BOOK_ID,MEMBER_ID,BOOK_FEE,ISSUE_DATE,DUE_DATE,RETURN_DATE,FINE) values (4,5,430,to_date('12-FEB-02','DD-MON-RR'),to_date('12-MAR-02','DD-MON-RR'),null,null);
Insert into LMS.BORROW (BOOK_ID,MEMBER_ID,BOOK_FEE,ISSUE_DATE,DUE_DATE,RETURN_DATE,FINE) values (6,6,350,to_date('13-JUL-23','DD-MON-RR'),to_date('20-JUL-23','DD-MON-RR'),null,null);
--------------------------------------------------------
--  DDL for Index BORROW_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "LMS"."BORROW_PK" ON "LMS"."BORROW" ("BOOK_ID", "MEMBER_ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSAUX" ;
--------------------------------------------------------
--  DDL for Trigger UPDATE_NO_OF_COPIES
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "LMS"."UPDATE_NO_OF_COPIES" 
AFTER INSERT ON borrow
FOR EACH ROW
BEGIN
    UPDATE books
    SET number_of_copies = number_of_copies - 1
    WHERE book_id = :NEW.book_id;
END;

/
ALTER TRIGGER "LMS"."UPDATE_NO_OF_COPIES" ENABLE;
--------------------------------------------------------
--  Constraints for Table BORROW
--------------------------------------------------------

  ALTER TABLE "LMS"."BORROW" MODIFY ("BOOK_ID" NOT NULL ENABLE);
  ALTER TABLE "LMS"."BORROW" MODIFY ("MEMBER_ID" NOT NULL ENABLE);
  ALTER TABLE "LMS"."BORROW" ADD CONSTRAINT "BORROW_PK" PRIMARY KEY ("BOOK_ID", "MEMBER_ID")
  USING INDEX "LMS"."BORROW_PK"  ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table BORROW
--------------------------------------------------------

  ALTER TABLE "LMS"."BORROW" ADD CONSTRAINT "MEMBER_FK" FOREIGN KEY ("MEMBER_ID")
	  REFERENCES "LMS"."MEMBERS" ("MEMBER_ID") ENABLE;
  ALTER TABLE "LMS"."BORROW" ADD CONSTRAINT "BOOK_FK" FOREIGN KEY ("BOOK_ID")
	  REFERENCES "LMS"."BOOKS" ("BOOK_ID") ENABLE;
