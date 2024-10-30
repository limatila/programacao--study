/* Deleting duplicate rows! */

delete t1 FROM ESports /* using ESports as t1 */
t1 INNER  JOIN ESports t2 /* using ESports as second iteration */
WHERE	/* delete conditions */
    t1.idJogo > t2.idJogo AND	/* Higher 'idJogo' is deleted */
    t1.modalidade = t2.modalidade AND
    t1.timeSelecao = t2.timeSelecao AND
    t1.dataJogos = t2.dataJogos;