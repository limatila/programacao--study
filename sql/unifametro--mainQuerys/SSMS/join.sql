create database AVON;
use AVON;

create table Vendedores(
	idVendedor int primary key identity, /* = auto_increment */
	nomeVendedor varchar(40) NOT NULL
);

create table Vendas(
	idVenda int primary key identity,
	dataVenda datetime,
	valorVenda DECIMAL(8,2) NOT NULL,
	comicao int,
	idVendedorF int FOREIGN KEY (idVendedorF) references Vendedores (idVendedor) NOT NULL
);

select * from Vendedores;

drop table Vendedores;

insert into Vendedores (nomeVendedor) values
('gabriel'),
('daniel'),
('marques');

insert into Vendas(dataVenda, valorVenda, comicao, idVendedorF) values
( GETDATE(), 4023.50, 20, 1),
( GETDATE(), 3500.00, 35, 3),
( GETDATE(), 1520.00, 15, 2),
( GETDATE(), 5005.69, 25, 1),
( GETDATE(), 4023.50, 20, 4); /* o id referenciado não pode "não existir" nos Vendedores*/ 

select * from Vendas;


/* Inner Join */
select idVendedor, nomeVendedor, idVenda, valorVenda
from Vendas INNER JOIN Vendedores on Vendedores.idVendedor = Vendas.idVendedorF; 
/* from object1 (join_type) object2 where object1.attr1PK = object2.attr2FK */


SET IDENTITY_INSERT Vendedores OFF;
insert into Vendedores (nomeVendedor) values
('luan'),
('biel');


/* Left Join */
select idVendedor, nomeVendedor, idVenda
from 
	Vendas LEFT JOIN Vendedores on Vendedores.idVendedor = Vendas.idVendedorF
ORDER BY 
	Vendas.idVendedorF;


/* Right Join */
select idVendedor, nomeVendedor, idVenda
from Vendas 
	RIGHT JOIN Vendedores on Vendedores.idVendedor = Vendas.idVendedorF; 


/* Complete Comission Calculus */
