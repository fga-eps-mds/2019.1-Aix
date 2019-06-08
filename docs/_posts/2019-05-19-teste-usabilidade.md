---
layout: post
title: Teste de usabilidade
tags: teste usabilidade 
category: Produto
---
|Data   |Versão   |Descrição   |Autor   |
|---|---|---|---|
|19/05/2019   | 1.0  |Criação do documento   |Lucas Vitor   |

## Introdução
Afim de atestar a qualidade do produto Aix, foi realizado um teste de usabilidade com pessoas que se enquadram em nosso público-alvo (alunos e monitores de disciplinas de introdução à programação ou iniciantes em geral de programação).

## Metodologia

Para a realização do teste foram escolhidos 6 alunos, dentre os quais 1 é monitor de uma disciplina de introdução à programação e 5 são alunos dessa disciplina. Todos seguiram um roteiro de atividades que ia desde o cumprimento e conhecimentos gerais sobre o bot, até a construção de um hello world, perpassando por várias das features presentes no software, tais como links extras para conteúdos iniciais e pesquisas em um fórum online.

Após os contatos com o bot, os participantes foram convidados à preencher um formulário relatando suas experiências e impressões do bot, afim de que a equipe de desenvolvimento possa entender o quão bem aceito o software será recebido pela comunidade, bem como erros, falhas e problemas de comunicação necessitam de atenção urgente para a manutenção da boa qualidade do produto.

## Resultados obtidos

Na aplicação do formulário foram feitas perguntas básicas como "Na sua opinião, para quê serve o chatbode Aix?" para entender se a ideia geral do bot é clara o suficiente para o usuário final, até a realização de atividades específicas como "Utilizando suas palavras, execute a tarefa de interação com o bot para que ele seja capaz de realizar uma pesquisa sobre um problema ou curiosidade relacionado a área de programação." afim de entender se a tarefa é de fácil resolução dentro do bot. Abaixo se encontra um resumo dos resultados encontrados:

### Questões gerais sobre o bot

Nesta parte procurou-se entender a visão geral do bot por parte dos participantes do teste.

![questao_1]({{ site.url }}/2019.1-Aix/assets/img/usabilidade/questao_1.png)

![questao_2]({{ site.url }}/2019.1-Aix/assets/img/usabilidade/questao_2.png)

![questao_3]({{ site.url }}/2019.1-Aix/assets/img/usabilidade/questao_3.png)

![questao_4]({{ site.url }}/2019.1-Aix/assets/img/usabilidade/questao_4.png)

### Tarefa 1 - Explicação do python

![questao_5]({{ site.url }}/2019.1-Aix/assets/img/usabilidade/questao_5.png)

![questao_6]({{ site.url }}/2019.1-Aix/assets/img/usabilidade/questao_6.png)

![questao_7]({{ site.url }}/2019.1-Aix/assets/img/usabilidade/questao_7.png)

### Tarefa 2 - Entendendo as funcionalidades do bot

![questao_8]({{ site.url }}/2019.1-Aix/assets/img/usabilidade/questao_8.png)

![questao_9]({{ site.url }}/2019.1-Aix/assets/img/usabilidade/questao_9.png)

![questao_10]({{ site.url }}/2019.1-Aix/assets/img/usabilidade/questao_10.png)

### Tarefa 3 - Pesquisa no bot

![questao_11]({{ site.url }}/2019.1-Aix/assets/img/usabilidade/questao_11.png)

![questao_12]({{ site.url }}/2019.1-Aix/assets/img/usabilidade/questao_12.png)

![questao_13]({{ site.url }}/2019.1-Aix/assets/img/usabilidade/questao_13.png)

### Feedback final

![questao_14]({{ site.url }}/2019.1-Aix/assets/img/usabilidade/questao_14.png)

![questao_15]({{ site.url }}/2019.1-Aix/assets/img/usabilidade/questao_15.png)

Além do formulário, foram anotadas questões que foram feitas de forma verbal e natural pelos participantes do teste. Dentre as quais, as questões mais frequentes foram:

<li>Pesquisa do stackoverflow falha quando se pergunta exatamente sobre um assunto já mapeado no bot</li>

<li>Explicação do que é stackoverflow</li>

<li>Assuntos muito gerais, exemplo: loops ao invés de for e while</li>

<li>Material sobre strings</li>

<li>Noção dos conteúdos base, um roteiro indicando o caminho a seguir por exemplo, pois um usuário totalmente leigo não saberia os assuntos para perguntar</li>

## Conclusões

Com a aplicação deste teste foi possível constatar que temos um bom guia num passo a passo do usuário dentro do conteúdo básico presente no bot, e que a realização das tarefas foi relativamente simples, pois a maioria dos participantes as concluiu sem grandes problemas, além disso, 75% dos participantes descreveu a maneira como as informações são apresentadas como ótima ou boa. Por outro lado, ficou evidente a necessidade de aumento do vocabulário do bot, inserção de conteúdos mais básicos, explicação de algumas features, e a criação de um roteiro que possa guiar de forma eficaz um usuário dentro da aplicação.

## Melhorias

Ao analisar as respostas dos usuários foi possível identificar melhorias a serem feitas nas próximas sprints. São elas:

- Deixar as informações dispostas no bot mais objetivas.
- Exemplificar com a sintaxe de python alguns conceitos.
- Explicar as diferentes estruturas de repetição e suas diferenças.
- Disponibilizar um cronograma de conteúdos a serem seguidos para usuários totalmente iniciantes. (Aula 1, Aula 2...)
- Melhorar a função de pesquisa para se obter uma maior variedade de informações.
- Melhorar precisão na detecção do conteúdo a ser apresentado.
- Permitir que conteúdos já mapeados estejam, também, sujeitos a pesquisas.
- Ser capaz de reconhecer mais "termos" (maior variedade de vocabulário).
- Adicionar exemplos em python em todas as respostas.
- Explicar o que é o stackoverflow
- Inserir conteúdo sobre strings.
- Um roteiro guiando o usuário.

Observações: Nem todas as melhorias identificadas no teste de usabilidade são coerentes com o escopo do projeto além de nem todas serem viáveis. Os gerentes do projeto analisarão o que e como cada melhoria deve ser implementada.