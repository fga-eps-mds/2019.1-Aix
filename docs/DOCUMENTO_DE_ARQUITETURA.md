# 1. Introdução
## 1.1 Finalidade
Este documento oferece uma visão geral arquitetural abrangente do sistema e, desse modo, especifica decisões relevantes na produção e implementação do projeto Aix em relação ao assunto discorrido, explicitando como acontecerá a comunicação dos diversos serviços contidos no software como um todo.

## 1.2 Escopo
Aix é um bot disponibilizado na plataforma Jupyter, que visa orientar o ensino e aprendizado do usuário com assuntos relacionados a introdução à linguagem python.


# 3 Metas e Restrições da Arquitetura 
A aplicação deverá ser suportada pelo Jupyter Notebook e para seu desenvolvimento serão usadas as seguintes tecnologias:
* React.js: biblioteca de JavaScript para criar interfaces para o usuário, com o qual faremos a parte de front-end da aplicação
* Flask: *microframework*, construído em python, para o desenvolvimento das API's do projeto. Será usado na versão 1.0.2.
* Docker: Ferramenta para gerar um ambiente isolado e construído especificamente para a equipe que será utilizado para facilitar o desenvolvimento do projeto. 
* Git: Ferramenta de versionamento que será usada em conjunto com o GitHub para salvar os dados do decorrer do projeto, possibilitando a hospedagem e a geração de backups do mesmo. Será usada a versão 2.7.4 ou maior.
* CodeClimate: Ferramenta para análise estática do código
* Rasa Core+NLU: Ferramenta para criação do ChatBot. Será usada na versão 0.14.6.
* Flake8: Ferramenta de análise estática de código. Será usada na versão #######
* Rocket Chat: Ferramenta para visualização do chat.
