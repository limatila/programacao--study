/* constraints are properties of an attribute that delimit the pattern of their values */
use Youtube;

create table Videos (
	urlVideo varchar(40) primary key unique,
    id integer(16) unique,
    constraint FK_idAutor foreign key (idUser) references Users (idUser)
);