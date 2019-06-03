---
layout: post
title: Estudo de Slots
tags: estudo slots customAction mds 
category: Estudo
---
| Data       | Versão | Descrição                                   | Autor            |
| :--------: | :----: | :-----------------------------------------: | :--------------: |
| 11/05/2019 | 0.0.1  | Criação do documento             | Gabriela, Iuri   |
| 25/05/2019 | 0.0.2  | Adição de FormActions no conteúdo             | Gabriela, Iuri, Pedro, Gustavo, André   |
| 29/05/2019 | 0.0.3  | Remoção de FormActions no conteúdo             |  Iuri  |

# Slots: o que são, de onde vem e o que fazem?

Segundo a documentação do [Rasa](https://rasa.com/docs/core/slots/), segue a descrição:

	
  

       "Slots são a memória do seu bot. Eles agem como um 
        armazenamento de valor-chave que pode ser usado
        para armazenar informações fornecidas pelo usuário 
        (por exemplo, sua cidade natal), bem como informações
        coletadas sobre o mundo exterior (por exemplo, o 
        resultado de uma consulta ao banco de dados)."

<!--more-->

Caso aja a necessidade de retornar ao usuário a previsão do tempo em sua localidade, por exemplo, como faz o projeto  [Gaia](https://github.com/BotGaia), seria interessante usarmos os slots para captar a região correspondente primeiramente, para que possamos, posteriormente, usar esse dado coletado para procurarmos as informações necessárias de retorno ao usuário. Afinal, para que possamos responder sobre o clima de um lugar, é necessário antes saber de qual local se trata.

## Tipos

<p align="justify"> &emsp;&emsp;
Existem diversos tipos de slots. Há os que influenciam no fluxo do bot, e os que não influenciam.</p>

**Temos as categorias:**
* **text:** preferências do usuário
* **bool:** valores binários. 
* **categorical:** opções de valores.
* **float:** para valores contínuos.
* **list:** armazena uma lista de valores.
* **unfeaturized:** não influencia o fluxo.

<p align="justify"> &emsp;&emsp;
Categóricos e booleanos são as categorias recomendadas para os slots importantes para o fluxo de conversa. Por outro lado, caso você queira apenas armazenar alguns dados, mas não quiser que isso afete o diálogo, use um unfeaturized slot.</p>

## Colocando a mão na massa
Para usarmos a ferramenta, é necessário seguirmos os seguintes passos:

**1.** adicionar no domain.yml a categoria slots.

**2.** adicionar o slot a lista de entidades.

**3.** criar as intents com exemplos de entidade.

**4.** criar as utters.

**5.** criar as stories.

### Exemplificando:

**Passo 1.** -domain.yml

    slots: 
      nome: 
	    type:
**P.S.:** em type será definido os tipos citados acima.

**Passo 2.** -domain.yml

    entities:
    	 - nome
**Passo 3.** -intents.md

    ## intent:preparo_r1
	    - o que a [Gabriela Lemos](nome) preparou para a R1
	    - o que o [Iuri Severo](nome) preparou para a R1
	    - o que o [Pedro Igor](nome) fez para a R1
	    - o que o [André](nome) fez para a R1
	    - o que o [Gustavo](nome) criou para a R1
	
Já o **Passo 4.** e o **Passo 5.** são usuais, de construção de utters e stories nos arquivos domain.yml e stories.md. Não tem segredo nenhum!

## Slots em uma Custom Action
&emsp;&emsp;
Outro modo de utilizar os slots é com uma Custom Action, a partir dos comandos ```SetSlot``` e ```tracker.get_slot```, como pode ser visto nos exemplos abaixo.
```
from rasa_core_sdk import Action

class TestSlot(Action):
    def name(self):
        return "action_test_slot"

    def run(self, dispatcher, tracker, domain):
        slot = tracker.get_slot('pesquisa')
        dispatcher.utter_message('Mensagem da custom action de teste')
        dispatcher.utter_message(slot)
```
```
from rasa_core_sdk.actions import Action
from rasa_core_sdk.events import SlotSet
import requests

class FetchProfileAction(Action):
    def name(self):
        return "fetch_profile"

    def run(self, dispatcher, tracker, domain):
        url = "http://myprofileurl.com"
        data = requests.get(url).json
        return [SlotSet("account_type", data["account_type"])]
```

# Teste de Slot
## Teste de nomes captados pela função **ActionIntegranteHorario** do **[Lappisudo](https://github.com/lappis-unb/lappisudo)**
* Bruna Nayara
```
Iuri Severo, [06.05.19 18:34]
Quando a Bruna Nayara está no Lappis?

Lappisudo, [06.05.19 18:34]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 18:34]
Tá aqui os horários de Bruna Nayara
```
<!--more-->

* Arthur Temporim
```
Iuri Severo, [06.05.19 18:35]
Quando o Arthur Temporim está no Lappis?

Lappisudo, [06.05.19 18:35]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 18:35]
Tá aqui os horários de Arthur Temporim
```

* Bruna Pinos
```
Lappisudo, [06.05.19 18:51]
Blz, vou me conectar ;)

Iuri Severo, [06.05.19 18:51]
quando a Bruna Pinos está no Lappis?

Lappisudo, [06.05.19 18:51]
Tá aqui os horários de Bruna Pinos
```

* Carla
```
Lappisudo, [06.05.19 18:52]
Blz, vou me conectar ;)

Iuri Severo, [06.05.19 18:52]
QUANDO A CARLA ESTÁ NO LAPPIS?

Lappisudo, [06.05.19 18:52]
Tá aqui os horários de Bruna Pinos

Lappisudo, [06.05.19 18:52]
Qual será nosso próximo assunto? Tente me perguntar algo aleatório, posso te surpreender com meus conhecimentos ;)

Lappisudo, [06.05.19 18:52]
Blz, vou me conectar ;)

Iuri Severo, [06.05.19 18:52]
Quando a Carla Rocha está no Lappis:

Lappisudo, [06.05.19 18:52]
Carla Rocha não tem horários na planilha

Lappisudo, [06.05.19 18:52]
Você tem mais alguma pergunta?

Lappisudo, [06.05.19 18:52]
Blz, vou me conectar ;)

Iuri Severo, [06.05.19 18:52]
Quando a Carla está no Lappis?

Lappisudo, [06.05.19 18:52]
Carla Rocha não tem horários na planilha
```

* Matheus Miranda
```
Lappisudo, [06.05.19 18:53]
Blz, vou me conectar ;)

Iuri Severo, [06.05.19 18:53]
Quando o Matheus Miranda está no Lappis?

Lappisudo, [06.05.19 18:53]
Matheus Miranda não tem horários na planilha

Lappisudo, [06.05.19 18:53]
Qual será nosso próximo assunto? Tente me perguntar algo aleatório, posso te surpreender com meus conhecimentos ;)

Lappisudo, [06.05.19 18:53]
Blz, vou me conectar ;)

Iuri Severo, [06.05.19 18:53]
Quando o Matheus está no Lappis?

Lappisudo, [06.05.19 18:53]
Matheus Miranda não tem horários na planilha
```

* Victor Moura
```
Lappisudo, [06.05.19 18:53]
Blz, vou me conectar ;)

Iuri Severo, [06.05.19 18:53]
Quando o Victor Moura está no Lappis?

Lappisudo, [06.05.19 18:53]
Tá aqui os horários de Victor Moura
```

* Guilherme Lacerda
```
Lappisudo, [06.05.19 18:53]
Blz, vou me conectar ;)

Iuri Severo, [06.05.19 18:54]
Quando o Guilherme Lacerda está no Lappis?

Lappisudo, [06.05.19 18:54]
Tá aqui os horários de Guilherme Lacerda
```

* Kamilla Costa
```
Lappisudo, [06.05.19 19:07]
Blz, vou me conectar ;)

Iuri Severo, [06.05.19 19:07]
Quando a Kamilla Costa está no Lappis?

Lappisudo, [06.05.19 19:07]
Kamilla Costa não tem horários na planilha

Lappisudo, [06.05.19 19:07]
Você tem mais alguma pergunta?

Lappisudo, [06.05.19 19:07]
Blz, vou me conectar ;)

Iuri Severo, [06.05.19 19:07]
Quando a Kamilla está no Lappis?

Lappisudo, [06.05.19 19:07]
Kamilla Costa não tem horários na planilha
```

> Após o nome não ser captado de forma correta, testei outras maneiras de escrevê-los para ver se o bot compreendia. Na maioria dos casos a resposta é negativa

### Teste de variação de escrita dos nomes já captados
> Os seguintes nomes foram captados com sucesso pela função:
* Bruna Nayara
* Arthur Temporim
* Bruna Pinos
* Victor Moura
* Guilherme Lacerda
> Continuando os testes, irei reescrevê-los variando caracteres maiúsculos, minúsculos, acentos e, em alguns casos, letras.

* Bruna Nayara
```
Iuri Severo, [06.05.19 19:16]
Quando a bruna nayara está no Lappis?

Lappisudo, [06.05.19 19:16]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:16]
Kamila Costa não tem horários na planilha

Lappisudo, [06.05.19 19:16]
Você tem mais alguma pergunta?

Iuri Severo, [06.05.19 19:17]
Quando a Bruna nayara está no Lappis?

Lappisudo, [06.05.19 19:17]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:17]
Kamila Costa não tem horários na planilha

Lappisudo, [06.05.19 19:17]
Você tem mais alguma pergunta?

Iuri Severo, [06.05.19 19:18]
Quando a bruna Nayara está no Lappis?

Lappisudo, [06.05.19 19:17]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:18]
Kamila Costa não tem horários na planilha

Lappisudo, [06.05.19 19:18]
Quer saber mais alguma coisa?

Iuri Severo, [06.05.19 19:18]
Quando a Bruna Naiara está no Lappis?

Lappisudo, [06.05.19 19:18]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:18]
Bruna Naiara não tem horários na planilha

Lappisudo, [06.05.19 19:18]
Qual será nosso próximo assunto? Tente me perguntar algo aleatório, posso te surpreender com meus conhecimentos ;)

Iuri Severo, [06.05.19 19:18]
Quando BRUNA NAYARA está no Lappis?

Lappisudo, [06.05.19 19:18]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:18]
Bruna Naiara não tem horários na planilha

Lappisudo, [06.05.19 19:18]
Qual será nosso próximo assunto? Tente me perguntar algo aleatório, posso te surpreender com meus conhecimentos ;)

Iuri Severo, [06.05.19 19:19]
Quando a Bruna Nayara está no Lappis?

Lappisudo, [06.05.19 19:19]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:19]
Tá aqui os horários de Bruna Nayara
```

* Arthur Temporim
```
Iuri Severo, [06.05.19 19:23]
Quando o arthur temporim está no lappis?

Lappisudo, [06.05.19 19:23]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:23]
Tá aqui os horários de Bruna Nayara

Lappisudo, [06.05.19 19:23]
Você tem mais alguma pergunta?

Iuri Severo, [06.05.19 19:23]
Quando o Arthur temporim está no lappis?

Lappisudo, [06.05.19 19:23]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:23]
Tá aqui os horários de Bruna Nayara

Lappisudo, [06.05.19 19:23]
Você tem mais alguma pergunta?

Iuri Severo, [06.05.19 19:23]
Quando o arthur Temporim está no lappis?

Lappisudo, [06.05.19 19:23]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:23]
Tá aqui os horários de Bruna Nayara

Lappisudo, [06.05.19 19:23]
Quer saber mais alguma coisa?

Iuri Severo, [06.05.19 19:24]
Quando o ARTHUR TEMPORIM está no lappis?

Lappisudo, [06.05.19 19:24]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:24]
Tá aqui os horários de Bruna Nayara

Lappisudo, [06.05.19 19:24]
Você tem mais alguma pergunta?

Iuri Severo, [06.05.19 19:24]
Quando o Artur Temporim está no lappis?

Lappisudo, [06.05.19 19:24]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:24]
Artur Temporim não tem horários na planilha

Lappisudo, [06.05.19 19:24]
Você tem mais alguma pergunta?

Iuri Severo, [06.05.19 19:24]
Quando o Arthur Temporim está no lappis?

Lappisudo, [06.05.19 19:24]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:24]
Tá aqui os horários de Arthur Temporim
```

* Victor Moura
```
Iuri Severo, [06.05.19 19:35]
Quando o victor moura está no Lappis?

Lappisudo, [06.05.19 19:35]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:35]
Tá aqui os horários de Arthur Temporim

Lappisudo, [06.05.19 19:35]
Você tem mais alguma pergunta?

Iuri Severo, [06.05.19 19:36]
Quando o Victor moura está no Lappis?

Lappisudo, [06.05.19 19:35]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:36]
Tá aqui os horários de Arthur Temporim

Lappisudo, [06.05.19 19:36]
Você tem mais alguma pergunta?

Iuri Severo, [06.05.19 19:36]
Quando o victor Moura está no Lappis?

Lappisudo, [06.05.19 19:36]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:36]
Tá aqui os horários de Arthur Temporim

Lappisudo, [06.05.19 19:36]
Você tem mais alguma pergunta?

Iuri Severo, [06.05.19 19:36]
Quando o VICTOR MOURA está no Lappis?

Lappisudo, [06.05.19 19:36]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:36]
Tá aqui os horários de Arthur Temporim

Lappisudo, [06.05.19 19:36]
Você tem mais alguma pergunta?

Iuri Severo, [06.05.19 19:37]
Quando o Vitor Moura está no Lappis?

Lappisudo, [06.05.19 19:37]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:37]
Vitor Moura não tem horários na planilha

Lappisudo, [06.05.19 19:37]
Você tem mais alguma pergunta?

Iuri Severo, [06.05.19 19:37]
Quando o Victor Moura está no Lappis?

Lappisudo, [06.05.19 19:37]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:37]
Tá aqui os horários de Victor Moura
```

> Pode-se reparar que os casos em que os dois nomes estão capitalizados (nome e sobrenome), o slot detecta corretamente os que foi escrito, porém, nos outros casos, o slot é dado como vazio e retorna o último texto detectado.

### Frases usadas na criação da intent da função
- quando que o [Eduardo Nunes](nome) vai estar no lappis
- [Victor Moura](nome)
- [Arthur Diniz](nome)
- [Francisco Matias](nome)
- me diga quando que [Fabíola Malta](nome) trabalha
- [Bruna Pinos](nome) vai trabalhar quais dias essa semana
- quais são os horários do [Arthur Temporim](nome) no lappis essa semana
- me informe os horarios da [Paloma](nome)
- [Gabriela](nome) trabalha quando essa semana
- horarios [Thalisson](nome)
- horários [Carla](nome)

#### Analisando Intent
> Após olhar a intent resolvi testar com uma frase exatamente igual a do exemplo.
O bot conseguiu captar o texto da slot da forma desejada, porém, quando o mesmo nome é aplicado em outra setença, o slot é tido como vazio.

```
Iuri Severo, [06.05.19 19:42]
horários Carla

Lappisudo, [06.05.19 19:41]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:42]
Carla não tem horários na planilha

Lappisudo, [06.05.19 19:42]
Quer saber mais alguma coisa?

Iuri Severo, [06.05.19 19:42]
horários Thalisson

Lappisudo, [06.05.19 19:42]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:42]
Tá aqui os horários de Thalisson

Lappisudo, [06.05.19 19:42]
Você tem mais alguma pergunta?

Iuri Severo, [06.05.19 19:42]
quando a Carla está no Lappis?

Lappisudo, [06.05.19 19:42]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:42]
Tá aqui os horários de Thalisson

Lappisudo, [06.05.19 19:42]
Você tem mais alguma pergunta?

Iuri Severo, [06.05.19 19:45]
quando o Pablo está no lappis?

Lappisudo, [06.05.19 19:45]
Blz, vou me conectar ;)

Lappisudo, [06.05.19 19:45]
Tá aqui os horários de Thalisson
```

> Outro ponto interessante que pode ser reparado a partir da intent da função é que a maioria dos nomes de exemplo são nomes compostos inicilializados com letra maiúscula, fato que segue o mesmo padrão de nomes que o slot consegue detectar.
> Casos mais específicos, como nomes únicos, só são percebidos nas frases exatas do exemplo.

|Quantidade de nomes compostos|Quantidade de nomes únicos|Total|
|:--:|:--:|:--:|
|7|4|11|
|63,64%|36,36%|100%|


## Conclusões dos testes realizados no bot
> Após reparar o padrão encontrado na função do Lappisudo, criei uma função de teste de slot na Aix, para verificar como ela reagia ao padrão notado.

* Teste de exemplos com uma palavra
	* Inicialmente o bot pareceu captar as palavras únicas inicializadas com letra maiúscula, porém essa detecção foi começando a falhar a medida que o teste se 
	seguia.
```
## intent:test_slot
- quero testar [Palavra](pesquisa)
- teste [Com](pesquisa)
- usar slot [Letra](pesquisa)
- teste para mim o slot [Maiúscula](pesquisa)
- entre no slot [No](pesquisa)
- quero fazer um teste da [Inicio](pesquisa)
- vou testar o slot de [Capitalizada](pesquisa)
```

```
Your input ->  Teste Capital                                                    
2019-05-07 11:55:56 DEBUG    rasa_core.tracker_store  - Recreating tracker for id 'default'
2019-05-07 11:55:56 DEBUG    rasa_core.processor  - Received user message 'Teste Capital' with intent '{'name': 'test_slot', 'confidence': 0.9124845862388611}' and entities '[{'start': 6, 'end': 13, 'value': 'Capital', 'entity': 'pesquisa', 'confidence': 0.5855489356445063, 'extractor': 'ner_crf'}]'
2019-05-07 11:55:56 DEBUG    rasa_core.processor  - Logged UserUtterance - tracker now has 179 events
2019-05-07 11:55:56 DEBUG    rasa_core.processor  - Current slot values: 
	pesquisa: Capital
2019-05-07 11:55:56 DEBUG    rasa_core.policies.memoization  - Current tracker state [{'prev_action_listen': 1.0, 'intent_test_slot': 1.0}, {'prev_action_test_slot': 1.0, 'intent_test_slot': 1.0}, {'prev_action_listen': 1.0, 'intent_test_slot': 1.0, 'entity_pesquisa': 1.0}]
2019-05-07 11:55:56 DEBUG    rasa_core.policies.memoization  - There is no memorised next action
2019-05-07 11:55:56 DEBUG    rasa_core.policies.ensemble  - Predicted next action using policy_0_KerasPolicy
2019-05-07 11:55:56 DEBUG    rasa_core.processor  - Predicted next action 'action_test_slot' with prob 1.00.
2019-05-07 11:55:56 DEBUG    rasa_core.actions.action  - Calling action endpoint to run action 'action_test_slot'.
2019-05-07 11:55:56 DEBUG    rasa_core.processor  - Action 'action_test_slot' ended with events '[]'
2019-05-07 11:55:56 DEBUG    rasa_core.processor  - Bot utterance 'BotUttered(text: Mensagem da custom action de teste, data: {
  "elements": null,
  "buttons": null,
  "attachment": null
})'
Mensagem da custom action de teste
2019-05-07 11:55:56 DEBUG    rasa_core.processor  - Bot utterance 'BotUttered(text: Capital, data: {
  "elements": null,
  "buttons": null,
  "attachment": null
})'
Capital
2019-05-07 11:55:56 DEBUG    rasa_core.policies.memoization  - Current tracker state [{'prev_action_test_slot': 1.0, 'intent_test_slot': 1.0}, {'prev_action_listen': 1.0, 'intent_test_slot': 1.0, 'entity_pesquisa': 1.0}, {'prev_action_test_slot': 1.0, 'intent_test_slot': 1.0, 'entity_pesquisa': 1.0}]
2019-05-07 11:55:56 DEBUG    rasa_core.policies.memoization  - There is no memorised next action
2019-05-07 11:55:56 DEBUG    rasa_core.policies.ensemble  - Predicted next action using policy_0_KerasPolicy
2019-05-07 11:55:56 DEBUG    rasa_core.processor  - Predicted next action 'action_listen' with prob 1.00.
2019-05-07 11:55:56 DEBUG    rasa_core.processor  - Action 'action_listen' ended with events '[]'
127.0.0.1 - - [2019-05-07 11:55:56] "POST /webhooks/rest/webhook?stream=true&token= HTTP/1.1" 200 255 0.066509
Your input ->  Teste Carro                                                      
2019-05-07 11:56:00 DEBUG    rasa_core.tracker_store  - Recreating tracker for id 'default'
2019-05-07 11:56:00 DEBUG    rasa_core.processor  - Received user message 'Teste Carro' with intent '{'name': 'test_slot', 'confidence': 0.9124845862388611}' and entities '[]'
2019-05-07 11:56:00 DEBUG    rasa_core.processor  - Logged UserUtterance - tracker now has 184 events
2019-05-07 11:56:00 DEBUG    rasa_core.processor  - Current slot values: 
	pesquisa: Capital
2019-05-07 11:56:00 DEBUG    rasa_core.policies.memoization  - Current tracker state [{'prev_action_listen': 1.0, 'intent_test_slot': 1.0, 'entity_pesquisa': 1.0}, {'prev_action_test_slot': 1.0, 'intent_test_slot': 1.0, 'entity_pesquisa': 1.0}, {'prev_action_listen': 1.0, 'intent_test_slot': 1.0}]
2019-05-07 11:56:00 DEBUG    rasa_core.policies.memoization  - There is no memorised next action
2019-05-07 11:56:00 DEBUG    rasa_core.policies.ensemble  - Predicted next action using policy_0_KerasPolicy
2019-05-07 11:56:00 DEBUG    rasa_core.processor  - Predicted next action 'action_test_slot' with prob 1.00.
2019-05-07 11:56:00 DEBUG    rasa_core.actions.action  - Calling action endpoint to run action 'action_test_slot'.
2019-05-07 11:56:00 DEBUG    rasa_core.processor  - Action 'action_test_slot' ended with events '[]'
2019-05-07 11:56:00 DEBUG    rasa_core.processor  - Bot utterance 'BotUttered(text: Mensagem da custom action de teste, data: {
  "elements": null,
  "buttons": null,
  "attachment": null
})'
2019-05-07 11:56:00 DEBUG    rasa_core.processor  - Bot utterance 'BotUttered(text: Capital, data: {
  "elements": null,
  "buttons": null,
  "attachment": null
})'Mensagem da custom action de teste

Capital
```

* Teste de exemplos com duas palavras
	* O bot consegue captar tanto palavras longas como palavras curtas, como por exemplo:
		* A B
		* Aaaaaaaaaaaaaaaaaaaaaa Bbbbbbbbbbbbbbbbbbbb

* Teste de exemplos com três palavras
	* O bot apresentou sucesso ao detectar as palavras nesse caso, pegando tanto palavras curtas como palavras longas, como por exemplo:
		* A B C
		* Aaaaaaaaaaaaaaaaaaaaaaaaaaa Bbbbbbbbbbbbbbbbbbbbbbbbb Cccccccccccccccccccc
```
## intent:test_slot
- quero testar [Palavra Composta Mais](pesquisa)
- teste [Muitas Coisas Maiusculas](pesquisa)
- usar slot [Ce Louco Meu](pesquisa)
- teste para mim o slot [Nao Sei Escrever](pesquisa)
- entre no slot [Algo Assim Saca](pesquisa)
- quero fazer um teste da [Ta E Doido](pesquisa)
- vou testar o slot de [Algo Com Sentido](pesquisa)
```

```
Your input ->  teste A B C                                                      
2019-05-07 12:29:43 DEBUG    rasa_core.tracker_store  - Recreating tracker for id 'default'
2019-05-07 12:29:43 DEBUG    rasa_core.processor  - Received user message 'teste A B C' with intent '{'name': 'test_slot', 'confidence': 0.6648008823394775}' and entities '[{'start': 6, 'end': 11, 'value': 'A B C', 'entity': 'pesquisa', 'confidence': 0.9141533469732314, 'extractor': 'ner_crf'}]'
2019-05-07 12:29:43 DEBUG    rasa_core.processor  - Logged UserUtterance - tracker now has 37 events
2019-05-07 12:29:43 DEBUG    rasa_core.processor  - Current slot values: 
	pesquisa: A B C
2019-05-07 12:29:43 DEBUG    rasa_core.policies.memoization  - Current tracker state [{'intent_test_slot': 1.0, 'prev_action_listen': 1.0, 'entity_pesquisa': 1.0}, {'intent_test_slot': 1.0, 'prev_action_test_slot': 1.0, 'entity_pesquisa': 1.0}, {'intent_test_slot': 1.0, 'prev_action_listen': 1.0, 'entity_pesquisa': 1.0}]
2019-05-07 12:29:43 DEBUG    rasa_core.policies.memoization  - There is no memorised next action
2019-05-07 12:29:43 DEBUG    rasa_core.policies.ensemble  - Predicted next action using policy_0_KerasPolicy
2019-05-07 12:29:43 DEBUG    rasa_core.processor  - Predicted next action 'action_test_slot' with prob 0.99.
2019-05-07 12:29:43 DEBUG    rasa_core.actions.action  - Calling action endpoint to run action 'action_test_slot'.
2019-05-07 12:29:43 DEBUG    rasa_core.processor  - Action 'action_test_slot' ended with events '[]'
2019-05-07 12:29:43 DEBUG    rasa_core.processor  - Bot utterance 'BotUttered(text: Mensagem da custom action de teste, data: {
  "elements": null,
  "buttons": null,
  "attachment": null
})'
2019-05-07 12:29:43 DEBUG    rasa_core.processor  - Bot utterance 'BotUttered(text: A B C, data: {
  "elements": null,
  "buttons": null,
  "attachment": null
})'Mensagem da custom action de teste

A B C
2019-05-07 12:29:43 DEBUG    rasa_core.policies.memoization  - Current tracker state [{'intent_test_slot': 1.0, 'prev_action_test_slot': 1.0, 'entity_pesquisa': 1.0}, {'intent_test_slot': 1.0, 'prev_action_listen': 1.0, 'entity_pesquisa': 1.0}, {'intent_test_slot': 1.0, 'prev_action_test_slot': 1.0, 'entity_pesquisa': 1.0}]
2019-05-07 12:29:43 DEBUG    rasa_core.policies.memoization  - There is no memorised next action
2019-05-07 12:29:43 DEBUG    rasa_core.policies.ensemble  - Predicted next action using policy_0_KerasPolicy
2019-05-07 12:29:43 DEBUG    rasa_core.processor  - Predicted next action 'action_listen' with prob 1.00.
2019-05-07 12:29:43 DEBUG    rasa_core.processor  - Action 'action_listen' ended with events '[]'
127.0.0.1 - - [2019-05-07 12:29:43] "POST /webhooks/rest/webhook?stream=true&token= HTTP/1.1" 200 253 0.039989
Your input ->  teste Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaa Bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
bbbbbbbbbbbbbbbbbbbbbb Ccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cccccccccccccccccc                                                              
2019-05-07 12:30:37 DEBUG    rasa_core.tracker_store  - Recreating tracker for id 'default'
2019-05-07 12:30:37 DEBUG    rasa_core.processor  - Received user message 'teste Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa Bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb Ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc' with intent '{'name': 'test_slot', 'confidence': 0.6648008823394775}' and entities '[{'start': 6, 'end': 243, 'value': 'Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa Bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb Ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc', 'entity': 'pesquisa', 'confidence': 0.9136730850566134, 'extractor': 'ner_crf'}]'
2019-05-07 12:30:37 DEBUG    rasa_core.processor  - Logged UserUtterance - tracker now has 43 events
2019-05-07 12:30:37 DEBUG    rasa_core.processor  - Current slot values: 
	pesquisa: Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa Bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb Ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
2019-05-07 12:30:37 DEBUG    rasa_core.policies.memoization  - Current tracker state [{'intent_test_slot': 1.0, 'prev_action_listen': 1.0, 'entity_pesquisa': 1.0}, {'intent_test_slot': 1.0, 'prev_action_test_slot': 1.0, 'entity_pesquisa': 1.0}, {'intent_test_slot': 1.0, 'prev_action_listen': 1.0, 'entity_pesquisa': 1.0}]
2019-05-07 12:30:37 DEBUG    rasa_core.policies.memoization  - There is no memorised next action
2019-05-07 12:30:37 DEBUG    rasa_core.policies.ensemble  - Predicted next action using policy_0_KerasPolicy
2019-05-07 12:30:37 DEBUG    rasa_core.processor  - Predicted next action 'action_test_slot' with prob 0.99.
2019-05-07 12:30:37 DEBUG    rasa_core.actions.action  - Calling action endpoint to run action 'action_test_slot'.
2019-05-07 12:30:37 DEBUG    rasa_core.processor  - Action 'action_test_slot' ended with events '[]'
2019-05-07 12:30:37 DEBUG    rasa_core.processor  - Bot utterance 'BotUttered(text: Mensagem da custom action de teste, data: {
  "elements": null,
  "buttons": null,
  "attachment": null
})'
2019-05-07 12:30:37 DEBUG    rasa_core.processor  - Bot utterance 'BotUttered(text: Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa Bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb Ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc, data: {
  "elements": null,
  "buttons": null,
  "attachment": null
})'
Mensagem da custom action de teste
Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa Bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb Ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
```




> Nenhum dos padrões observados é útil para o problema encontrado na Aix, sendo provável que, após mais analises, seja concluido que o método atual é o mais eficaz para nossas necessidades.

