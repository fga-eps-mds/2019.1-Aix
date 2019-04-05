---
layout: post
title: Plano de Gerenciamento de Custos
tags: plano custos documento eps
---
# Plano de Gerenciamento de Custos
---


## 1. Introdução

<p align="justify">Esse documento tem por objetivo identificar e documentar a forma como será feita a gerência de custos do projeto. Detalhando os processos para gerência de custos e regras de medição.

Ele basea-se na definição do PMBOK, que determina o Gerenciamento dos Custos do Projeto como o responsável por incluir os processos envolvidos em planejamento, estimativas, orçamentos, financiamentos, gerenciamento e controle dos custos, de modo que o projeto possa ser terminado dentro do orçamento aprovado. </p>
<!--more-->

## 2. Processos para Gerenciamento dos Custos do Projeto

<p align="justify">O  processo aqui descrito se basea no plano de gerenciamento de custo descrito no PMBOK. Ele compreende quatro fases: planejamento de custos, estimativa de custos, determinação de orçamento, controle de custos, abaixo está descrito a forma como cada uma das etapas será realizada no presente projeto. </p>

### 2.1. Estimar Custos

<p align="justify">Segundo o PMBOK, estimar os custos é desenvolver uma estimativa dos recursos necessários para executar as atividades do projeto, essas estimativas incluem a identificação e a consideração das alternativas de custo para iniciar e terminar o projeto.</p>

<p align="justify">Para auxiliar no processo de estimar custos, serão utilizadas as seguintes técnicas:</p>

- Estimativa Análoga: Esta estimativa se baseia na experiência dos membros da equipe em projetos semelhantes.

- Estimativa bottom-up: Esta estimativa se baseia na estrutura analítica do projeto para gerar estimativa de custos, partindo dos componentes de nível mais baixo da estrutura.

### 2.2. Determinar Orçamento

<p align="justify">Para determinar o valor do orçamento do projeto será feito o cálculo baseado no número de horas trabalhadas planejadas da equipe multiplicado pelo preço da hora. Logo, o orçamento será determinado por:</p>

                             Orçamento = Horas Trabalhadas * Preço da Hora

### 2.3. Controlar Custos

<p align="justify">O controle de custos será feito por meio da Gerência do valor da agregado(EVM) ao decorrer do projeto.</p>

<p align="justify">Para isso será necessário calcular algumas variáveis em alguns momentos do projeto. Por isso será necessário calcular três elementos: valor planejado (VP), valor agregado(VA) e o custo real (CR). A seguir será explicado um pouco sobre cada elemento:</p>

- Valor Planejado (VP)

    - O valor planejado será estimado a partir das horas, e será dado em reais. Sendo este o número de horas de trabalho planejadas para cada membro da equipe multiplicado pelo número de integrantes e o resultado desta operação multiplicado pelo custo da hora trabalhada.

- Valor Agregado(VA)

    - Valor agregado (VA) é a medida do trabalho executado expressa em termos do orçamento autorizado para tal trabalho. É o orçamento associado ao trabalho autorizado que foi concluído.

    - Ele é calculado por meio da multiplicação do valor planejado para a atividade pela porcentagem concluída da mesma atividade ao fim do tempo planejado.Tendo assim o valor agregado em reais.

- Custo Real(CR)

    - O custo real representa o quanto foi gasto na execução do trabalho, sendo este calculado a partir da multiplicação das horas gastas pelos integrantes do projeto pelo preço da hora trabalhada.

Com estas dimensões é possível realizar o cálculo da variação de custos e do índice de desempenho de custos, dois importantes indicadores para o gerenciamento do valor agregado.</p>

## 3. Regras de Medição e Desempenho

<p align="justify">A medição de desempenho dos custos ao decorrer do projeto será dada pelo Gerenciamento do valor Agregado(EVM), como foi dito. Para que esta análise seja mais precisa e quantificada deve se calcular dois índices de eficiência:</p>

- IDC - Índice de Desempenho de Custos
- IDP - Índice de Desempenho de Prazos

<p align="justify">O IDC mede a eficiência dos custos em relação ao orçamento planejado, ou seja, IDC = Valor Agregado/Custo Real. Para comparação e análise o IDC pode se enquadrar em três diferentes intervalos:</p>

|Valor|	Interpretação|
| :--: | :--: |
|IDC > 1|Custo mais baixo que o planejado|
|IDC = 1|Custo conforme planejado|
|IDC < 1|Custo mais alto que o planejado|

<p align="justify">Já o IDP mede a eficiência do cronograma do projeto, e é calculado dividindo o valor agregado pelo valor planejado, ou seja, IDP = VA/VP. Para comparação e análise o IDP pode se enquadrar em três diferentes intervalos:</p>

|Valor|	Interpretação|
| :--: | :--: |
|IDP > 1|Adiantado|
|IDP = 1|No prazo|
|IDP < 1|Atrasado|

<p align="justify">Para análise do valor agregado também existem outras duas importantes variáveis de desempenho que serão utilizadas durante o projeto para determinar a situação momentânea do projeto:</p>

- Variação de Prazos
- Variação de Custos

<p align="justify">A variação de prazos é uma medida de desempenho do cronograma expressa como a diferença entre o valor agregado e o valor planejado. É a quantidade de adiantamento ou atraso do projeto em relação à data de entrega planejada, em um determinado momento. É igual ao valor agregado (VA) menos o valor planejado (VP), ou seja, VPR = VA – VP.</p>

<p align="justify">A variação de custos(VC) é a quantidade de déficit ou excedente orçamentário em um determinado momento, expressa como a diferença entre o valor agregado(VA) e o custo real(CR), ou seja, VC = VA – CR. A VC é uma medida do desempenho dos custos em um projeto, e é particularmente crítica pois indica a relação entre o desempenho físico e os custos gastos.</p>


## 5. Bibliografia

> [GCS da equipe do Receita Mais](https://github.com/fga-eps-mds/2017.2-Receita-Mais/wiki/Plano-de-Gerenciamento-e-Configura%C3%A7%C3%A3o-de-Software)

> PMI. Um guia do conhecimento em gerenciamento de projetos. Guia PMBOK 6a. ed. - EUA: Project Management Institute, 2017.