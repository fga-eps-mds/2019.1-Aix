---
layout: post
title: Folha de Estilo
tags: folha estilo eps documento
---
# Folha de Estilo

Este documento define as convenção seguidas para a programação na linguagem python que serão utilizadas no presente projeto. Ele tem como base o [PEP8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/), porém apresenta algumas leves alterações para refletir melhor as necessidades da equipe.
Obervação: este documento pode sofrer alterações, caso seja evidenciado que alguma das convenções aqui descritas não se adequam da melhor forma ao contexto do projeto.
<!--more-->
## Layout do Código

### Identação

Usar 4 espaços por nível de identação (configurar tab para 4 espaços)

Como fazer:

    #Com argumentos no primeira linha:
    foo = long_function_name(var_one, var_two,
                             var_three, var_four)


    #Adicione 4 espaços extras para distinguir argumentos do resto (caso não fique na primeira linha):
    def long_function_name(
            var_one, var_two, var_three,
            var_four):
        print(var_one)


    #Sem argumentos na primeira linha:
    foo = long_function_name(
        var_one, var_two,
        var_three, var_four)

Como não fazer:

    #Argumentos na primeira linha são proibidos quando não utilizar alinhamento vertical:
    foo = long_function_name(var_one, var_two,
        var_three, var_four)

    #Identação dos argumentos não se distingue do resto do código:
    def long_function_name(
        var_one, var_two, var_three,
        var_four):
        print(var_one)

No caso de listas e dicionários, o fechamento deve ser feito abaixo do conteúdo, no mesmo nível da declaração da lista ou dicionário:

Como fazer:

    my_list = [
        1, 2, 3,
        4, 5, 6,
    ]

    my_dict = {
        "key1": "value1",
        "key2": "value2"
    }

Como não fazer:

    my_list = [
        1, 2, 3,
        4, 5, 6,]

    my_dict = {
        "key1": "value1",
        "key2": "value2"}


### Tamanho máximo de caracteres por linha

O tamanho máximo de caracteres por linha será de 79 caracteres.

Este número se deve a maior comodidade e adequação à maioria dos editores de texto, evitando a necessidade de scroll lateral no texto, permitindo, assim, uma visão melhor do código como um todo.

Em casos em que a linha ultrapasse o valor estipulado, a linha deverá ser quebrada (neste caso, será utilizado a continuação de linha implícita, através de parênteses, colchetes e chaves). Outra possibilidade é a utilização de barra invertida.

Exemplo:

    with open('/path/to/some/file/you/want/to/read') as file_1, \
        open('/path/to/some/file/being/written', 'w') as file_2:
        file_2.write(file_1.read())


### Quebra de linha em operadores binários

Caso necessário, será utilizado quebra de linha após o operador binário.

Como fazer:

    income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

Como não fazer:

    income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)


### Espaços em branco

Deverá existir dois espaços em branco entre as declarações de funções.

Como fazer:

    def function1():
        do_something()

    
    def function2():
        do_something_but_different()

Como não fazer:

    def function1():
        do_something()
    
    def function2():
        do_something_but_different()

Deverá existir um espaço em branco entre parágrafos de código.


### Imports

Os imports são sempre colocados na parte superior do arquivo, logo após os comentários de módulos e docstrings, e antes dos módulos globais e constantes.

Os imports devem ser agrupadas na seguinte ordem:

Imports de biblioteca padrão.
Imports de terceiros relacionadas.
Imports específicas de aplicativo / biblioteca local.

Imports devem ser feitos em linha separadas.

Como fazer:

    import os
    import sys

Como não fazer:

    import sys, os

Também é permitido desta forma:

    from subprocess import Popen, PIPE


## Aspas em Strings

Python não distigue entre aspas simples e duplas. Então por pura convenção, será utilizada aspas simples para Strings.

## Espaçamento entre declarações e expressões

Evite espaçamentos nos seguintes casos:
- Imediatamente dentro de parênteses, colchetes e chaves:

<!-- Forçando formatação -->
    Yes: spam(ham[1], {eggs: 2})

    No:  spam( ham[ 1 ], { eggs: 2 } )


- Entre uma vírgula final e um fechamento de parênteses:

<!-- Forçando formatação -->
    Yes: foo = (0,)

    No:  bar = (0, )


- Imediatamente antes de um vírgula, ponto e vírgula ou dois pontos:

<!-- Forçando formatação -->
    Yes: if x == 4: print x, y; x, y = y, x

    No:  if x == 4 : print x , y ; x , y = y , x


- Imediatamente antes de abertura de parênteses:

<!-- Forçando formatação -->
    Yes: spam(1)

    No:  spam (1)


- Imediatamente antes de indexação:

<!-- Forçando formatação -->
    Yes: dct['key'] = lst[index]

    No:  dct ['key'] = lst [index]


- Alinhamento entre operadores:

<!-- Forçando formatação -->
Como fazer:

    x = 1
    y = 2
    long_variable = 3

Como não fazer:

    x             = 1
    y             = 2
    long_variable = 3


## Comentários

Comentários que contradizem o código são piores do que comentários. Sempre priorize manter os comentários atualizados quando o código for alterado!

Comentários devem ser frases completas. A primeira palavra deve ser maiúscula, a menos que seja um identificador que comece com uma letra minúscula (nunca altere o caso dos identificadores!).

Os comentários de bloco geralmente consistem em um ou mais parágrafos construídos com sentenças completas, com cada sentença terminando em um período.

Os comentários devem seguir a língua do código.

### Blocos de comentários

Os blocos de comentários devem seguir a identação do código, e cada linha do comentário de começar com # e um espaço antes do texto.

### Comentários em linha

Devem ser separados em dois espaços do código, e começar com # e um espaço em branco antes do código.


## Convenções de nomenclatura

- Arquivos

Arquivos devem seguir o padrão snake case.

Exemplo:

    nlu_config.yml

- Classes

Classes devem seguir o padrão pascal case.

Exemplo:

    class ClassNameHere()

- Funções

Funções devem seguir o padrão camel case.

Exemplo:

    def functionNameHere()

- Variáveis

Variáveis devem seguir o padrão camel case.

Exemplo:

    int variableNameHere


- Constantes

Constantes devem seguir o padrão screaming snake case.

Exemplo:

    int CONSTANT_NAME_HERE

