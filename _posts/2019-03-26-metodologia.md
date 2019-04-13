---
layout: post
title: Metodologia
tags: metodologia documento eps
category: Contribuicao
---

<p align="justify">&emsp;&emsp; Este documento tem o objetivo de esclarecer as metodologias ágeis adotadas para o projeto **Aix**. Abaixo, encontra-se descrito as metodologias bases (Scrum e Kanban), papeis e artefatos selecionados, suprindo assim, as necessidades de organização e atividades da equipe.</p>
<!--more-->
<p align="justify">&emsp;&emsp;O <b><i>Scrum</i></b> é um <i>framework</i> que preza pela entrega de valor ao cliente de maneira rápida, criativa, onde sua equipe trabalha de forma produtiva.</p>
<p align="justify">&emsp;&emsp;Tem como artefatos <i>Product Backlog</i>, <i>Sprint Backlog</i> e incrementos. Atividades, tem as Sprints, <i>Sprints Planning</i>, Daily Scrum, <i>Sprint Review</i> e Retrospectiva da <i>Sprint</i>. E como artefatos temos o <i>Product Backlog</i> e <i>Sprint Backlog</i>.</p>


<p align="justify">&emsp;&emsp; Algumas práticas que iremos adotar desta metodologia são: <i>Pair Programming</i>, Integração Contínua, Padrão de Código e Testes.</p>


# Papéis

## <i>Product Owner</i>
* Atribuições
    - Organizar o <i>Product Backlog</i> em ordem de prioridade, de forma a entregar valor ao cliente e manter a coesão do produto;
    - Garantir que o <i>Product Backlog</i> esteja de forma clara;
    - Assegurar que os Desenvolvedores entendam o <i>Product Backlog</i> no nível de especificação necessário;
    - Trabalhar a venda do produto de software;
    - Fazer o intermédio entre cliente e equipe;
    - Mostrar a visão do produto em documentos como Canvas.

## <i>Scrum Master</i>
* Atribuições
    - Garantir que o <i>Product Backlog</i> seja feito, de acordo com a priorização do <i>Product Owner</i>, pelos Desenvolvedores;
    - Certificar-se que os rituais ageís sejam realizados por toda a equipe da forma como foi descrito;
    - Mapear o progresso da equipe e do desenvolvimento do produto, assim como suas falhas e questões a melhorar;
    - Documentar o processo de cada <i>Sprint</i>.

## Arquiteto de <i>Software</i>
* Atribuições
    - Mapear, juntamente ao <i>Product Owner</i> e DevOps, a arquitetura necessária para o desenvolvimento do produto;
    - Desenhar e diagramar a arquitetura do produto;
    - Garantir que a arquitetura seja implementada pelos Desenvolvedores.
## <DevOps>
* Atribuições
    - Desenhar, juntamente com o Arquiteto, os vários pipelines do produto de software;
    - Implementar a integração contínua;
    - Garantir o deploy contínuo;
    - Facilitar a configuração do ambiente de desenvolvimento da equipe.
## <i>Quality Assurance</i>
* Atribuições
    - Decidir métricas para avaliar o produto de software e seu desenvolvimento;
    - Coletar e Analisar as métricas do produto de software;
    - Garantir as melhorias das métricas que necessitam dessas melhorias e manter a qualidade, tanto em termos de código, quanto em usabilidade, do produto de software.
## Desenvolvedores
* Atribuições
    - Desenvolver as funcionalidades priorizadas pelo <i>Product Owner</i> e selecionadas pelo <i>Scrum Master</i> dentro da <i>Sprint</i>;
    - Manter a qualidade do produto em relação a código.

# Atividades da <i>Metodologia</i>

## <i>Sprint</i>

* Trata-se de período definido pela equipe, que no caso do projeto é um período de uma semana, onde são realizado as tarefas definidas pelo <i>Scrum Master</i>, mas priorizadas pelo <i>Product Owner</i>.
* Assim que este período é encerrado, entrega-se um valor ao cliente, como foi definido.

    - No projeto: a <i>Sprint</i> tem início no sábado e seu término no sábado seguinte.

## Planejamento da <i>Sprint</i>

* São reuniões onde o <i>Scrum Master</i>, em conjunto com o <i>Product Owner</i>, decide as funcionalidades e atividades que deverão ser realizadas pela equipe de Desenvolvimento e também avaliadas quais melhorias devem ser feitas.
* O esforço para realizar cada uma das tarefas é medido com a equipe e assim, essas tarefas serão pontuadas.
* É definido também, as duplas que trabalharão em conjunto (<i>Pair Programming</i>).

## <i>Daily Meeting</i>

* Reuniões com o tempo determinado de 15 minutos, onde cada membro da equipe fala sobre o andamento da tarefa e seu planejamento para terminá-la.
    - No projeto: estas reuniões ocorrem de segunda a sexta, e possuem duração de, no máximo, 20 minutos.

## <i>Sprint Review</i>

* Discussão das dificuldades, melhorias e pontos positivos durante a <i>Sprint</i>, além do levantamento das tarefas realizadas e não realizadas.
* A avaliação geral da <i>Sprint</i> é feita pelo <i>Scrum Master</i>, porém todas os pontos (positivos, negativos e a melhorar) é debatido pela equipe.
    - No projeto: a Review ocorre aos sábados, no mesmo dia do Planejamento da <i>Sprint</i>.

## <i>Pair Programming</i>

* Ritual onde dois membros da equipe de Desenvolvimento, trabalham juntos para realizar uma tarefa.
* A cada 15 minutos, um deles assume o papel de piloto, ou seja, escreve o código, e o outro assume o papel de co-piloto e dita a lógica para realizar a funcionalidade e também auxilia o piloto a pensar na melhor forma de desenvolver essa funcionalidade.

## Integração Contínua

* Prática de testar as modificações do código que foi submetida ao repositorio remoto do projeto.
* Todo o funcionamento da integração continua é pensado e efeitvado pelo DevOps do projeto.

## Padrão de Código

* É a definição de escrita do código, de maneira a manter a homogeniedade deste.
* A folha de estilo, documento que define esse padrão, é contruida pelo <i>Quality Assurence</i>.

## Testes

* Toda a funcionalidade desenvolvida, deve ser testada, ou seja, deve ser implementados testes que prevêm funcionamento errôneo ou indesejado da funcionalidade. E esta funcionalidade deve passar em todos os testes escritos.

## <i>Kanban</i>

* Metodologia que consistem em um quadro divido em <i><b>TO DO</b></i>, <i><b>DOING</b></i> e <i><b>DONE</b></i>, e em cada uma destas colunas é colocado as tarefas que devem ser feitas, as que estão no processo de ser feitas e as completas, respectivamente.

    - No projeto, utilizamos o <i><b>Zenhub</b></i> para contemplar esta metodologia.



# Referências Bibliográficas

> | [GLOSSARY Extreme Programming](https://www.agilealliance.org/glossary/xp/#q=~(filters~(postType~(~'post~'aa_book~'aa_event_session~'aa_experience_report~'aa_glossary~'aa_research_paper~'aa_video)~tags~(~'xp))~searchTerm~'~sort~false~sortDirection~'asc~page~1))

> | [Extreme Programming - Conceitos e Práticas](https://www.devmedia.com.br/extreme-programming-conceitos-e-praticas/1498)

> | [What is Scrum](https://www.scrum.org/resources/what-is-scrum?gclid=Cj0KCQjwlK7cBRCnARIsAJiE3Mg-GBLapVDq-TPyx-wt0K0_8jLFjB14XaEjPZzMTJUJ5fPvZWmQmokaAs23EALw_wcB)

> | [Lino - Metodologia](https://github.com/fga-eps-mds/2018.2-Lino/edit/master/docs/metodologia.md)
