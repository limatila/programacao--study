CREATE TABLE Professores (
	PK_idProfessor SERIAL PRIMARY KEY,
	nome VARCHAR NOT NULL,
	CPF VARCHAR NOT NULL UNIQUE
);

ALTER TABLE Materias ADD CONSTRAINT (FK_idProfessor) REFERENCES Professores.PK_idProfessor;