# 1. Introdução
## 1.1 Finalidade
Este documento oferece uma visão geral arquitetural abrangente do sistema e, desse modo, especifica decisões relevantes na produção e implementação do projeto Aix em relação ao assunto discorrido, explicitando como acontecerá a comunicação dos diversos serviços contidos no software como um todo.

## 1.2 Escopo
Aix é um bot disponibilizado na plataforma Jupyter, que visa orientar o ensino e aprendizado do usuário com assuntos relacionados a introdução à linguagem python.


# 3 Metas e Restrições da Arquitetura 
A aplicação deverá ser suportada pelo Jupyter Notebook e para seu desenvolvimento serão usadas as seguintes tecnologias:
* React.js: biblioteca de JavaScript para criar interfaces para o usuário, com o qual faremos a parte de front-end da aplicação
* Flask: *microframework*, construído em python, para o desenvolvimento das API's do projeto.

  Além disso, a ferramenta Docker será utilizada para facilitar o desenvolvimento em um ambiente isolado e construído especialmente para a equipe.