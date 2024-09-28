use youtube;
show TABLES;

select * from users;

show columns from users;
alter table users
	modify column idUser integer auto_increment;

insert into users(nomeUser, email, senha, descricao, localConexao) values
('Andrew', 'andWeW@hotmail.com', 31904421, 'Anivia', 'Fortaleza-CE'),
('Gabu', 'chemicalGabi@gmail.com', 98899154, 'Psicologia', 'Fortaleza-CE'),
('Well', 'dodocaNauts@gmail.com', 13157, 'Nutrição', 'Fortaleza-CE'),
('Marcos', 'futa2501@gmail.com', 11004, 'Contábeis', 'Rio de Janeiro-RJ');

update users
set descricao = 'Nordeste'
where LOWER(localConexao) like 'fortaleza-ce';
