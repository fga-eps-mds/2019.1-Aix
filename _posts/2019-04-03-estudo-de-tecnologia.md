---
layout: post
title: Estudo de Tecnologia
tags: estudo tecnologia boilerplate eps mds
category: Projeto
---
# Estudo de Tecnologia Boilerplate

## Definições
* **Intent**: Inteção do usuário, "significado" da frase;
* **Utter**: Ação de resposta do bot; Mensagem que ele envia após identificar um intent;
* **Storie**: Conjunto de intents e utters, define o caminho que o Bot irá tomar na situação definida
* **Entities**: Quase como um assunto, conjunto de palavras que podem encaixar numa mesma intent
    * ex: entitie "Esporte" contém:
        * Futebol, Volei, Basquete

## Sintaxe: 

### Como elaborar uma intent:
Primeiramente é necessário atribuir um nome a intent. Para fazer isso coloca-se '## intent: ' e logo após os dois pontos o nome da intent.

	ex: ## intent:conversar

Após definir o título é necessário definir as frases que serão reconhecidas pelo bot para que interaja com o usuário. Uma dica importante é não repetir palavras e/ou frases. Sempre tentar utilizar palavras diferentes em cada frase. Antes de digitar cada frase é colocado um '-', após um espaço é escrita a frase. Uma frase por linha apenas.

	ex: ## intent:conversar
		- Preciso falar um coisa
		- Vamos bater um papo?
		- Quero te contar um segredo.

Para iniciar outra intent basta dar um enter, colocar '##' e definir título e frases para a intent.

### Como elaborar uma utter:
Assim como as Intents, as Utters necessitam de um título e este deve se relacionar a uma Intent. O título deve ser iniciado por "utter_" logo após é colocado o título que deve ser o mesmo título de uma intent existente e logo após ':'.
	
	ex: utter_conversar:

Logo na linha de baixo são adicionados os textos de resposta ao usuário assim que uma utter é chamada. É possível adicionar diversos textos. O bot, de forma aleatória escolherá qual irá utilizar. Para definir um texto resposta, coloca-se '- text: |'. Todas as palavras que vierem abaixo, até que se encontre uma próxima utter ou um próximo text, faz parte do texto.

	ex: utter_conversar:
		- text: |
			Oiii, quanto tempo!
			Sobre o que gostaria de falar?

		- text: |
			Tenhos muitas novidades..
			Nem sei por onde começar!

### Como elaborar uma storie:
Assim como as Intents e as Utters, as Stories também necessitam de título. Para criar um título utiliza-se '## ' logo após um espaço é definido o nome da storie ou caminho a ser seguido.

	ex: ## bater_um_papo

Após definir o título é necessário identificar as intents e respectivas utters que deverão ser seguidas, respectivamente. Para definir a intent que será utilizada colocamos '* ' e logo após o nome da intent. Na linha de baixo, pressiona-se Tab, coloca-se um '- ' e logo a pós a utter correspondente a intent adicionada. 

	ex: ## bater_um_papo
		* conversar
			- utter_conversar

Para que siga realmente uma história, são colocadas várias intents e utters que se complementem passando a ideia de que é uma pessoa quem está conversando.

	ex: ## batter_um_papo
		* cumprimentar
			- utter_cumprimentar
		* perguntar_como_esta
			- utter_perguntar_como_esta
		* perguntar_novidades
			-utter_perguntar_novidades



## Pastas e documentos importantes
* /bot/data/intents/ -> Local onde ficam as intents
* /bot/data/stories/ -> Local onde ficam as stories
* /bot/domain.yml -> Arquivo que lista as intents, entidades, utters e o templates das utters