/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     08/08/2022 10:56:30 p. m.                    */
/*==============================================================*/


drop index ARTIST_PK;

drop table ARTIST;

drop index ARTISTIC_TECHNIC_PK;

drop table ARTISTIC_TECHNIC;

drop index ARTWORK_PK;

drop table ARTWORK;

drop index RELATIONSHIP_4_FK;

drop index RELATIONSHIP_6_FK;

drop index ARTWORK_ARTIST_PK;

drop table ARTWORK_ARTIST;

drop index RELATIONSHIP_5_FK;

drop index RELATIONSHIP_7_FK;

drop index ARTWORK_TECHNIC_PK;

drop table ARTWORK_TECHNIC;

drop index CATEGORY_PK;

drop table CATEGORY;

drop index DOCTYPE_PK;

drop table DOCTYPE;

drop index RELATIONSHIP_10_FK;

drop index RELATIONSHIP_9_FK;

drop index IDEAS_PK;

drop table IDEAS;

drop index RELATIONSHIP_8_FK;

drop index RELATIONSHIP_7_FK2;

drop index MESSAGE_PK;

drop table MESSAGE;

drop index RELATIONSHIP_3_FK;

drop index RELATIONSHIP_2_FK;

drop index RATING_PK;

drop table RATING;

drop index RELATIONSHIP_1_FK;

drop index USERS_PK;

drop table USERS;

/*==============================================================*/
/* Table: ARTIST                                                */
/*==============================================================*/
create table ARTIST (
   ID_ARTIST            SERIAL               not null,
   NAME_ARTIST          VARCHAR(1024)        not null,
   LASTNAME_ARTIST      VARCHAR(1024)        not null,
   EMAIL_ARTIST         VARCHAR(1024)        not null,
   PHONE                NUMERIC              not null,
   constraint PK_ARTIST primary key (ID_ARTIST)
);

/*==============================================================*/
/* Index: ARTIST_PK                                             */
/*==============================================================*/
create unique index ARTIST_PK on ARTIST (
ID_ARTIST
);

/*==============================================================*/
/* Table: ARTISTIC_TECHNIC                                      */
/*==============================================================*/
create table ARTISTIC_TECHNIC (
   ID_AT                SERIAL               not null,
   TITLE                VARCHAR(1024)        not null,
   DESCRIPTION          VARCHAR(1024)        not null,
   constraint PK_ARTISTIC_TECHNIC primary key (ID_AT)
);

/*==============================================================*/
/* Index: ARTISTIC_TECHNIC_PK                                   */
/*==============================================================*/
create unique index ARTISTIC_TECHNIC_PK on ARTISTIC_TECHNIC (
ID_AT
);

/*==============================================================*/
/* Table: ARTWORK                                               */
/*==============================================================*/
create table ARTWORK (
   ID_ARTWORK           SERIAL               not null,
   TITLE_ARTWORK        VARCHAR(1024)        not null,
   DESCRIPTRION_ARTWORK VARCHAR(1024)        not null,
   DATE_PUBLISHED       DATE                 not null,
   IMAGE                VARCHAR(1024)        not null,
   constraint PK_ARTWORK primary key (ID_ARTWORK)
);

/*==============================================================*/
/* Index: ARTWORK_PK                                            */
/*==============================================================*/
create unique index ARTWORK_PK on ARTWORK (
ID_ARTWORK
);

/*==============================================================*/
/* Table: ARTWORK_ARTIST                                        */
/*==============================================================*/
create table ARTWORK_ARTIST (
   ID_ARTWORKARTIST     SERIAL               not null,
   ID_ARTIST_FK         INT4                 not null,
   ID_ARTWORK_FK        INT4                 not null,
   constraint PK_ARTWORK_ARTIST primary key (ID_ARTIST_FK, ID_ARTWORK_FK, ID_ARTWORKARTIST)
);

/*==============================================================*/
/* Index: ARTWORK_ARTIST_PK                                     */
/*==============================================================*/
create unique index ARTWORK_ARTIST_PK on ARTWORK_ARTIST (
ID_ARTIST_FK,
ID_ARTWORK_FK,
ID_ARTWORKARTIST
);

/*==============================================================*/
/* Index: RELATIONSHIP_6_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_6_FK on ARTWORK_ARTIST (
ID_ARTWORK_FK
);

/*==============================================================*/
/* Index: RELATIONSHIP_4_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_4_FK on ARTWORK_ARTIST (
ID_ARTIST_FK
);

/*==============================================================*/
/* Table: ARTWORK_TECHNIC                                       */
/*==============================================================*/
create table ARTWORK_TECHNIC (
   ID_ARTWORK_TECHNIC_PK SERIAL               not null,
   ID_AT_FK             INT4                 not null,
   ID_ARTWORK_FK        INT4                 not null,
   constraint PK_ARTWORK_TECHNIC primary key (ID_AT_FK, ID_ARTWORK_FK, ID_ARTWORK_TECHNIC_PK)
);

/*==============================================================*/
/* Index: ARTWORK_TECHNIC_PK                                    */
/*==============================================================*/
create unique index ARTWORK_TECHNIC_PK on ARTWORK_TECHNIC (
ID_AT_FK,
ID_ARTWORK_FK,
ID_ARTWORK_TECHNIC_PK
);

/*==============================================================*/
/* Index: RELATIONSHIP_7_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_7_FK on ARTWORK_TECHNIC (
ID_ARTWORK_FK
);

/*==============================================================*/
/* Index: RELATIONSHIP_5_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_5_FK on ARTWORK_TECHNIC (
ID_AT_FK
);

/*==============================================================*/
/* Table: CATEGORY                                              */
/*==============================================================*/
create table CATEGORY (
   ID_CATEGORY          SERIAL               not null,
   CAT_NAME             VARCHAR(1024)        not null,
   constraint PK_CATEGORY primary key (ID_CATEGORY)
);

/*==============================================================*/
/* Index: CATEGORY_PK                                           */
/*==============================================================*/
create unique index CATEGORY_PK on CATEGORY (
ID_CATEGORY
);

/*==============================================================*/
/* Table: DOCTYPE                                               */
/*==============================================================*/
create table DOCTYPE (
   ID_DOC               SERIAL               not null,
   TYPE_DOC             TEXT                 not null,
   constraint PK_DOCTYPE primary key (ID_DOC)
);

/*==============================================================*/
/* Index: DOCTYPE_PK                                            */
/*==============================================================*/
create unique index DOCTYPE_PK on DOCTYPE (
ID_DOC
);

/*==============================================================*/
/* Table: IDEAS                                                 */
/*==============================================================*/
create table IDEAS (
   ID_IDEAS             SERIAL               not null,
   ID_CATEGORY_IDFK     INT4                 null,
   ID_USER_IDFK         INT4                 null,
   IDEAS_TITLE          VARCHAR(1024)        not null,
   IDEAS_DESC           VARCHAR(1024)        not null,
   IS_PUBLIC            BOOL                 not null,
   constraint PK_IDEAS primary key (ID_IDEAS)
);

/*==============================================================*/
/* Index: IDEAS_PK                                              */
/*==============================================================*/
create unique index IDEAS_PK on IDEAS (
ID_IDEAS
);

/*==============================================================*/
/* Index: RELATIONSHIP_9_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_9_FK on IDEAS (
ID_CATEGORY_IDFK
);

/*==============================================================*/
/* Index: RELATIONSHIP_10_FK                                    */
/*==============================================================*/
create  index RELATIONSHIP_10_FK on IDEAS (
ID_USER_IDFK
);

/*==============================================================*/
/* Table: MESSAGE                                               */
/*==============================================================*/
create table MESSAGE (
   ID_MESSAGE           SERIAL               not null,
   ID_ARTIST_MESS_FK    INT4                 null,
   ID_USER_MESS_FK      INT4                 null,
   SUBJECT              VARCHAR(1024)        not null,
   MESSAGE              VARCHAR(1024)        not null,
   constraint PK_MESSAGE primary key (ID_MESSAGE)
);

/*==============================================================*/
/* Index: MESSAGE_PK                                            */
/*==============================================================*/
create unique index MESSAGE_PK on MESSAGE (
ID_MESSAGE
);

/*==============================================================*/
/* Index: RELATIONSHIP_7_FK2                                    */
/*==============================================================*/
create  index RELATIONSHIP_7_FK2 on MESSAGE (
ID_ARTIST_MESS_FK
);

/*==============================================================*/
/* Index: RELATIONSHIP_8_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_8_FK on MESSAGE (
ID_USER_MESS_FK
);

/*==============================================================*/
/* Table: RATING                                                */
/*==============================================================*/
create table RATING (
   ID_RATING            SERIAL               not null,
   ID_USER              INT4                 not null,
   ID_ARTWORK           INT4                 not null,
   RATING               NUMERIC              not null,
   OPINION              VARCHAR(1024)        not null,
   DATE                 DATE                 not null,
   constraint PK_RATING primary key (ID_RATING)
);

/*==============================================================*/
/* Index: RATING_PK                                             */
/*==============================================================*/
create unique index RATING_PK on RATING (
ID_RATING
);

/*==============================================================*/
/* Index: RELATIONSHIP_2_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_2_FK on RATING (
ID_USER
);

/*==============================================================*/
/* Index: RELATIONSHIP_3_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_3_FK on RATING (
ID_ARTWORK
);

/*==============================================================*/
/* Table: USERS                                                 */
/*==============================================================*/
create table USERS (
   ID_USER              INT4                 not null,
   ID_DOC               INT4                 not null,
   NAME_USER            VARCHAR(1024)        not null,
   LASTNAME_USER        VARCHAR(1024)        not null,
   PASSWORD             VARCHAR(1024)        not null,
   EMAIL_USER           VARCHAR(1024)        not null,
   TYPE                 VARCHAR(1024)        not null,
   constraint PK_USERS primary key (ID_USER)
);

/*==============================================================*/
/* Index: USERS_PK                                              */
/*==============================================================*/
create unique index USERS_PK on USERS (
ID_USER
);

/*==============================================================*/
/* Index: RELATIONSHIP_1_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_1_FK on USERS (
ID_DOC
);

alter table ARTWORK_ARTIST
   add constraint FK_ARTWORK__RELATIONS_ARTIST foreign key (ID_ARTIST_FK)
      references ARTIST (ID_ARTIST)
      on delete restrict on update restrict;

alter table ARTWORK_ARTIST
   add constraint FK_ARTWORK__RELATIONS_ARTWORK foreign key (ID_ARTWORK_FK)
      references ARTWORK (ID_ARTWORK)
      on delete restrict on update restrict;

alter table ARTWORK_TECHNIC
   add constraint FK_ARTWORK__RELATIONS_ARTWORK foreign key (ID_ARTWORK_FK)
      references ARTWORK (ID_ARTWORK)
      on delete restrict on update restrict;

alter table ARTWORK_TECHNIC
   add constraint FK_ARTWORK__RELATIONS_ARTISTIC foreign key (ID_AT_FK)
      references ARTISTIC_TECHNIC (ID_AT)
      on delete restrict on update restrict;

alter table IDEAS
   add constraint FK_IDEAS_RELATIONS_USERS foreign key (ID_USER_IDFK)
      references USERS (ID_USER)
      on delete restrict on update restrict;

alter table IDEAS
   add constraint FK_IDEAS_RELATIONS_CATEGORY foreign key (ID_CATEGORY_IDFK)
      references CATEGORY (ID_CATEGORY)
      on delete restrict on update restrict;

alter table MESSAGE
   add constraint FK_MESSAGE_RELATIONS_ARTIST foreign key (ID_ARTIST_MESS_FK)
      references ARTIST (ID_ARTIST)
      on delete restrict on update restrict;

alter table MESSAGE
   add constraint FK_MESSAGE_RELATIONS_USERS foreign key (ID_USER_MESS_FK)
      references USERS (ID_USER)
      on delete restrict on update restrict;

alter table RATING
   add constraint FK_RATING_RELATIONS_USERS foreign key (ID_USER)
      references USERS (ID_USER)
      on delete restrict on update restrict;

alter table RATING
   add constraint FK_RATING_RELATIONS_ARTWORK foreign key (ID_ARTWORK)
      references ARTWORK (ID_ARTWORK)
      on delete restrict on update restrict;

alter table USERS
   add constraint FK_USERS_RELATIONS_DOCTYPE foreign key (ID_DOC)
      references DOCTYPE (ID_DOC)
      on delete restrict on update restrict;