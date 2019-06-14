---
layout: post
title: Resultados do Teste de usabilidade 2
tags: teste usabilidade
category: Teste de Usabilidade
---

| Data       | Versão | Descrição            | Autor         |
| ---------- | ------ | -------------------- | ------------- |
| 13/06/2019 | 1.0    | Criação do documento | Kamilla Costa |

## Introdução

Afim de atestar a qualidade do produto Aix, foi realizado um teste de usabilidade com pessoas que se enquadram em nosso público-alvo (alunos e monitores de disciplinas de introdução à programação ou iniciantes em geral de programação) por meio de um teste aplicado presencialmente.

## Metodologia

Para a realização do teste foram escolhidos 6 alunos, dentre os quais havia alunos da disciplina de APC, alunos de outros cursos da universiadade e alunos que estão encerrando a graduação referente ao curso de software. Todos seguiram um roteiro de atividades que ia desde o cumprimento e conhecimentos gerais sobre o bot, até a construção de um hello world, perpassando por várias das features presentes no software, tais como links extras para conteúdos iniciais e pesquisas em um fórum online, assim como a realização do login na pplataforma UVA.

## Pontos positivos

- Personalidade é muito boa
- Cronograma muito intuitivo
- É muito bom o bot indicar o próximo conteúdo, evitar abrir o cronograma toda hora
- A action 'vaga' está funcionando e pegando qual o fluxo estamos seguindo.

## Tarefas que necessitaram da execução de mais de um passo

- arquivos, onde foi necessário perguntar 3 vezes pra conseguir a resposta que queria
- pesquisa no stack que precisou de 2 passos
- sobre Stack Overflow demorou 3 passos para conseguir a resposta.

## Melhorias a serem implementadas

- Instalação tá só pra debian, seria bom extender pra outros S.O
- Ao pesquisar no stack ele retorna coisas relacionadas à outras linguagens e não só python
- Tentar traduzir os termos em português na pesquisa do stack overflow em caso de pergunta em português pra aumentar as respostas. Ou pedir para o usuário digitar o erro em inglês.
- Usuário leigo pode não saber onde codar, falar sobre o jupyter, interpretador interativo, etc...
- Exemplo de bibliotecas falhou (mas ao testar eu msm, funcionou)
- Não tem nenhum retorno com exercícios (a não ser q seja escrito o nome corretamente)(não cai nem em fallback)
- Exemplo de arquivos retornou "sobre arquivos" (mas ao testar eu msm, funcionou)
- Conteúdo extra de variáveis tá com a intent mal elaborada
- Intents das actions do UVA não estão funcionais, com poucas frases de exemplo
- Usuário usou exemplos para perguntar sobre assuntos para chegar ao cronograma e não conseguiu (basta adicionar intents referentes)
- Usuário sugeriu adicionarmos um exemplo próprio para cada tipo de variável (inteiros, pontos flutuantes, booleanos, caracteres e strings), tanto explicativo quanto em código
- Usuário sugeriu a implementação de um comando que levasse automaticamente ao próximo conteúdo
- Usuário sugeriu que fosse mais claro como acessar o cronograma
- Existe um problema na apresentção. "o que você pode fazer","o que você é capaz","qual seu nome", "qual seu objetivo" não estão retornando o esperado.
- Definir o que é Stack Overflow antes de sugerir a pesquisa, já que nem todos os usuários já tiveram contato com a ferramenta.
- Algumas utters finais de conteúdo não indicam o próximo conteúdo a ser seguido
- Nenhum usuário participante do teste conseguiu chegar na história da aix. Isso deve ser melhorado.
- utilizar coloquialismos como "printar" e "inputar" nas intents, pois é assim que pesquisaram.
- Falar o que é loop infinito.
- Melhorar intents sobre inputs, pois o usuário não conseguiu chegar neste fluxo mesmo após muitas tentativas
- Melhorar intents de Strings e de funções. Pois quando não tem ascento, não vai.

## Conclusões

Com a aplicação deste teste foi possível constatar que temos um bom guia num passo a passo do usuário dentro do conteúdo básico presente no bot e que o cronograma criado é de grande valia para que o usuário seja guiado durante sua interação com o bot, e que a realização das tarefas foi relativamente simples, pois a maioria dos participantes as concluiu sem grandes problemas. Por outro lado, ficou evidente a necessidade de refatoração de algumas utters e intents, melhorias em relação a pesquisa realizada no stackoverflow, adição da explicação sobre local para desenvolvimento do código entre outras sugestões de melhoria.
