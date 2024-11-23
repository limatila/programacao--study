-- Active: 1732392411540@@127.0.0.1@6666@estudoDB
/* DDL */
CREATE TABLE IF NOT EXISTS materias (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    dataCriacao DATE
);

CREATE VIEW materia1 AS (
    SELECT * FROM materias
    WHERE nome = 'Java'
)

/* DML */
ALTER TABLE materias ADD FK_idProfessor INTEGER;

INSERT INTO materias (nome, dataCriacao) VALUES
('Java', '2024-12-23');

UPDATE materias
SET fk_idProfessor = NULL
WHERE id = 4

DELETE FROM materias
WHERE id = 6

/* DQL */
SELECT * FROM materias
WHERE 
    extract(year from dataCriacao) = '2024' 
    AND NOT 
    extract(month from dataCriacao) = '11';

SELECT dado1 FROM (
    SELECT nome "dado1", dataCriacao FROM materias
) AS "Query";

SELECT * FROM materias
ORDER BY id DESC
LIMIT 1;

/* COUNT SUM MAX MIN AVG */
CREATE VIEW essaView AS (SELECT 
        extract(month from dataCriacao) AS "Mês", COUNT(id) AS "materias" 
    FROM 
        materias
    GROUP BY 
        "Mês"
    HAVING
        extract(month from dataCriacao) = 12
)

/* número de matérias criadas, agrupadas por mês de criação tendo que eu só quero ver o mês 12 */


CREATE VIEW essaView AS (
SELECT 
    EXTRACT(MONTH FROM dataCriacao) AS "Mês", 
    COUNT(id) AS "Quantidade"
FROM 
    materias
WHERE
    materias != 'Java'
GROUP BY 
    EXTRACT(MONTH FROM dataCriacao)
HAVING
    EXTRACT(MONTH FROM dataCriacao) IN (11, 12))
/* !Consulta à fazer acima! */

/* Modelo de Views: CREATE VIEW nomeView AS (select) */
