/* logical: AND, OR, NOT, LIKE, */
/* relational: =, <, >, <=, >=, != <> */

/* DDL */
create database TVprogramation;
use TVprogramation;

create table ESports(
    idJogo integer(8) primary key auto_increment NOT NULL, /* will auto increment, no need to fill */
    modalidade varchar(25),
    timeSelecao varchar (20) NULL,
    dataJogos datetime
);

insert into ESports (modalidade, timeSelecao, dataJogos) values
("FF", "LOUD", "2023-10-11 17:00"),
("Yugioh", "Riquelmix", "2022-11-05 13:00"),
("CS", "Fnatic", "2023-05-17 19:00"),
("FF", "Baki", "2023-07-28 09:00"),
("LOL", "PAIN", "2021-08-30 18:00");


/* DQL */
select * from ESports;

select timeSelecao, modalidade 
from ESports
where modalidade = "CS";

select modalidade, dataJogos from ESports
where EXTRACT(year from dataJogos) >= "2023"; /* selecting the "year" part of the datetime attributed */

select dataJogos, modalidade from ESports
where EXTRACT(year from dataJogos) <= "2023" AND modalidade = "PES"; 


/* deletes (DML) */
set SQL_SAFE_UPDATES = 0; /* desables feature that impossibilitates deleting records without specifying a key */
delete from ESports 
where dataJogos >= "2024-08-29";


/* like param. in DQL */
/* % sinaliza onde começa a semelhança. %FU procura quem termina em "FU", "A%" procura quem começa em "A". %ABC% procura das duas formas */
select * from ESports
where timeSelecao like "FU%"; /* tudo que comece com 'FU' */

select modalidade, idJogo from ESports
where modalidade like "%S"; /* tudo que termine com 'S' */

select * from ESports
where timeSelecao not like "%Z%"; /* tudo que NAO contenha 'Z' */ /*translate*/

/* grab formatted date in select */
select date_format(dataJogos, "%d/%m/%Y - ás %H:%i horas"), timeSelecao from ESports;