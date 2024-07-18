/* Procedures and Functions are ways to apply repeated SQL commands */
/* Will store specific commands and execute when called */ 
/* Created to support various applications in different programming languages */ 

use AVON;
SELECT * FROM INFORMATION_SCHEMA.tables;


/* Procedures: Complete operations and transactions. Will not be able to declare vars */
CREATE PROCEDURE aumentaUnidade AS
	BEGIN
		select 'doing something';
	END
aumentaUnidade();

/* Functions: Small operations, daily commands */ 
CREATE FUNCTION selectTable(table1 varchar)
DECLARE	/* declare vars */
	@table1 as varchar(20)
BEGIN /* beginning operation */
	select * from table1;
END;
$$ LANGUAGE SQL; /* specify which language will use this */

SELECT selectTable('Vendedores'); --Calling a func

create function diminuiUnidade(val integer)
RETURNS integer AS $$
	select val - 1;
$$ language SQL;	

select diminuiUnidade(20);