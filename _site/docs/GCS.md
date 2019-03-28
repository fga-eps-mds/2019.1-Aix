# Plano de Gerenciamento

---

# Sumário

[1. Introdução](#1-introdução)

[2. Ferramentas](#2-ferramentas)

[4. Diagrama de Integração entre Ferramentas](#3-diagrama-de-integração-entre-ferramentas)

[5. Políticas](#3-políticas)

[6. Uso de Issues](#3-uso-de-issues) 

---


## 1. Introdução

<p align="justify">Esse documento tem como objetivo a construção de um plano para definição das ferramentas que serão utilizadas pela equipe, das políticas para padronização de <i>commits</i>, <i>branchs</i>, <i>pull requests</i> e <i>issues</i>. </p>

## 2. Ferramentas

<p align="justify"> As ferramentas que serão utilizadas pela Equipe de Desenvolvimento serão:</p>

|Ferramentas|Versão|Descrição|
|:--:|:--:|:--:|
|Visual Studio Code|-|Editor de texto para codar|
|Git|2.7.4 ou maior|Ferramenta de versionamento|
|GitHub|-|Servidor de hospedagem do projeto|
|GitHub Pages|-|Página estática para documentação|
|CodeClimate|-|Ferramenta para análise estática do código|
|Rasa Core+NLU|0.14.6|Ferramenta para criação do ChatBot|
|Flask|1.0.2|Framework de desenvolvimento para API|
|Flak8||Ferramenta de análise estática de código|
|Rocket Chat|-|Ferramenta para visualização do chat|

### 2 Visual Studio Code
### 2 Git
### 2 GitHub
### 2 GitHub Pages
### 2 GitHub
### 2 CodeClimate
### 2 Rasa Core+NLU
### 2 Flask
### 2 Flak8
### 2 Rocket Chat


## 3. Políticas

### 3.1 Política de __Commits__

<p align="justify">
Os commits deveram possuir mensagens curtas, significativas e em português sobre o que é adicionado, corrigido ou removido no mesmo. Deve ser atômico, de forma a facilitar a refatoração e a rastreabilidade das funcionalidades.

Cada commit estará ligado diretamente a uma issue, e para facilidade no rastreamento das atividades cada commit deverá possuir o hash da issue a qual se relaciona.

E caso haja pareamento no desenvolvimento do commit, o commit deverá ser co-autorado. O seguinte padrão deve ser seguido:

#Número_da_issue - Mensagem descritiva do commit


Co-authored-by: Nome da pessoa < emaildapessoa >

</p>

### 3.2 Política de __Branchs__

<p align="justify">
O repositório do projeto contará com duas branches principais para o desenvolvimento, sendo elas: master e devel, e as branches auxiliares contendo as funcionalidades desenvolvidas.

A branch master conterá a versão estável do produto, tendo seu conteúdo proveniente da branch de desenvolvimento (devel) após a aprovação do pull request. Por decisões de projeto, nenhum commit poderá ser feito pelos membros diretamente na branch master, exceto os commits iniciais de configuração do repositório.

A branch devel será utilizada para o desenvolvimento do produto, onde a integração das funcionalidades desenvolvidas pela equipe nas branches auxiliares ocorrerá.

As branches auxiliares serão utilizadas para o desenvolvimento das funcionalidades. Essas branches serão nomeadas de acordo com a rastreabilidade e na língua portuguesa, tendo o seu padrão de acordo com a metodologia adotada no momento.

O nome da branch seguirá o seguinte padrão: issue_numero_da_issue_tema_da_issue

- Exemplo: issue_1_documento_de_visao</p>

### 3.3 Política de Aprovação de Código

<p align="justify">
Após a implementação ou correção de bug descrita na issue (o que inclui todos os critérios de aceitação estarem completos), o membro deverá abrir um Pull Request para a branch devel, que será revisado por um integrante da gerência responsável (em geral, Product Owner ou Scrum Master). E ao final de casa Sprint um Pull Request deverá ser aberto a branch Master, a partir da Devel e ser revisado pelo  Product Owner.</p>

## 4. Uso de Issues

<p align="justify">
As issues serão utilizadas por questões de rastreabilidade, ou seja, para se ter maior controle sobre o que é desenvolvido, além de permitir melhor gestão de pessoal, pois facilita a alocação de trabalho para serviços específicos e permite acompanhamento do desenvolvimento a qual descreve. Cada issue deverá seguir o template descrito na própria issue.</p>



## 5. Bibliografia

> | [GCS da equipe do Receita Mais](https://github.com/fga-eps-mds/2017.2-Receita-Mais/wiki/Plano-de-Gerenciamento-e-Configura%C3%A7%C3%A3o-de-Software)