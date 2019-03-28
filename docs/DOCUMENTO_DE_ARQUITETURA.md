# 1: Introdução
## 1.1 Finalidade
Este documento oferece uma visão geral arquitetural abrangente do sistema e, desse modo, especifica decisões relevantes na produção e implementação do projeto Aix em relação ao assunto discorrido, explicitando como acontecerá a comunicação dos diversos serviços contidos no software como um todo.

## 1.2 Escopo
Aix é um bot disponibilizado na plataforma Jupyter, que visa orientar o ensino e aprendizado do usuário com assuntos relacionados a introdução à linguagem python.

## Referências (tem q formatar dps)
* [Receita Mais](https://github.com/fga-eps-mds/2017.2-Receita-Mais/wiki/Documento-de-Arquitetura#4)
* [Dulce](https://dulce-work-schedule.github.io/especificacao/arquitetura.html)
* [Kalkuli](https://fga-eps-mds.github.io/2018.2-Kalkuli/docs/docArquitetura)
* [IBM](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjl7cre9pjhAhUDErkGHb2eA_IQFjAAegQIARAC&url=https://www.dca.ufrn.br/~anderson/FTP/dca0120/modelodocarquiteturasoftware.doc&usg=AOvVaw2P9L4xfD4kcFo0YtBNmuu8)
* [Quero Mais Conversa](https://github.com/QueroMais/QueroMaisConversa/wiki/Casos-de-Uso)

# 3: Metas e Restrições da Arquitetura 
A aplicação deverá ser suportada pelo Jupyter Notebook e para seu desenvolvimento serão usadas as seguintes tecnologias:
* React.js: biblioteca de JavaScript para criar interfaces para o usuário, com o qual faremos a parte de front-end da aplicação
* Flask: *microframework*, construído em python, para o desenvolvimento das API's do projeto. Será usado na versão 1.0.2.
* Docker: Ferramenta para gerar um ambiente isolado e construído especificamente para a equipe que será utilizado para facilitar o desenvolvimento do projeto. 
* Git: Ferramenta de versionamento que será usada em conjunto com o GitHub para salvar os dados do decorrer do projeto, possibilitando a hospedagem e a geração de backups do mesmo. Será usada a versão 2.7.4 ou maior.
* CodeClimate: Ferramenta para análise estática do código
* Rasa Core+NLU: Ferramenta para criação do ChatBot. Será usada na versão 0.14.6.
* Flake8: Ferramenta de análise estática de código. Será usada na versão #######
* Rocket Chat: Ferramenta para visualização do chat.

# 4: Casos de Uso

## 4.2 Especificações dos casos de uso
|Casos de Uso|Ator|Descrição|
|---|---|------|
|UC01 - Resposta de dúvidas| Usuário | Este caso de uso ocorre quando o usuário envia uma pergunta em relação à escrita da linguagem estudada ou assuntos básicos de programação|
|UC02 - Ajuda com sintaxe| Usuário| Este caso de uso ocorre quando o usuário erra algo na digitação de seu código. O Bot irá alertá-lo do erro|
|UC03 - Indicação de bibliotecas| Usuário | Este caso de uso permite o usuário buscar uma funcionalidade que não está disponível da STL da linguagem python. O Bot irá sugerir bibliotecas que possuam tal funcionalidade|
|UC04 - Compilação de códigos| Usuário | Este caso de uso permite o usuário compilar códigos a partir do envio de dados de entrada, saída e o script do código|
|UC05 - Feedback da compilação dos códigos| Sistema | Este caso de uso ocorre após a compilação de um código, onde o bot avisa o usuário de possíveis erros e warnings que aconteceram na ação pedida e os explica, para que possam ser consertados|
|UC06 - Salvar conversa| Sistema | Esse caso de uso ocorre após o usuário fechar o programa. O bot automaticamente salva os dados da conversa para que num próximo uso seja possível rever os que já foi conversado|
