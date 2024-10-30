create database Youtube;
use Youtube;

create table Users(
	idUser integer primary key unique,
	nomeUser varchar(15),
	email varchar(30) not null,
	senha integer not null,
	descricao varchar(80),
	localConexao varchar(20)
);

select * from Users;