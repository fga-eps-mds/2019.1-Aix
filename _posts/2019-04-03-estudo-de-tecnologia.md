---
layout: post
title: Estudo de Tecnologia
tags: estudo tecnologia boilerplate eps mds
---
# Estudo de Tecnologia Boilerplate

## Definições
* **Intent**: Inteção do usuário, "significado" da frase;
* **Utter**: Ação de resposta do bot; Mensagem que ele envia após identificar um intent;
* **Storie**: Conjunto de intents e utters, define o caminho que o Bot irá tomar na situação definida
* **Entities**: Quase como um assunto, conjunto de palavras que podem encaixar numa mesma intent
    * ex: entitie "Esporte" contém:
        * Futebol, Volei, Basquete

## Pastas e documentos importantes
* /bot/data/intents/ -> Local onde ficam as intents
* /bot/data/stories/ -> Local onde ficam as sotires
* /bot/domain.yml -> Arquivo que lista as intents, entidades, utters e o templates das utters