use AVON;
select * from INFORMATION_SCHEMA.tables;

DECLARE @aNumber as integer /* Declaring var */
SELECT @aNumber = 10	  /* Attributing/Initializing */
SELECT @aNumber as 'aNumber';
/* always execute together. Var will be lost after an execution */


DECLARE @vendorNumber as integer
SELECT @vendorNumber = (SELECT COUNT(*) from Vendedores)
select @vendorNumber as 'Vendor Number'; /* will present the number of entrys in the table */


DECLARE @bNumber as integer = 928 /* quick usage */
select @aNumber as 'número';

/* working calculations for integers! */
select @aNumber + @bNumber + (select SUM(valorVenda) from Vendas) as 'Sum a + b numbers + (soma vendas totais)'
-- arithmetic operators include: +, -, *, /, % 


/* String concatenation */
select CONCAT('this ', 'is ', 'concatenated') as 'Concatenated string';

DECLARE @aString as varchar(50) = 'Jhon';
SELECT @aString = CONCAT(@aString, ' is awesome!'); /* same as common langs, can bring the first reference to modify itself */
select @aString as 'My string';