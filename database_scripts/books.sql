--------------------------------------------------------
--  File created - Tuesday-July-18-2023   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table BOOKS
--------------------------------------------------------

  CREATE TABLE "LMS"."BOOKS" 
   (	"BOOK_ID" NUMBER, 
	"BOOK_TITLE" VARCHAR2(100 BYTE), 
	"AUTHOR_NAME" VARCHAR2(100 BYTE), 
	"PUBLISHER" VARCHAR2(100 BYTE), 
	"NUMBER_OF_COPIES" NUMBER(4,0), 
	"SHELF_LOCATION" VARCHAR2(10 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSAUX" ;
REM INSERTING into LMS.BOOKS
SET DEFINE OFF;
Insert into LMS.BOOKS (BOOK_ID,BOOK_TITLE,AUTHOR_NAME,PUBLISHER,NUMBER_OF_COPIES,SHELF_LOCATION) values (1,'Calculus: Early Transcendentals','James Stewart',' Cengage Learning',800,'M1');
Insert into LMS.BOOKS (BOOK_ID,BOOK_TITLE,AUTHOR_NAME,PUBLISHER,NUMBER_OF_COPIES,SHELF_LOCATION) values (2,'Calculus','Michael Spivak','Cambridge University Press',598,'M2');
Insert into LMS.BOOKS (BOOK_ID,BOOK_TITLE,AUTHOR_NAME,PUBLISHER,NUMBER_OF_COPIES,SHELF_LOCATION) values (3,'Introduction to Algorithms','Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein','MIT Press
',351,'D1');
Insert into LMS.BOOKS (BOOK_ID,BOOK_TITLE,AUTHOR_NAME,PUBLISHER,NUMBER_OF_COPIES,SHELF_LOCATION) values (4,'Data Structures and Algorithms Made Easy','Narasimha Karumanchi','CareerMonk Publications',496,'D2');
Insert into LMS.BOOKS (BOOK_ID,BOOK_TITLE,AUTHOR_NAME,PUBLISHER,NUMBER_OF_COPIES,SHELF_LOCATION) values (5,'Electronic Principles','Albert Malvino and David Bates','McGraw-Hill Education',700,'E1');
Insert into LMS.BOOKS (BOOK_ID,BOOK_TITLE,AUTHOR_NAME,PUBLISHER,NUMBER_OF_COPIES,SHELF_LOCATION) values (6,'computer','kumar','abc',330,'E23');
Insert into LMS.BOOKS (BOOK_ID,BOOK_TITLE,AUTHOR_NAME,PUBLISHER,NUMBER_OF_COPIES,SHELF_LOCATION) values (12,'Aram Gah','Furqan Ahmed','MIT PRESS',700,'E23');
Insert into LMS.BOOKS (BOOK_ID,BOOK_TITLE,AUTHOR_NAME,PUBLISHER,NUMBER_OF_COPIES,SHELF_LOCATION) values (7,'Pakistan studies','Umar Sadiq','McGraw-Hill Education',700,'E23');
Insert into LMS.BOOKS (BOOK_ID,BOOK_TITLE,AUTHOR_NAME,PUBLISHER,NUMBER_OF_COPIES,SHELF_LOCATION) values (8,'Transulent ','stan lee','McGraw-Hill Education',700,'E23');
Insert into LMS.BOOKS (BOOK_ID,BOOK_TITLE,AUTHOR_NAME,PUBLISHER,NUMBER_OF_COPIES,SHELF_LOCATION) values (9,'The Boys','stan Lee','McGraw-Hill Education',700,'E23');
Insert into LMS.BOOKS (BOOK_ID,BOOK_TITLE,AUTHOR_NAME,PUBLISHER,NUMBER_OF_COPIES,SHELF_LOCATION) values (10,'Marvel','stan lee','McGraw-Hill Education',700,'E23');
Insert into LMS.BOOKS (BOOK_ID,BOOK_TITLE,AUTHOR_NAME,PUBLISHER,NUMBER_OF_COPIES,SHELF_LOCATION) values (11,'Mehfil','Ifrikhar Ali','McGraw-Hill Education',700,'E23');
Insert into LMS.BOOKS (BOOK_ID,BOOK_TITLE,AUTHOR_NAME,PUBLISHER,NUMBER_OF_COPIES,SHELF_LOCATION) values (13,'safar e zindagi','Ali Hasnain','McGraw-Hill Education',700,'E23');
Insert into LMS.BOOKS (BOOK_ID,BOOK_TITLE,AUTHOR_NAME,PUBLISHER,NUMBER_OF_COPIES,SHELF_LOCATION) values (14,'Kidpanned','Alex turing','McGraw-Hill Education',700,'E23');
Insert into LMS.BOOKS (BOOK_ID,BOOK_TITLE,AUTHOR_NAME,PUBLISHER,NUMBER_OF_COPIES,SHELF_LOCATION) values (15,'Imitation Game','Elan Turing','McGraw-Hill Education',700,'E23');
--------------------------------------------------------
--  DDL for Index BOOKS_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "LMS"."BOOKS_PK" ON "LMS"."BOOKS" ("BOOK_ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSAUX" ;
--------------------------------------------------------
--  Constraints for Table BOOKS
--------------------------------------------------------

  ALTER TABLE "LMS"."BOOKS" MODIFY ("BOOK_ID" NOT NULL ENABLE);
  ALTER TABLE "LMS"."BOOKS" ADD CONSTRAINT "BOOKS_PK" PRIMARY KEY ("BOOK_ID")
  USING INDEX "LMS"."BOOKS_PK"  ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table BOOKS
--------------------------------------------------------

  ALTER TABLE "LMS"."BOOKS" ADD CONSTRAINT "BOOKS_FK" FOREIGN KEY ("BOOK_ID")
	  REFERENCES "LMS"."BOOKS" ("BOOK_ID") DISABLE;
