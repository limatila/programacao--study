SELECT R."idPage", R."titleReceita", U."first_name"
FROM "Receitas_receita" as R
INNER JOIN "auth_user" as U on r."userSubmitted_id" = U.id;