drop database if exists air;
create database air;
use air;
drop table if exists user;
drop table if exists identity;
drop table if exists case;
drop table if exists catalog;

/*==============================================================*/
/* Table: user 用户表                                           */
/*==============================================================*/
create table user
(
   id                   int not null auto_increment,
   username             varchar(20),
   password             varchar(20),
   primary key (id)
);
/*==============================================================*/
/* Table: identity 身份表                                       */
/*==============================================================*/
create table identity
(
   id                   int not null auto_increment,
   name             	varchar(20),
   primary key (id)
);
/*==============================================================*/
/* Table: identity 案例表                                       */
/*==============================================================*/
create table case
(
	id					int not null auto_increment,
	path                varchar(20),
	cid                 int,
	primary key (id)
);
/*==============================================================*/
/* Table: catalog 目录表                                        */
/*==============================================================*/
create table catalog
(
   id                   int not null auto_increment,
   title                varchar(20),
   iid					int,
   pid                  int,
   primary key (id)
);

/* 分类关联父分类外键 */
alter table catalog add constraint FK_Reference_1 foreign key (pid) references catalog (id) on delete restrict on update restrict;
/* 分类关联身份外键 */
alter table catalog add constraint FK_Reference_2 foreign key (iid) references identity (id) on delete restrict on update restrict;
/* 案例关联分类外键 */
alter table case add constraint FK_Reference_3 foreign key (cid) references catalog (id) on delete restrict on update restrict;

/* 用户 */
insert into user(username,password) values('admin','admin');

insert into identity(name) values('运输公司');
insert into identity(name) values('被侵权人');
insert into identity(name) values('物权人');
insert into identity(name) values('保险公司');
insert into identity(name) values('旅客');

/* ID说明：五位数id = 一级分类编号（占1位） + 二级分类编号（占2位） + 三级分类编号（占2位） */
/* 一级分类，根据身份id确定 */
insert into catalog(id,title,iid) values(10000,'航空货物运输合同纠纷',1);
insert into catalog(id,title,iid) values(20000,'人身、财产侵权责任',2);
insert into catalog(id,title,iid) values(30000,'物权纠纷',3);
insert into catalog(id,title,iid) values(40000,'保险纠纷',4);
insert into catalog(id,title,iid) values(50000,'航空旅客运输合同',5);
/* 二级分类，根据一级分类id确定 */
insert into catalog(id,title,pid) values(10100,'程序',10000);
insert into catalog(id,title,pid) values(10200,'货物运输证据',10000);
insert into catalog(id,title,pid) values(10300,'法院判决表述',10000);
insert into catalog(id,title,pid) values(10400,'争议事由',10000);
insert into catalog(id,title,pid) values(10500,'责任主体',10000);
insert into catalog(id,title,pid) values(10600,'赔偿范围',10000);
insert into catalog(id,title,pid) values(10700,'赔偿数额',10000);
insert into catalog(id,title,pid) values(10800,'法律法规',10000);
insert into catalog(id,title,pid) values(10900,'法院判决',10000);
insert into catalog(id,title,pid) values(20100,'责任主体',20000);
insert into catalog(id,title,pid) values(20200,'事由',20000);
insert into catalog(id,title,pid) values(20300,'赔偿范围',20000);
insert into catalog(id,title,pid) values(20400,'法律法规',20000);
insert into catalog(id,title,pid) values(20500,'证据',20000);
insert into catalog(id,title,pid) values(30100,'赔偿数额（法院）',30000);
insert into catalog(id,title,pid) values(30200,'证据',30000);
insert into catalog(id,title,pid) values(30300,'引用法律法规（不用具体条文）',30000);
insert into catalog(id,title,pid) values(30400,'责任主体',30000);
insert into catalog(id,title,pid) values(30100,'争议事由',30000);
insert into catalog(id,title,pid) values(30200,'赔偿范围',30000);
insert into catalog(id,title,pid) values(40100,'证据',40000);
insert into catalog(id,title,pid) values(40200,'适用法律',40000);
insert into catalog(id,title,pid) values(40300,'程序',40000);
insert into catalog(id,title,pid) values(40400,'责任主体',40000);
insert into catalog(id,title,pid) values(40500,'争议事由',40000);
insert into catalog(id,title,pid) values(40600,'赔偿范围',40000);
insert into catalog(id,title,pid) values(40700,'赔偿数额',40000);
insert into catalog(id,title,pid) values(50100,'赔偿范围',50000);
insert into catalog(id,title,pid) values(50200,'证据',50000);
insert into catalog(id,title,pid) values(50300,'争议事由',50000);
insert into catalog(id,title,pid) values(50400,'责任主体',50000);
insert into catalog(id,title,pid) values(50500,'法律法规',50000);
insert into catalog(id,title,pid) values(50600,'赔偿数额（法院）',50000);
insert into catalog(id,title,pid) values(50700,'程序问题',50000);
/* 三级分类，根据二级分类id确定 */
insert into catalog(id,title,pid) values(10101,'缺席审理',10100);
insert into catalog(id,title,pid) values(10102,'反诉',10100);
insert into catalog(id,title,pid) values(10103,'调解',10100);
insert into catalog(id,title,pid) values(10104,'小额诉讼程序',10100);
insert into catalog(id,title,pid) values(10105,'再审',10100);
insert into catalog(id,title,pid) values(10106,'二审（上诉）',10100);
insert into catalog(id,title,pid) values(10107,'管辖权异议',10100);
insert into catalog(id,title,pid) values(10108,'简易程序',10100);
insert into catalog(id,title,pid) values(10109,'普通程序',10100);
insert into catalog(id,title,pid) values(10201,'财产损失报告',10200);
insert into catalog(id,title,pid) values(10202,'信用证',10200);
insert into catalog(id,title,pid) values(10203,'保函',10200);
insert into catalog(id,title,pid) values(10204,'价单',10200);
insert into catalog(id,title,pid) values(10205,'提货单',10200);
insert into catalog(id,title,pid) values(10206,'快递（单）',10200);
insert into catalog(id,title,pid) values(10207,'提单',10200);
insert into catalog(id,title,pid) values(10208,'清单',10200);
insert into catalog(id,title,pid) values(10209,'运单（书）',10200);
insert into catalog(id,title,pid) values(10210,'账单',10200);
insert into catalog(id,title,pid) values(10211,'货物受理票',10200);
insert into catalog(id,title,pid) values(10212,'单据',10200);
insert into catalog(id,title,pid) values(10213,'收据',10200);
insert into catalog(id,title,pid) values(10214,'照片',10200);
