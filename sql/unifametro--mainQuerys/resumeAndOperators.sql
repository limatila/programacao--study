/* logical: AND OR NOT */
/* relational: =, <, >, <=, >=, != <> */

create database TVprogramation;
use TVprogram;

create table ESports(
    idJogo primary key integer(8) auto_increment NOT NULL, /* will auto increment, no need to fill */
    modalidade varchar(25),
    timeSelecao varchar (20) NULL,
    dataJogos datetime
)

insert into ESports (modalidade, timeSelecao, dataJogos) values
("CS", "MIBR", "2023-10-11"),
("LOL", "LOUD", "2022-11-05"),
("CS", "FURIA", "2023-05-17"),
("PES", "BIEL", "2023-07-28"),
("LOL", "INTZ", "2024-08-30");


/* DDL */
select * from ESports;

select timeSelecao 
from ESports
where modalidade = "CS";

select modalidade from ESports
where EXTRACT(year from dataJogos) >= "2023"; /* selecting the "year" part of the datetime attributed */

select dataJogos from ESports
where EXTRACT(year from dataJogos) <= "2023" AND modalidade = "PES"; 


/* deletes (DML) */
set SQL_SAFE_UPDATES = 0; /* desables feature that impossibilitates deleting records without specifying a key */

delete * from ESports 
where dataJogos >= "2024-08-29";



/* like param. in select */
select * from ESports
where timeSelecao like "FU"; /* tudo que comece com 'FU' */

select dataJogos from ESports
where timeSelecao like "%el%"; /* os records imediatamente antes e depois do encontrado */



/* grab formatted date in select */
select date_format(dataJogos, "%d/%m/%Y") from ESports