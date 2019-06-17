---
layout: post
title: Documento de Qualidade
tags: qualidade usabilidade teste eps
category: Gerencia
---
|Data   |Versão   |Descrição   |Autor   |
|---|---|---|---|
|26/04/2019   | 1.0  |Criação do documento   |Kamilla Costa   |
|17/06/2019   | 1.1  |Atualização do documento | Kamilla Costa |

## Objetivo

O objetivo desse documento é apresentar como, quais e os porquês referentes às adoções de cada tipo de teste durante o processo de desenvolvimento do produto. 

## Qualidade aplicada no contexto de chatbots

A problemática envolvida no contexto de aplicação de qualidade em chatbots se dá pela falta de técnicas para aplicação de testes específicos para controle da qualidade de chatbots. Diante desta dificuldade os riscos serão mitigados por meio da aplicação dos seguintes testes:
    - Testes de Usabilidades
    - Testes Unitários 
    - Testes Estáticos

## Testes de Usabilidade

O cumprimento de testes de usabilidade baseia-se na aplicação da técnica de validação utilizada para avaliar um produto ou serviço. Os testes são realizados com usuários representativos do público-alvo. 
Os dados foram levantados baseado na aplicação de um formulário no Google Forms mediante a validação de funcionalidades aplicadas para a release 1 afim de refatorar conteúdos e aplicar melhorias nas implementação existentes.

![]({{ site.url }}/2019.1-Aix/assets/img/grafico1.png)

A partir destes dados foi observado que parte dos usuários conseguiram acessar a parte do fluxo que está integrada a API do stackoverflow e parte ou não conseguiram acessar ou não levaram mais tempo que o proposto para identificar que o fluxo esteja intuitivo o suficiente para o usuário. Logo identificamso a necessidade de implementar melhorias quanto a construção dos fluxos de conversas.

![]({{ site.url }}/2019.1-Aix/assets/img/grafico2.png)

Em relação a satisfação dos usuário quanto a explicação referente aos conteúdos dispostos no bot, foi observado que metade dos usuários ficaram satisfeitos e a outra maior parte da metade achou exagerado demais a quantidade de conteúdo oferecida pelo bot. Identificando assim melhorias quanto a quantidade de informação fornecida e adequação do melhor formato para estar disposto na janela do bot.

![]({{ site.url }}/2019.1-Aix/assets/img/grafico3.png)

Foi possível identificar melhoria spor meio desta coleta de sugestões que os usuários esperam uma melhor interação do bot quanto a algumas perguntas gerais do campo da programação assim como uma maior diversidade de aceitação quanto ao vocabulário do bot.

![]({{ site.url }}/2019.1-Aix/assets/img/grafico4.png)

Neste quesito foi possivel identificar que mais da metade dos usuários não tiveram problemas quanto ao fluxo do bot e a consideraram intuitiva.

![]({{ site.url }}/2019.1-Aix/assets/img/grafico5.png)

Neste quesito foi possivel identificar que mais da metade dos usuários não tiveram problemas quanto a compreensão das funcionalidades dispostas no bot.

![]({{ site.url }}/2019.1-Aix/assets/img/grafico6.png)

Quanto as sugestões de melhorias foi possível identificar várias que estão sendo planejadas para implementação afim de melhorar a interação entre bot e usuário assim como identificar alguns problemas por meio de sua utilização com usuários diversificados.

Foram aplicados mais dois testes de usabilidade documentados no repositório.



## Testes Unitários

A aplicação de testes unitários se dá por meio da implementação de testes da menor parte testável de um programa. Em nosso contexto, como entrega para a release 1 foi aplicado o teste unitário na função da custom action responsável pela integração do bot com a API do stackoverflow por meio da utilização do framework Pytest.


![]({{ site.url }}/2019.1-Aix/assets/img/teste.png)


## Testes Estáticos

A análise estática de softwares, também conhecida como whitebox, trabalha diretamente com o código. Nesse caso, os componentes são verificados sem que o produto seja executado. No chatbot Aix foi aplicado o uso de ferramentas automatizadas no qual o principal objetivo dessa técnica é identificar erros de programação como práticas ruins, erros de sintaxe, identação entre outros. As ferramentas utilizadas são Flake8 e CodeClimate

#### CodeClimate
![]({{ site.url }}/2019.1-Aix/assets/img/codeclimate1.png)

#### Flake8
![]({{ site.url }}/2019.1-Aix/assets/img/flake8.png)