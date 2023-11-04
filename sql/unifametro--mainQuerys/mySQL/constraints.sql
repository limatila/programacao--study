/* constraints are properties of an attribute that delimit the pattern of their values */
use Youtube;

create table Videos (
    id integer(16) unique primary key,
    urlVideo varchar(40) unique not null,
    FK_idAutor integer FOREIGN KEY (idUser) references Users (idUser),
    datePublication datetime not null 
    constraint datePublication default getData() /* if the date is not inserted, define the current date to it. */
);