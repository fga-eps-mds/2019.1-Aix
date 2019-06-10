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
<ol>
    <li>
        <p>Digite o modelo de intent que você deseja gerar.</p>
        <p>As opções são: codigo_em_python, conteudo_extra, desafio, exemplo, exercicio, sobre.</p>
    </li>
    <li>
        <p>Digite o conteúdo que deve ser concatenado com o modelo escolhido</p>
        <p>Podem ser digitados todas as variações do conteúdo, exemplo: variavel, variaveis, variável, variáveis.</p>
    </li>
    <li>
        <p>Digite "QQ" para finalizar a iteração pedindo o conteúdo e começar a criação do arquivo final.</p>
    </li>
    <li>
        <p>Será gerada um arquivo nomeado "result.txt", nele estará todas as intents mapeadas já com os conteúdos concatenados.</p>
    </li>
</ol>