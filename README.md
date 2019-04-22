<p align="center">
  <img src="https://raw.githubusercontent.com/fga-eps-mds/2019.1-Aix/master/assets/img/cabracinza.png" alt="Logo">
</p>

<h1 align="center"> Aix - Bot de Aprendizado integrado a plataforma Jupyter</h1>

  <p align="center">
    <a href="https://fga-eps-mds.github.io/2019.1-Aix"><strong>Visite nossa página &raquo;</strong></a>
    <br>
  </p>
</p>

### Sobre o projeto

<p align="justify"> &emsp;&emsp;
  O projeto Aix baseia-se na criação de um bot disponibilizado na plataforma <a href="https://jupyter.org" margin=50> Jupyter</a>, que visa orientar o ensino e aprendizado do usuário com assuntos relacionados a introdução à linguagem python.</p>

<p align="justify"> &emsp;&emsp;
  Como principais funcionalidade, tem-se:
</p>


### Principais funcionalidades

* Auxilio no esclarecimento de dúvidas sobre sintaxe e estrutura da linguagem Python;
* Auxilio na identificação da biblioteca que o usuário necessita para desenvolvimento;
* Apoio ao estudo da linguagem com sugestão de links seguros para busca na web;
* Feedback sobre correção de exercícios propostos ao bot;

### Guia de Contribuição
Caso queira contribuir com o projeto verifique o documento <a href="https://github.com/fga-eps-mds/2019.1-Aix/blob/master/docs/CODE_OF_CONDUCT.md" margin=50> CONTRIBUTING</a>

Caso tenha interesse em contribuir com nossa documentação é bem simples!

- Vá para a nossa branch gh-pages onde se encontra nosso documentos

```
  git checkout gh-pages
```
- Crie uma issue baseado em nosso template de issue regular a partir da branch gh-pages

```
  git checkout -b "issue_x_documentoX"
```

- Entre na pasta _posts

```
  cd _posts
```
  Nesta página você encontra todos os documentos referentes ao projetos!

- Lembre se de seguir nossa folha de estilo que pode ser encontrada em:

```
  cd _posts/2019-03-29-gcs.md
```
- Agora abra um pr em nosso repositório

- Agora é só aguardar que revisaremos seu PR e te daremos um feedback!


### Instalação
  Nesta seção estão descritos os passos necessários para instalar e executar o Aix localmente.

#### Pré-requisitos
* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/get-docker)
* [Docker-compose](https://docs.docker.com/compose/install/#install-compose)

#### Configuração
  Clone o repositório
  ```
    git clone https://github.com/fga-eps-mds/2019.1-Aix.git
  ```
  Inicialize o RocketChat
  ```
    docker-compose up -d rocketchat
  ```
  Inicialize o Bot(recomenda-se aguardar 3 minutos para que o rocketchat inicialize)
  ```
    docker-compose up bot
  ```
  Inicialize o Jupyter
  ```
    docker-compose up jupyter
  ```
  Sua instância do jupyter estará disponível em 
  ```
    http://localhost:8888/?token=f3e7fa23fb7e347ad05914368b625416b7a95a674dc078f7
  ```

  
### Licença

<p align="justify">&emsp;&emsp; Aix é distribuído sob a licença GPLv3. Consulte <a href="https://github.com/fga-eps-mds/2019.1-Aix/blob/master/LICENSE">LICENSE</a> para obter detalhes.</p>
