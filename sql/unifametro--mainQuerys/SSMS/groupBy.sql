create database People;
use People;

create table Adults(
	id int primary key identity,
	height float,
	age smallint,
	profession varchar(30) /* at the moment: teacher, medic, systems analyst. */
);

insert into Adults(height, age, profession) values
(1.54, 19, 'teacher'),
(1.68, 21, 'medic'),
(1.78, 19, 'systems analyst'),
(1.58, 21, 'systems analyst'),
(1.56, 18, 'teacher'),
(1.87, 24, 'medic'),
(1.80, 21, 'systems analyst'),
(1.64, 27, 'teacher'),
(1.73, 32, 'medic');

drop table Adults;

create table Kids(
	id int primary key identity,
	height float,
	age smallint,
	studies bit
);

insert into Kids(height, age, studies) values
(1.30, 5, 1),
(1.60, 13, 0),
(1.50, 11, 0),
(1.10, 5, 1),
(1.35, 10, 1),
(1.60, 17, 1),
(1.50, 12, 0),
(1.10, 11, 1),
(0.70, 2, 0),
(0.90, 3, 1);

select * from Adults;

/* agregated functions includes: min, max, sum, avg, count, and more */
/* or the GROUP BY itself: */
select 
	AVG(height) as 'Altura M�dia', /* agregated columns do not need to be specified in the group by */
	count(studies) as Contagem,
	studies as 'Estuda Atualmente' 
from 
	Kids
group by 
	studies;


/* HAVING: specifying agregated lines */
select 
	CONVERT(decimal(3,2), AVG(age)) as 'Idade M�dia', /* PORQUE N�O EST� MOSTRANDO 9,5? */
	case when studies=0 then 'N�o' /* using conditional to format the content returned */
		 when studies=1 then 'Sim' 
		 END as 'Estuda Atualmente'
from 
	Kids
group by
	studies
having
	studies = 0; /* will show only the average student age */


select
	AVG(height) as 'Altura M�dia',
	profession as 'Profiss�o'
from
	Adults
group by
	profession,
	age /* needs to be specified, because it's being used in Having clause */
having
	age >= 24;

