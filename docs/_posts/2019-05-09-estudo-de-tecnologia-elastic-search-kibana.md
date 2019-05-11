---
layout: post
title: Estudo de Tecnologia Elastic Search e Kibana
tags: estudo tecnologia elasticSearch kibana
category: Projeto
---

|Data|Versão|Descrição|Autor|
|:--:|:--:|:--:|:--:|
|11/05/2019| 1.0|Criação do documento de estudo de métricas para ElasticSearch e Kibana| Iuri|



# Estudo de Tecnologia - Elastic Search e Kibana

## Elastic Search
&emsp;&emsp;Elasticsearch é um software open source, que provê uma interface RESTful de pesquisa e análise de dados capaz de solucionar um número crescente de casos de uso.
Em conjunto com o Kibana, ele pode ser operado a partir dos requests existentes numa API RESTful com escrita em formato Json e permite a criação, edição e exclusão de dados, consultas básicas e análise básica de texto, incluindo uso de tokenizers e filtros.

&emsp;&emsp;Mais informações sobre as funções básicas e como instalar o Elastic Search e o Kibana pode ser encontradas na página oficial da Elastic, a partir do link [Elasticsearch: Introdução](https://www.elastic.co/pt/webinars/getting-started-elasticsearch?elektra=home&amp;storm=banner).

<!--more-->

## Kibana
&emsp;&emsp;Kibana é uma janela dentro do Elastic Stack que permite exploração visual e análise em tempo real dos dados no Elasticsearch. Fornece uma interface para que o usuário possa executar diversas funções do Elaticsearch e gerenciar esses dados da forma que achar mais conveniente, sendo possível a criação de diversos tipos de gráficos, mapas de coordenadas e outras formas de organização desses dados para visualização. Também é possível a criação de _dashboards_ para os tipos de visulização criadas, o que permite um melhor gerenciamentos e manuseabilidade dos tópicos selecionados, além de permitir um compartilhamento rápido dos mesmos.

&emsp;&emsp;Mais informações sobre as funções básicas e como instalar o Elastic Search e o Kibana pode ser encontradas na página oficial da Elastic, a partir do link [Introdução ao Kibana](https://www.elastic.co/pt/webinars/getting-started-kibana?baymax=rtp&elektra=products&storm=kibana&iesrc=ctr). 


## Aix + ElasticSearch + Kibana
&emsp;&emsp;Toda análise de dados que percorrem a Aix pode ser feita a partir da aplicação do ElasticSearch ao bot, com auxílio do Kibana para visualização desses dados. A conexão dessas ferramentas com o bot deve ser feita em um container exclusivo do docker, o qual as especificações de configuração podem ser geradas a partir de um código ```.py```. A partir disso, as métricas definidas para análise podem ser avaliadas, organizadas e dispostas em um dashboard com os gráficos disponibilizados pelo Kibana.

&emsp;&emsp;Um exemplo desse aplicação pode ser visto na [Tais](https://github.com/lappis-unb/tais), a assistente virtual do Ministério da Cultura, e no [Rasa Boilerplate](https://github.com/lappis-unb/rasa-ptbr-boilerplate), desenvolvido pelo [Lappis](https://github.com/lappis-unb).


## Métricas possíveis para análise
&emsp;&emsp;Uma métrica é uma medida quantificável usada para avaliar a qualidade do projeto e dessa forma melhorar o planejamento do mesmo.
Após discorrer sobre as diversas métricas possíveis de se validar, ficou decidido que seria de melhor viabilidade a análise das seguintes para o desenvolvimento da Aix:

- **Quantidade de usuários totais**

&emsp;&emsp;&emsp;&emsp;Medir a quantidade de usuários/sessões que já interagiram com a Tais. As medidas podem variar de acordo com o intervalo de tempo definido (por dia, por semana, por mês, ...).

- **Interações por usuário [IU]**

&emsp;&emsp;&emsp;&emsp;Quantificar a média de perguntas realizadas por usuário.

&emsp;&emsp;&emsp;&emsp;IU = (Qtd. total de perguntas do usuário) / (Qtd. total de usuários)

- **Horas com mais atividades**

&emsp;&emsp;&emsp;&emsp;Identificar em qual horário os usuários mais interagem com o bot. Definir por intervalo de tempo (De 11:00 às 12:30, etc).

- **Perguntas mais frequentes**

&emsp;&emsp;&emsp;&emsp;Analisar as perguntas que são feitas com mais frequências.

&emsp;&emsp;&emsp;&emsp;Neste caso, pode-se definir como a pergunta mais realizada em todo o tempo, ou então a pergunta que foi tendência em determinado intervalo de tempo.

- **Taxa de confusão (CR)**

&emsp;&emsp;&emsp;&emsp;Calcular a quantidade de _fallbacks_ em relação à quantidade de perguntas realizadas pelos usuários.

&emsp;&emsp;&emsp;&emsp;CR = (Qtd. de _fallbacks_) / (Qtd. total de perguntas)

- **Frases/palavras mais frequentes**

&emsp;&emsp;&emsp;&emsp;Analisar as frases/palavras que são mais realizadas. Neste caso, pode-se definir também como as palavras mais realizadas em todo o tempo, ou então a que foi tendência em determinado intervalo de tempo.

- **Fallback por intent**

&emsp;&emsp;&emsp;&emsp;Identificar quais são as intenções de usuários que mais geram _fallbacks_.

- **Fluxo de sessão**

&emsp;&emsp;&emsp;&emsp;Um fluxograma que mostra o "caminho" percorrido pelos usuários em cada sessão de conversa e a porcentagem de cada "caminho". Relacionando também com a métrica anterior de **_Fallback_ por intent**, a qual identifica em qual intenção o bot entrou no fallback.


Sendos essas métricas úteis tanto para negócios quanto para o desenvolvimento do bot em si.


## Referências
* [Elasticsearch: Introdução](https://www.elastic.co/pt/webinars/getting-started-elasticsearch?elektra=home&amp&storm=banner), acessado dia 09/05/2019
* [Introdução ao Kibana](https://www.elastic.co/pt/webinars/getting-started-kibana?baymax=rtp&elektra=products&storm=kibana&iesrc=ctr), acessado dia 09/05/2019
* [Tais - README](https://github.com/lappis-unb/tais/blob/master/README.md)
* [Estudo sobre metricas para bots](https://github.com/lappis-unb/tais/wiki/Estudo-sobre-metricas-para-bots)