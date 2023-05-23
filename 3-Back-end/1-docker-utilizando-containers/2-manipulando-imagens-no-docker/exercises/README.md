🚀 Exercício:

Vamos usar uma imagem disponível no DockerHub conhecida como “cowsay” (uma vaca falante no terminal 🐮)!

A ideia é deixarmos a mensagem para o cowsay parametrizável. Dessa forma, conseguiremos executar o comando:

Copiar
    docker container run cowsay Muuuuuuhhh
E ter a seguinte saída no terminal:

Copiar
____________
< Muuuuuuhhh >
------------
         \   ^__^
         \  (oo)\_______
            (__)\       )\/\
               ||----w |
               ||     ||
Para isso:

Crie um Dockerfile utilizando a imagem chuanwen/cowsay.
Defina um ENTRYPOINT para a execução do comando.
Observe que o executável cowsay está no diretório /usr/games/
Lembre-se que com ele, diferente do CMD, o comando não poderá ser sobrescrito com o docker run, porém conseguiremos passar parâmetros ao binário e exploraremos esse recurso para poder passar a mensagem.
Utilize o CMD para definir uma mensagem padrão.
Gere uma build e execute um container baseado em sua imagem sem passar nenhum comando.
Execute um novo container passando sua mensagem para testar. Além da mensagem você pode utilizar a opção -l para listar outros personagens disponíveis e então executar algo como docker container run cowsay -f dragon-and-cow "VQV TRYBE", para exibir um dragão junto com a vaquinha.


=============================================================================================================================================================================================

Solução

<!-- Crie um Dockerfile utilizando a imagem chuanwen/cowsay. -->

FROM chuanwen/cowsay:latest

<!-- Agora defina um ENTRYPOINT para a execução do comando. -->

ENTRYPOINT [ "/usr/games/cowsay" ]

<!-- Utilize o CMD para definir uma mensagem padrão. -->

CMD [ "#VQV Trybe" ]

<!-- Gere uma build e execute um contêiner baseado em sua imagem sem passar nenhum comando. -->

docker image build ./ -t cowsay

<!-- Agora execute um novo contêiner passando sua mensagem para testar. Além da mensagem você pode utilizar a opção -l para listar outros personagens disponíveis e então executar algo como docker container run cowsay -f dragon-and-cow "VQM TRYBE", para exibir um dragão junto com a vaquinha. -->
<!-- Para rodar com a mensagem padrão que você criou no [CMD] execute: -->

docker container run cowsay

Você também pode passar um parâmetro logo após o comando:

<!-- docker container run cowsay Go Trybe! -->

<!-- Este comando vai rodar um leão com a frase #VQV TRYBE: -->

docker container run cowsay -f moofasa "#VQV TRYBE"

<!-- Finalmente, se quiser obter a lista com os outros animais, rode o comando: -->

docker container run cowsay -l