---
layout: post
title: Usabilidade do script de automatização de intents
tags: script automatização intents mds 
category: Produto
---

| Data       | Versão | Descrição                                   | Autor            |
| :--------: | :----: | :-----------------------------------------: | :--------------: |
| 09/06/2019 | 0.0.1  | Criação do script para automação de intent             |  Gabriela, Gustavo   |
| 10/06/2019 | 0.0.2  | Refatoração devido a problemas de formatação       |  Gabriela, Gustavo   |

## O que é
Script com vários modelos de intents mapeados para facilitar a criação de novas intents ou manuntenabilidade das existentes.

## Como usar
1. Digite o modelo de intent que você deseja gerar.
    As opções são: codigo_em_python, conteudo_extra, desafio, exemplo, exercicio, sobre.

2. Digite o conteúdo que deve ser concatenado com o modelo escolhido
    Podem ser digitados todas as variações do conteúdo, exemplo: variavel, variaveis, variável, variáveis.

3. Digite "QQ" para finalizar a iteração pedindo o conteúdo e começar a criação do arquivo final.

4. Será gerada um arquivo nomeado "result.txt", nele estará todas as intents mapeadas já com os conteúdos concatenados.