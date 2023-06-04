<!-- Exercício 1 🚀 : -->
<!-- Vamos aprimorar nossos conhecimentos sobre images e volumes, para isso: -->

<!-- 1 - Crie um arquivo HTML chamado missao_trybe.html que tenha a seguinte estrutura: -->

Tag <title> com o seguinte texto “Trybe”;
Tag <H1> com o seguinte texto “Missão da Trybe”;
Tag <p> com o seguinte texto “Gerar oportunidade para pessoas”;
Salve o arquivo em qualquer lugar da sua máquina com a extensão html
<!-- 2 - Crie um container para manter um servidor httpd:2.4.54 Apache e vincule sua porta interna com a porta 4545 da sua máquina local. -->

docker run -d --name site-trybe -p 4545:80 -v <caminho do arquivo html>:/usr/local/apache2/htdocs httpd:2.4.54

<!-- 3 - Após criar o container, acesse a página HTML que está rodando no servidor em seu browser. -->

http://localhost:4545/missao_trybe.html

<!-- 4 - Acesse o arquivo missao_trybe.html e acrescente a tag <p> com o seguinte texto: “Nosso negócio é GENTE! #VQV”; -->

<p>Nosso negócio é GENTE! #VQV</p>

<!-- 5 - Obtenha o id do container httpd:2.4.54; -->

docker ps -a

<!-- 6 - Obtenha o Mounts através da propriedade Source, que deve mostrar o volume desse container no Docker Host; -->

docker inspect <ID-DO-CONTAINER>

<!-- 7 - Agora pare o container httpd:2.4.54; -->

docker stop <ID-DO-CONTAINER>

<!-- 8 - Exclua o seu container; -->

docker rm -f <ID-DO-CONTAINER>

<!-- 9 - Verifique se a pasta onde você salvo o arquivo html permanece no mesmo lugar; -->

cd <ENDEREÇO-DA-PASTA>
ls -la

<!-- 10 - Obtenha o IMAGE ID do servidor; -->

docker images

<!-- 11 - Depois de obter o IMAGE ID, exclua a imagem. -->

docker image rmi -f <ID-DA-IMAGEM>

<!-- Exercício 2 🚀: -->
<!-- Crie o arquivo Compose para subir um ghost blog, essa plataforma é similar com o WordPress e é utilizada para criar sites de conteúdo. Você pode ler no site oficial como criar conteúdos nele e utilizá-lo. Para esse exercício, utilizaremos apenas sua página de exemplo: -->

<!-- 1 - Utilize a versão “3” no arquivo; -->
<!-- 2 - Crie um service para subir a plataforma, utilize a imagem ghost:1-alpine; -->
<!-- 3 - Publique a porta 2368, fazendo bind também para a 2368; -->

criar arquivo docker-compose.yaml
version: '3'

services:
  ghost:
    image: ghost:1-alpine
    ports: 
      - 2368:2368

<!-- 4 - Suba a aplicação utilizando o docker-compose e então acesse a porta publicada para validar se deu tudo certo. -->

docker-compose up

<!-- Exercício 3 🚀: -->
<!-- Por padrão o ghost utiliza um banco de dados SQLite interno para salvar as informações, porém, vamos alterar esse comportamento para exercitar nossos conhecimentos: -->

<!-- 1 - Crie um novo serviço db para o nosso banco de dados:
Podemos utilizar o banco de dados MySQL, utilize a imagem mysql:5.7.40;
Precisamos definir uma senha root para o banco, para isso utilize a variável de ambiente MYSQL_ROOT_PASSWORD

2 - Agora precisamos configurar nosso serviço ghost para utilizar o banco de dados:
Defina o tipo de banco de dados a ser usado pelo ghost definindo a variável de ambiente database__client para mysql;
Defina o serviço db como servidor do banco de dados na variável de ambiente database__connection__host;
Defina as credenciais para a conexão com o banco de dados
Para definir a pessoa usuária (root), utilize a variável de ambiente database__connection__user
Para definir a senha (a mesma que definimos no nosso serviço db), utilize a variável de ambiente database__connection__password
Defina o nome ghost para o nome do database no banco de dados utilizando a variável de ambiente database__connection__database;
Utilize a opção depends_on para criar relações de dependências entre os serviços. -->

  version: '3'

  services:
    ghost:
      image: ghost:1-alpine
      restart: always
      ports:
        - 2368:2368
      depends_on:
        - "db"
      environment:
        # see https://ghost.org/docs/config/
        database__client: mysql
        database__connection__host: db
        database__connection__user: root
        database__connection__password: password
        database__connection__database: ghost

    db:
      # platform: Linux/x86_64 # Caso utilize MacOS, descomente essa linha
      image: mysql:5.7.40
      environment:
        MYSQL_ROOT_PASSWORD: password


<!-- 3 - Suba o ambiente com o novo arquivo usando o docker-compose e então acesse a porta. -->

docker-compose up

<!-- Exercício 4: -->
<!-- Agora vamos praticar os conceitos de volumes e networks. -->

<!-- 1 - Configure o nosso serviço mysql para utilizar um volume, conforme vimos no conteúdo, utilize o caminho target /var/lib/mysql. -->

<!-- 2 - Ao invés de utilizar a rede padrão criada pelo Compose, defina uma rede chamada my-network para a comunicação dos dois serviços. -->

<!-- 3 - Suba o ambiente com o novo arquivo usando o docker-compose e então acesse-o. -->

    version: '3'

    services:

      ghost:
        image: ghost:1-alpine
        restart: always
        ports:
          - 2368:2368
        depends_on:
          - "db"
        environment:
          # see https://ghost.org/docs/config/
          database__client: mysql
          database__connection__host: db
          database__connection__user: root
          database__connection__password: password
          database__connection__database: ghost
        networks:
          - my-network

      db:
        # platform: Linux/x86_64 # Caso utilize MacOS, descomente essa linha
        image: mysql:5.7.40
        restart: always
        environment:
          MYSQL_ROOT_PASSWORD: password
        volumes:
          - db-data:/var/lib/mysql
        networks:
          - my-network
    volumes:
      db-data:

    networks:
      my-network:

<!-- Exercício 5: -->
<!-- Agora vamos criar um novo arquivo Compose, para rodarmos uma aplicação React, conforme vimos alguns exemplos do conteúdo: -->

<!-- 1 - Inicie um novo projeto ReactJS utilizando o create-react-app; -->

<!-- 2 - Crie o Dockerfile, conforme vimos na aula passada; -->

<!-- 3 - Crie um novo arquivo Compose utilizando a versão 3; -->

<!-- 4 - Defina um serviço no arquivo para nosso app, para isso utilize a opção build para apontar para o Dockerfile; -->

<!-- 5 - Publique a porta exposta no Dockerfile fazendo bind para a porta 8080 do localhost; -->

  arquivo Dockerfile

  version: '3'

  services:

    frontend:
      build: ./my-app
      ports:
        - 8080:80

<!-- Exercício 6: -->
<!-- Para simularmos o processo de desenvolvimento, faça a alteração em alguma parte do código do app react, e então execute o comando para subir o serviço novamente, “rebuildando” a imagem para aplicar as alterações. -->

docker-compose up --build -d