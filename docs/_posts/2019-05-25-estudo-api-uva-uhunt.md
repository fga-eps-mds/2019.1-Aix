---
layout: post
title: Estudo da API do UVa/uHunt
tags: estudo api uva webService 
category: Estudo
---
| Data       | Versão | Descrição                                   | Autor            |
| :--------: | :----: | :-----------------------------------------: | :--------------: |
| 11/05/2019 | 0.0.1  | Adição de FormActions no conteúdo             | Gabriela, Iuri, Pedro, Gustavo, André   |


# UVa e uHunt
&emsp;&emsp;
O [UVa](https://uva.onlinejudge.org/) é um juiz online onde é possível encontrar diversas questões de maratonas de programação, como as maratonas do [ICPC](https://icpc.baylor.edu/). Ele possui uma ferramenta complementar que funciona como interface para que o usuário possa ver suas estatíticas e visualizar os problemas de forma mais ordenada chamada [uHunt](https://uhunt.onlinejudge.org/id/0).

<!--more-->

## API uHunt
&emsp;&emsp;
Durante os estudos de como integrar o UVa ao bot foi validado que a API do uHunt seria o melhor modo, isto se dá ao fato de que ela possui ferramentas como conversão de username para id, listar as submissões de um usuário, entre outras funções que seriam úteis para nosso projeto. 

&emsp;&emsp;
Todos os dados da API do uHunt podem ser vista [aqui](https://uhunt.onlinejudge.org/api). Apesar da documentação não ter uma interface agradável, suas descrições e explicações não são mal desenvolvidas e sua utilização, devido à isso, é simples.

&emsp;&emsp;
No entanto, o uHunt não possui as funcionalidades de login e submissão de exercícios, nem em seu site, nem na API, o que nos levou a estudar o próprio site do UVa.

## WebService UVa
&emsp;&emsp;
Para conseguir utilizar o site do UVa e fazer as ações citadas foi necessário acessâ-lo de forma direta, a partir do request do site em um código python.

#### Acessando o UVa
&emsp;&emsp;
Para fazer o acesso do site foi criado uma ```session``` para que, desse modo, fosse possível realizar o ```post``` do login e após o ```post``` da submissão. Nessa sessão foi feito o ```get``` da url do site inicial do [UVa](https://uva.onlinejudge.org/). Após definir a sessão base, começamos a trabalhar nos ```posts```.

**Realizando o Login**
&emsp;&emsp;
Para realizar o login foi necessário gerar uma ```soup``` do texto adquirido do request da página inicial para que, a partir dele, pudéssemos ter acesso ao formulário encontrado na página e, desse modo, adquirir os parâmetros e a url necessários para realizar o login.
* Url para login: ```'https://uva.onlinejudge.org/index.php?option=com_comprofiler&task=login'```
* Parâmetros: ```'username'``` e ```'passwd'```

**Realizando a Submissão de exercícios**
&emsp;&emsp;
A submissão de exercícios não foi muito diferente do login, tendo ,em sua maioria, mudanças na url para gerar a ```soup``` e os parâmetros passados após o processamento da mesma. 
* Url para ```soup```: ```'https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25&page=submit_problem&problemid=' + id_do_problema```
* Url para submissão: ```'index.php?option=com_onlinejudge&Itemid=25&page=save_submission'```
* Parâmetros: ```'problemid'```, ```'category'```, ```'language'```, ```'codeupl'``` e ```'code'```
