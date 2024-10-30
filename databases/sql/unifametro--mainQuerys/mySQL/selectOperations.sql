create database school;
use school;

create table estudantes(
	id integer primary key auto_increment,
	nome varchar(40),
    matricula integer(6) unique,
	ativo boolean,
    dataIncluido date,
    dataConcluido date
);

create table professores(
	id integer primary key auto_increment not null,
	nome varchar(40) not null,
    ativo boolean not null
);

/*
create table disciplinas(
	idDisciplina integer primary key unique auto_increment,
    nome varchar(20) unique,
    ativo boolean
);
*/

insert into estudantes(nome, matricula, dataIncluido, dataConcluido) values 
("deftonerson da silva", 202306, "2023-01-01", "2026-03-16"),
("Bonácio Zurkan", 202305, "2022-01-01", "2026-12-01"),
("Lucas Cavalcante", 202204, "2022-01-01", "2025-12-01");

insert into professores(nome, ativo) values
("Marcos Fontes", true),
("Belmondo", true),
("Waldejares", true);


set SQL_SAFE_UPDATES = 0;
select * from estudantes;


/* WHERE delimiter */ 
select nome, matricula from estudantes
where EXTRACT(year from dataIncluido) < 2023;

delete from estudantes
WHERE matricula = 202202; 


/* ORDER BY sorting */
select nome, id from estudantes
ORDER BY nome;

select nome, id from estudantes
where id >= 30
ORDER BY id DESC; /* showing the newest from id 30 */


/* GROUP BY  */
select COUNT(id) as nomesTotais, nome as Nome from estudantes /* 'as' presents the attribute in the desired name */
group by nome;
/* will count duplicate names */


/* HAVING delimiter */
