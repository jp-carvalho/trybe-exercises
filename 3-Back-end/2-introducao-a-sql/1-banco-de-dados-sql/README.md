<!-- Vamos treinar!
Usando os comandos que você acabou de aprender, resolva os seguintes desafios:

Crie o container MYSQL: -->

docker container run --name container-mysql -e MYSQL_ROOT_PASSWORD=senha-mysql -d -p 3306:3306 mysql:8.0.31

<!-- Entre no banco de dados mysql. -->

 mysql -u root -p

<!-- Visualize todas as tabelas desse banco. -->

 USE nome_do_banco_de_dados_aqui;
 SHOW TABLES;

<!-- Visualize a estrutura de pelo menos 10 tabelas diferentes e tente entender o tipo de estrutura que costuma ser utilizada. -->

 DESCRIBE nome_da_tabela;

<!-- Crie um novo banco de dados com o seu nome e depois entre nele! -->

 CREATE DATABASE seu_nome_aqui;
 USE seu_nome_aqui;

<!-- Pronto! Agora você pode executar comandos SQL dentro do seu banco de dados sem usar a interface gráfica, o que pode ser útil em alguns cenários em que você não tem acesso ao MySQL Workbench. -->


<!-- EXERCICIOS DIA -->

<!-- Agora vamos abrir o Workbench e fazer uma análise prática do banco de dados sakila, que já deve estar instalado, caso você tenha feito a instalação do MySql Workbench de forma padrão. Caso o banco sakila não esteja disponível, volte até a seção Restaurando o banco de dados de prática sakila e siga as instruções listadas. Com esse banco disponível na sua instalação do Workbench, sua missão agora é tentar finalizar os exercícios a seguir! -->

<!-- Exercício 1: Descubra como fazer uma pesquisa em qualquer tabela sem utilizar uma linha de código usando o MySql Workbench. -->

Basta clicar com botão direito na tabela e clicar em “select rows - limit 200” O limite vai depender da configuração do workbench.

<!-- Exercício 2: Descubra como é possível criar uma tabela sem usar código SQL usando o MySql Workbench. -->

Na barra lateral esquerda, clicar em tables com o botão direito e em seguida clicar em Create Table

<!-- Exercício 3: Feito isso, crie uma tabela com as seguintes restrições: -->

<!-- Nome da tabela: filme -->

<!-- Colunas: -->

<!-- filme_id - primary key, tipo int, incrementa por 1 cada vez que um valor é inserido automaticamente; -->
<!-- descricao - não permite nulos, tipo texto (varchar(100)); -->
<!-- ano_lancamento - não permite nulos, tipo int; -->
<!-- nota - permite nulos, tipo int; -->

imagem na pasta

<!-- Exercício 4: Analise a tabela city e encontre a tabela à qual a coluna country_id faz referência. -->

Ela faz referência à tabela country.

<!-- Exercício 5: Após resolver o exercício anterior, responda: qual tipo de relacionamento a tabela city faz com a tabela country? -->

N:1

<!-- Exercício 6: Qual tipo de relacionamento a tabela country faz com a tabela city? -->

1:N

<!-- Exercício 7: Abra tabela por tabela do banco sakila e encontre no mínimo 3 exemplos de um relacionamentos 1:N ou N:1. -->

store -> staff
country -> city
film -> language