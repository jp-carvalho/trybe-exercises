<!-- Qual é o resultado de 13 * 8 ? Descubra usando apenas o SELECT; -->

SELECT 13*8;

<!-- Monte uma query que exiba a data e hora atuais. Dê a essa coluna o nome “Data Atual”. -->

SELECT now() AS 'Data Atual';

<!-- Vamos agora entrar no banco de dados sakila e encontrar as seguintes informações, montando uma query para cada uma: -->

<!-- Escreva uma query que selecione todos os registros da tabela city; -->

SELECT * FROM sakila.city;

<!-- Escreva uma query que exiba apenas os registros das colunas first_name e last_name da tabela customer; -->

SELECT first_name, last_name FROM sakila.customer;

<!-- Escreva uma query que exiba todos os registros da tabela rental; -->

SELECT * FROM sakila.rental;

<!-- Escreva uma query que exiba o título, a descrição e a data de lançamento dos filmes registrados na tabela film; -->

SELECT title, description, release_year FROM sakila.film;

<!-- Utilize o SELECT para explorar todas as tabelas do banco de dados. -->

SELECT * FROM sakila.nome_da_tabela;

<!-- Na tabela sakila.film, monte uma query que exiba o título e o ano de lançamento dos filmes em uma coluna e dê a ela o nome Lançamento do Filme. -->

SELECT CONCAT(title, ' - ', release_year) AS 'Lançamento do Filme' FROM sakila.film;

<!-- Na tabela sakila.address, monte uma query que exiba a rua e o distrito de cada registro em uma coluna apenas, e dê a essa coluna o nome Endereço. -->

SELECT CONCAT(address, ' - ', district) AS Endereço FROM saklila.address;


<!-- Para criá-la no seu banco de dados, abra uma nova janela de query no MySQL Workbench e execute o seguinte código:

Copiar
CREATE DATABASE `Escola`;
CREATE TABLE IF NOT EXISTS Escola.Estudantes (
    `Nome` VARCHAR(7) CHARACTER SET utf8,
    `Idade` INT
);
INSERT INTO Escola.Estudantes VALUES
    ('Rafael', 25),
    ('Amanda', 30),
    ('Roberto', 45),
    ('Carol', 19),
    ('Amanda', 25);
Feito isso, você terá acesso à tabela Estudantes do banco de dados Escola. Levando em conta a explicação que você acabou de ver, como você montaria uma query para encontrar os seguintes dados? -->

<!-- Monte uma query para encontrar pares únicos de nomes e idades. -->

SELECT DISTINCT Nome, Idade FROM Escola.Estudantes;

<!-- Quantas linhas você encontraria na query anterior? -->

5

<!-- Monte uma query para encontrar somente os nomes únicos. -->

SELECT DISTINCT Nome FROM Escola.Estudantes;

<!-- Quantas linhas você encontraria na query anterior? -->

4

<!-- Monte uma query para encontrar somente as idades únicas. -->

SELECT DISTINCT Idade FROM Escola.Estudantes;

<!-- Quantas linhas você encontraria na query anterior? -->

4

<!-- Essa é a tabela staff do banco de dados sakila. Como você poderia responder às seguintes questões? -->

<!-- Quantas senhas temos cadastradas nessa tabela? -->

1

<!-- Quantas pessoas temos no total trabalhando para nossa empresa? -->

2

<!-- Juntando tudo que vimos hoje
No conteúdo do dia, aprendemos que:

Para fazer pesquisas e retornar dados do banco, utilizamos o SELECT.
Para juntar (concatenar) duas ou mais colunas, utilizamos o CONCAT.
Para evitar dados repetidos em nossas queries, utilizamos o DISTINCT.
Para contar todos os dados retornados, usamos o COUNT.
Com o LIMIT e o OFFSET, podemos especificar quantos e quais serão os valores retornados.
E para ordenar nossos dados de maneira crescente ou decrescente, utilizamos o comando ORDER BY.
Bônus: Exercícios para fixar
Agora é a sua vez! Vamos juntar tudo isso na prática usando a tabela sakila.film: -->

<!-- Escreva uma query que exiba todos os filmes cadastrados no banco de dados. -->

SELECT * FROM sakila.film;

<!-- Escreva uma query que exiba apenas o nome dos filmes, seu ano de lançamento e sua classificação. -->

SELECT title, release_year, rating FROM sakila.film;

<!-- Quantos filmes temos cadastrados? -->

SELECT COUNT(title) FROM sakila.film;
1000

<!-- Para os exercícios a seguir, vamos usar a tabela sakila.actor: -->

<!-- Escreva uma query que exiba apenas os sobrenomes únicos cadastrados. -->

SELECT DISTINCT last_name FROM sakila.actor;

<!-- Quantos sobrenomes únicos temos na tabela? -->

SELECT COUNT(DISTINCT last_name) FROM sakila.actor;
121

<!-- Ordene os valores na tabela em ordem crescente de sobrenomes e em ordem decrescente de nome. -->

ORDER BY  last_name, first_name DESC;

<!-- Usando a tabela language: -->

<!-- Crie uma pesquisa que mostre os 5 idiomas cadastrados, mas não mostre o idioma english. -->

SELECT * FROM sakila.language LIMIT 10 OFFSET 1;

<!-- Usando a tabela film: -->

<!-- Selecione todos os dados da tabela. Pronto, fez isso? 1.1 Agora vamos tentar fazer o seguinte: Crie uma query para encontrar os 20 primeiros filmes, incluindo o título, o ano de lançamento, a duração, a classificação indicativa e o custo de substituição. Ordene os resultados pelos filmes com a maior duração e depois pelo menor custo de substituição. -->

SELECT * FROM sakila.film;
SELECT title, release_year, length, rating, replacement_cost FROM sakila.film
ORDER BY length DESC, replacement_cost ASC
LIMIT 20;
