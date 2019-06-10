INSERT INTO controle_itemdesenvolvimento (concluido)
SELECT  SUM((TR.participacao*TR.status)/100)
	FROM controle_tarefas TR
	LEFT JOIN controle_itemdesenvolvimento IT ON TR.itdes_id = IT.id
	GROUP BY IT.id;