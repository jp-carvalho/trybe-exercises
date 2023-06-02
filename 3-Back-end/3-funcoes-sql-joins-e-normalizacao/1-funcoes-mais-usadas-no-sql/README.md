<!-- Para fixar
Agora, vamos fixar os aprendizados com alguns desafios: -->

<!-- Faça uma query que exiba a palavra 'trybe' em CAIXA ALTA. -->
SELECT UCASE('trybe');


<!-- Faça uma query que transforme a frase 'A Internet mudou o mundo' em 'A IA mudou o mundo'. -->
SELECT REPLACE('A Internet mudou o mundo', 'Internet', 'IA');

<!-- Utilizando uma query, encontre quantos caracteres temos em 'Uma frase qualquer'. -->
SELECT LENGTH('Uma frase qualquer');

<!-- Extraia e retorne apenas a palavra “JavaScript” da frase 'A linguagem JavaScript está entre as mais usadas'. -->
SELECT SUBSTRING('A linguagem JavaScript está entre as mais usadas', 13, 10);

<!-- Por fim, padronize a string 'RUA NORTE 1500, RIO DE JANEIRO, BRASIL' para que suas informações estejam todas em caixa baixa. -->
SELECT LCASE('RUA NORTE 1500, RIO DE JANEIRO, BRASIL');


<!-- Usando o IF na tabela sakila.film, exiba o id do filme, o título e uma coluna extra chamada ‘filme visto?’, em que deve-se avaliar se o nome do filme é ‘ACE GOLDFINGER‘. Caso seja, exiba “OK”. Caso contrário, exiba “FALTA ASSISTIR”. Não esqueça de usar um alias para renomear a coluna da condicional. -->
SELECT film_id, title, IF (title = 'ACE GOLDFINGER', 'OK', 'FALTA ASSISTIR') AS 'filme visto?'
FROM sakila.film;


<!-- Usando o CASE na tabela sakila.film, exiba o título, a classificação indicativa (rating) e uma coluna extra que vamos chamar de ‘grupo-alvo’ em que colocaremos a classificação do filme de acordo com as seguintes siglas:
G: “Livre para todas as idades”;
PG: “Maiores de 10 anos”;
PG-13: “Maiores de 13 anos”;
R: “Maiores de 17 anos”;
Se não cair em nenhuma das classificações anteriores: “Proibido para menores de idade”. -->

SELECT title, rating,
	CASE 
		WHEN rating = 'G' THEN 'Livre para todas as idades'
		WHEN rating = 'PG' THEN 'Maiores de 10 anos'
    WHEN rating = 'PG-13' THEN 'Maiores de 13 anos'
    WHEN rating = 'R' THEN 'Maiores de 17 anos'
		ELSE 'Proibido para menores de idade'
  END AS 'grupo-alvo'
FROM sakila.film;

<!-- Monte uma query usando o MOD juntamente com o IF para descobrir se o valor 15 é par ou ímpar. Chame essa coluna de ‘Par ou Ímpar’, onde ela pode dizer ‘Par’ ou ‘Ímpar’. -->
SELECT IF ( 15 MOD 2 = 0, 'PAR', 'IMPAR');


<!-- Temos uma sala de cinema que comporta 220 pessoas. Quantos grupos completos de 12 pessoas podemos levar ao cinema sem que ninguém fique de fora? -->
SELECT 220 DIV 12;
//18

<!-- Utilizando o resultado anterior, responda à seguinte pergunta: temos lugares sobrando? Se sim, quantos? -->
SELECT IF(220 MOD 12 = 0, 'NÃO', CONCAT('SIM, ', 220 MOD 12));
//SIM, 4


<!-- Monte uma query que gere um valor entre 15 e 20. -->
SELECT ROUND(15 + (RAND() * 5))

<!-- Monte uma query que exiba o valor arredondado de 15.7515971 com uma precisão de 5 casas decimais. -->
SELECT ROUND(15.7515971, 5);

<!-- Estamos com uma média de 39.494 de vendas de camisas por mês. Qual é o valor aproximado para baixo dessa média? -->
SELECT FLOOR(39.494);

<!-- Temos uma taxa de inscrição de 85.234% no curso de fotografia para iniciantes. Qual é o valor aproximado para cima dessa média? -->
SELECT CEIL(85.234);

<!-- Monte uma query que exiba a diferença de dias entre '2030-01-20' e hoje. -->
SELECT DATEDIFF('2030-01-20', NOW());

<!-- Monte uma query exiba a diferença de horas entre '10:25:45' e '11:00:00'. -->
SELECT TIMEDIFF('10:25:45', '11:00:00');

<!-- Monte um query que exiba:
A média de duração dos filmes e dê o nome da coluna de ‘Media de Duracao’;
A duração mínima dos filmes como ‘Duracao Minima’;
A duração máxima dos filmes como ‘Duracao Maxima’;
A soma de todas as durações como ‘Tempo de Exibicao Total’;
E, finalmente, a quantidade total de filmes cadastrados na tabela sakila.film como ‘Filmes Registrados’. -->
SELECT AVG(length) AS 'Media de Duração',
	MIN(length) AS 'Duração Mínima',
	MAX(length) AS 'Duração Máxima',
	SUM(length) AS 'Tempo de Exibição Total',
	COUNT(*) AS 'Filmes Registrados' 
FROM sakila.film;

<!-- Monte uma query que exiba a quantidade de clientes cadastrados na tabela sakila.customer que estão ativos e a quantidade que estão inativos. -->
SELECT active, COUNT(*) FROM sakila.customer
	GROUP BY active;

<!-- Monte uma query para a tabela sakila.customer que exiba a quantidade de clientes ativos e inativos por loja. Os resultados devem conter o ID da loja, o status dos clientes (ativos ou inativos) e a quantidade de clientes por status. -->
SELECT store_id, active, COUNT(*) FROM sakila.customer
	GROUP BY store_id, active
  ORDER BY store_id, active;


<!-- Monte uma query que exiba a média de duração de locação por classificação indicativa (rating) dos filmes cadastrados na tabela sakila.film. Os resultados devem ser agrupados pela classificação indicativa e ordenados da maior média para a menor. -->
SELECT AVG(rental_duration) AS avg_rental_duration, rating FROM sakila.film
	GROUP BY rating
  ORDER BY avg_rental_duration DESC;


<!-- Monte uma query para a tabela sakila.address que exiba o nome do distrito e a quantidade de endereços registrados nele. Os resultados devem ser ordenados da maior quantidade para a menor. -->
SELECT district, COUNT(*) FROM sakila.address
	GROUP BY district
  ORDER BY COUNT(*) DESC;


<!-- Usando a query a seguir, modifique-a de forma que exiba apenas as durações médias que estão entre 115.0 a 121.50. Além disso, dê um alias (apelido) à coluna gerada por AVG(length), de forma que deixe a query mais legível. Finalize ordenando os resultados de forma decrescente. -->

<!-- SELECT rating, AVG(length) -->
<!-- FROM sakila.film -->
<!-- GROUP BY rating; -->
SELECT rating, AVG(length) AS duração_media
FROM sakila.film
GROUP BY rating
HAVING AVG(length) BETWEEN 115.0 AND 121.50
ORDER BY duração_media DESC;



<!-- Usando a query a seguir, exiba apenas os valores de total do custo de substituição que estão acima de $3950.50. Dê um alias que faça sentido para SUM(replacement_cost), de forma que deixe a query mais legível. Finalize ordenando os resultados de forma crescente. -->

<!-- SELECT rating, SUM(replacement_cost) -->
<!-- FROM sakila.film -->
<!-- GROUP by rating; -->
SELECT rating, SUM(replacement_cost) AS cost
FROM sakila.film
GROUP by rating
HAVING cost > 3950.50
ORDER BY cost;
