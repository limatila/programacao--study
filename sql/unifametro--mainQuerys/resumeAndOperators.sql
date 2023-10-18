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
("LOL", "ZAUNITAS", "2022-05-11 09:46"); /*
("Yugioh", "Riquelmix", "2022-11-05 13:00"),
("CS", "Fnatic", "2023-05-17 19:00"),
("FF", "Baki", "2025-07-28 09:00"),
("LOL", "PAIN", "2026-08-30 18:00");
*/

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
delete from ESports /* deleting too much future games */
where dataJogos >= "2024-08-29";

delete t1 FROM ESports t1 /* deleting */
INNER  JOIN ESports t2
WHERE
    t1.idJogo > t2.idJogo AND
    t1.modalidade = t2.modalidade AND
    t1.timeSelecao = t2.timeSelecao AND
    t1.dataJogos = t2.dataJogos;



/* like param. in DQL */
/* % sinalizes where the similiarities begin. %FU searchs who end in 'FU', "A%" searchs who begin in "A". "%ABC%" searchs in the 2 ways. */
select * from ESports
where timeSelecao like "FU%"; /* All that starts in 'FU' */

select modalidade, idJogo from ESports
where modalidade like "%S"; /* All that ends in 'S' */

select * from ESports
where timeSelecao not like "%Z%"; /* All that DOESN'T contain 'Z' */

/* grab formatted date in select */
select date_format(dataJogos, "%d/%m/%Y - ás %H:%i horas"), timeSelecao from ESports;

/* display ordered by date */
select date_format(dataJogos, "%d/%m/%Y"), timeSelecao from esports
order by EXTRACT(year from dataJogos);

/*! to test!*/
/* showing sum of all objects */
select COUNT(idJogo) from ESports;

/* selecting, grouping, and ordering decrescently */
select timeSelecao, max(dataJogos) from ESports
GROUP BY modalidade 
ORDER BY max(dataJogos) DESC;

/* showing average year of the matches */
select avg(EXTRACT(year from dataJogos)) from ESports;

/*  */
select idJogo, dataValidade from ESports
;

