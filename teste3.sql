SELECT  IT.nome_item, TR.nome_tarefa, TR.participacao, TR.status, SUM((TR.participacao*TR.status)/100)
	AS IT_concluido
	FROM controle_tarefas TR
	LEFT JOIN controle_itemdesenvolvimento IT ON TR.itdes_id = IT.id
	GROUP BY IT.id;