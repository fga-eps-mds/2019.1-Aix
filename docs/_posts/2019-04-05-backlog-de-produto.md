---
layout: post
title: Backlog do Produto
tags: plano backlog documento eps
category: Produto
---
| Data       | Versão | Descrição                                   | Autor            |
| :--------: | :----: | :-----------------------------------------: | :--------------: |
| 17/04/2019 | 0.0.1  | Criação do backlog                  | Kamilla Costa   e Lucas Vitor |
| 22/04/2019 | 0.0.2  | Refatoração do backlog              | Kamilla Costa    |

Foram criado algumas personas para inserção das histórias de usuário como:
- Desenvolvedor: Responsável pelo desenvolvimento de funcionalidades do bot
- Usuário: Persona a quem se destina o uso do bot
- Administrador do bot: Responsável pela inserção de conteúdos no bot

Por experiências de sprints iniciais, o grupo optou por não levantar as tasks de forma que as mesmas serão deixar para definir as tasks de cada história na reunião de planejamento para evitar retrabalho uma vez que as definições se alteram muito ao decorrer da implementação das outras histórias.

## Épicos


<table>
  <tr>
   <td><strong>ID</strong>
   </td>
   <td><strong>DESCRIÇÃO</strong>
   </td>
  </tr>
  <tr>
   <td>EP01
   </td>
   <td>Sobre Aix
   </td>
  </tr>
  <tr>
   <td>EP02
   </td>
   <td>Instalação
   </td>
  </tr>
  <tr>
   <td>EP03
   </td>
   <td>Conteúdo
   </td>
  </tr>
  <tr>
   <td>EP04
   </td>
   <td>Linkagem
   </td>
  </tr>
  <tr>
   <td>EP05
   </td>
   <td>Primeiro Programa
   </td>
  </tr>
</table>

<!--more-->

## Features


<table>
  <tr>
   <td><strong>ID</strong>
   </td>
   <td><strong>DESCRIÇÃO</strong>
   </td>
   <td><strong>ÉPICO</strong>
   </td>
  </tr>
  <tr>
   <td>FT01
   </td>
   <td>Cumprimento/Despedida  Aix
   </td>
   <td>EP01
   </td>
  </tr>
  <tr>
   <td>FT02
   </td>
   <td>Apresentação de funcionalidades Aix
   </td>
   <td>EP01
   </td>
  </tr>
  <tr>
   <td>FT03
   </td>
   <td>Coleta de dados sobre ambiente de desenvolvimento
   </td>
   <td>EP02
   </td>
  </tr>
  <tr>
   <td>FT04
   </td>
   <td>Guia de instalação de dependências Python
   </td>
   <td>EP02
   </td>
  </tr>
  <tr>
   <td>FT05
   </td>
   <td>Apresentação Python
   </td>
   <td>EP03
   </td>
  </tr>
  <tr>
   <td>FT06
   </td>
   <td>Conteúdo sobre Variáveis
   </td>
   <td>EP03
   </td>
  </tr>
  <tr>
   <td>FT07
   </td>
   <td>Conteúdo sobre Estruturas Condicionais
   </td>
   <td>EP03
   </td>
  </tr>
  <tr>
   <td>FT08
   </td>
   <td>Conteúdo sobre Estruturas de repetição
   </td>
   <td>EP03
   </td>
  </tr>
  <tr>
   <td>FT09
   </td>
   <td>Conteúdo sobre Vetores
   </td>
   <td>EP03
   </td>
  </tr>
  <tr>
   <td>FT10
   </td>
   <td>Conteúdo sobre Matrizes
   </td>
   <td>EP03
   </td>
  </tr>
  <tr>
   <td>FT11
   </td>
   <td>Conteúdo sobre Funções
   </td>
   <td>EP03
   </td>
  </tr>
  <tr>
   <td>FT12
   </td>
   <td>Conteúdo sobre Arquivos
   </td>
   <td>EP03
   </td>
  </tr>
  <tr>
   <td>FT13
   </td>
   <td>Linkagem estática
   </td>
   <td>EP03
   </td>
  </tr>
  <tr>
   <td>FT14
   </td>
   <td>Linkagem conteúdo extra
   </td>
   <td>EP04
   </td>
  </tr>
  <tr>
   <td>FT15
   </td>
   <td>Linkagem erro
   </td>
   <td>EP04
   </td>
  </tr>
  <tr>
   <td>FT16
   </td>
   <td>Linkagem exercício
   </td>
   <td>EP04
   </td>
  </tr>
  <tr>
   <td>FT17
   </td>
   <td>Programando o primeiro Hello World
   </td>
   <td>EP05
   </td>
  </tr>
</table>



## Histórias de Usuários 


<table>
  <tr>
   <td>ID
   </td>
   <td>Descrição
   </td>
   <td>Feature
   </td>
  </tr>
  <tr>
   <td>IS01
   </td>
   <td>Eu, como usuário, desejo receber cumprimento do bot para dar início a conversa
   </td>
   <td>FT01
   </td>
  </tr>
  <tr>
   <td>IS02
   </td>
   <td>Eu, como usuário , desejo saber sobre  a Aix
   </td>
   <td>FT01
   </td>
  </tr>
  <tr>
   <td>IS03
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico para que o bot seja capaz de Manter uma conversa
   </td>
   <td>FT01
   </td>
  </tr>
  <tr>
   <td>IS04
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico para que o bot entre em Fallback quando necessário
   </td>
   <td>FT01
   </td>
  </tr>
  <tr>
   <td>IS05
   </td>
   <td>Eu, como usuário, desejo receber mensagem de despedida do bot para finalizar a conversa
   </td>
   <td>FT01
   </td>
  </tr>
  <tr>
   <td>IS06
   </td>
   <td>Eu, como usuário, desejo saber sobre as funcionalidades existentes no bot
   </td>
   <td>FT02
   </td>
  </tr>
  <tr>
   <td>IS07
   </td>
   <td>Eu, como usuário, desejo ser questionado quanto a existência de um ambiente de desenvolvimento configurado  
   </td>
   <td>FT03
   </td>
  </tr>
  <tr>
   <td>IS08
   </td>
   <td>Eu, como desenvolvedor, desejo coletar dados sobre o ambiente de desenvolvimento do usuário
   </td>
   <td>FT03
   </td>
  </tr>
  <tr>
   <td>IS09
   </td>
   <td>Eu, como usuário, desejo receber indicações de dependências do meu ambiente de desenvolvimento
   </td>
   <td>FT04
   </td>
  </tr>
  <tr>
   <td>IS10
   </td>
   <td>Eu, como usuário, desejo ser guiado na instalação das dependências do python
   </td>
   <td>FT04
   </td>
  </tr>
  <tr>
   <td>IS11
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico Sobre Python
   </td>
   <td>FT05
   </td>
  </tr>
  <tr>
   <td>IS12
   </td>
   <td>Eu, como usuário, desejo saber sobre Curiosidades da linguagem Python
   </td>
   <td>FT05
   </td>
  </tr>
  <tr>
   <td>IS13
   </td>
   <td>Eu, como usuário, desejo saber sobre Curiosidades da linguagem Python
   </td>
   <td>FT05
   </td>
  </tr>
  <tr>
   <td>IS14
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com a definição de variável para que o usuário compreenda o conteúdo.
   </td>
   <td>FT06
   </td>
  </tr>
  <tr>
   <td>IS15
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com exemplos de usos de variáveis em python para que o usuário compreenda o conteúdo.
   </td>
   <td>FT06
   </td>
  </tr>
  <tr>
   <td>IS16
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com um link para conteúdo extra sobre variáveis para que o usuário compreenda o conteúdo.
   </td>
   <td>FT06/FT13
   </td>
  </tr>
  <tr>
   <td>IS17
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com um link para sugestão de exercício sobre uso de variáveis para que o usuário compreenda o conteúdo.
   </td>
   <td>FT06/FT13
   </td>
  </tr>
  <tr>
   <td>IS18
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com a definição do que são estruturas condicionais para que o usuário compreenda o conteúdo.
   </td>
   <td>FT07
   </td>
  </tr>
  <tr>
   <td>IS19
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com exemplos de utilização de estruturas condicionais para que o usuário compreenda o conteúdo.
   </td>
   <td>FT07
   </td>
  </tr>
  <tr>
   <td>IS20
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico um link para conteúdo extra sobre estruturas condicionais para que o usuário compreenda o conteúdo.
   </td>
   <td>FT07/FT13
   </td>
  </tr>
  <tr>
   <td>IS21
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico um link para sugestão de exercício sobre uso de estruturas condicionais para que o usuário compreenda o conteúdo.
   </td>
   <td>FT07/FT13
   </td>
  </tr>
  <tr>
   <td>IS22
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com a definição do que são estruturas de repetição para que o usuário compreenda o conteúdo.
   </td>
   <td>FT08
   </td>
  </tr>
  <tr>
   <td>IS23
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com exemplos de utilização de estruturas de repetição para que o usuário compreenda o conteúdo.
   </td>
   <td>FT08
   </td>
  </tr>
  <tr>
   <td>IS24
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com um link para conteúdo extra sobre estruturas de repetição para que o usuário compreenda o conteúdo.
   </td>
   <td>FT08/FT13
   </td>
  </tr>
  <tr>
   <td>IS25
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com um link para sugestão de exercício sobre uso de estruturas de repetição para que o usuário compreenda o conteúdo.
   </td>
   <td>FT08/FT13
   </td>
  </tr>
  <tr>
   <td>IS26
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com a definição do que são vetores para que o usuário compreenda o conteúdo.
   </td>
   <td>FT09
   </td>
  </tr>
  <tr>
   <td>IS27
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com exemplos de utilização de vetores para que o usuário compreenda o conteúdo.
   </td>
   <td>FT09
   </td>
  </tr>
  <tr>
   <td>IS28
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com um link para conteúdo extra sobre vetores para que o usuário compreenda o conteúdo.
   </td>
   <td>FT09/FT13
   </td>
  </tr>
  <tr>
   <td>IS29
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com um link para sugestão de exercício sobre uso de vetores para que o usuário compreenda o conteúdo.
   </td>
   <td>FT09/FT13
   </td>
  </tr>
  <tr>
   <td>IS30
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com a definição do que são matrizes para que o usuário compreenda o conteúdo.
   </td>
   <td>FT10
   </td>
  </tr>
  <tr>
   <td>IS31
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com exemplos de utilização de matrizes para que o usuário compreenda o conteúdo.
   </td>
   <td>FT10
   </td>
  </tr>
  <tr>
   <td>IS32
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com um link para conteúdo extra sobre matrizes para que o usuário compreenda o conteúdo.
   </td>
   <td>FT10/FT13
   </td>
  </tr>
  <tr>
   <td>IS33
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com um link para sugestão de exercício sobre uso de matrizes para que o usuário compreenda o conteúdo.
   </td>
   <td>FT10/FT13
   </td>
  </tr>
  <tr>
   <td>IS34
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com a definição do que são funções para que o usuário compreenda o conteúdo.
   </td>
   <td>FT11
   </td>
  </tr>
  <tr>
   <td>IS35
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com exemplos de utilização de funções para que o usuário compreenda o conteúdo.
   </td>
   <td>FT11
   </td>
  </tr>
  <tr>
   <td>IS36
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com um link para conteúdo extra sobre funções para que o usuário compreenda o conteúdo.
   </td>
   <td>FT11/FT13
   </td>
  </tr>
  <tr>
   <td>IS37
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com um link para sugestão de exercício sobre uso de funções para que o usuário compreenda o conteúdo.
   </td>
   <td>FT11/FT13
   </td>
  </tr>
  <tr>
   <td>IS38
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com a definição do que são arquivos para que o usuário compreenda o conteúdo.
   </td>
   <td>FT12
   </td>
  </tr>
  <tr>
   <td>IS39
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com exemplos de utilização de arquivos para que o usuário compreenda o conteúdo.
   </td>
   <td>FT12
   </td>
  </tr>
  <tr>
   <td>IS40
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com um link para conteúdo extra sobre arquivos para que o usuário compreenda o conteúdo.
   </td>
   <td>FT12/FT13
   </td>
  </tr>
  <tr>
   <td>IS41
   </td>
   <td>Eu, como administrador do bot, desejo adicionar o tópico com um link para sugestão de exercício sobre uso de arquivos para que o usuário compreenda o conteúdo.
   </td>
   <td>FT12/FT13
   </td>
  </tr>
  <tr>
   <td>IS42
   </td>
   <td>Eu, como desenvolvedor, desejo procurar e estudar estrutura de sites confiáveis para estudos da linguagem
   </td>
   <td>FT14
   </td>
  </tr>
  <tr>
   <td>IS43
   </td>
   <td>Eu, como desenvolvedor, desejo criar crawler (ou ligação com a API) dos sites encontrados para conteúdo extra
   </td>
   <td>FT14
   </td>
  </tr>
  <tr>
   <td>IS44
   </td>
   <td>Eu, como desenvolvedor, desejo estudar estrutura da API do stackoverflow
   </td>
   <td>FT15
   </td>
  </tr>
  <tr>
   <td>TS45
   </td>
   <td>Eu, como desenvolvedor, desejo criar API para comunicação com a API do Stackoverflow
   </td>
   <td>FT15
   </td>
  </tr>
  <tr>
   <td>IS46
   </td>
   <td>Eu, como desenvolvedor, desejo estudar estrutura do URI e correlatos para verificação de viabilidade técnica
   </td>
   <td>FT16
   </td>
  </tr>
  <tr>
   <td>IS47
   </td>
   <td>Eu, como desenvolvedor, desejo criar crawler (ou ligação com a API) dos sites encontrados para recomendação de exercícios
   </td>
   <td>FT16
   </td>
  </tr>
  <tr>
   <td>IS48
   </td>
   <td>Eu, como usuário, desejo ser auxiliado na construção do meu primeiro programa ‘Hello Word’
   </td>
   <td>FT17
   </td>
  </tr>
</table>
