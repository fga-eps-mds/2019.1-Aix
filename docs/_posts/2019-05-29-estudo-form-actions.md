---
layout: post
title: Estudo de FormActions
tags: estudo formActions customAction mds 
category: Estudo
---
| Data       | Versão | Descrição                                   | Autor            |
| :--------: | :----: | :-----------------------------------------: | :--------------: |
| 29/05/2019 | 0.0.1  | Criação do documento             |  Iuri   |


## FormActions
&emsp;&emsp;
Uma das ações mais comuns em conversas é receber uma lista de dados, como por exemplo, o nome, telefone e cpf de um usuário. Os FormActions foram feitos para isso, coletar múltiplos dados do usuário durante a conversa. No site do [Rasa na parte de Forms](https://rasa.com/docs/rasa/core/forms/) eles usam de exemplo uma conversação na qual o usuário deseja pesquisar por um restaurante, esse exemplo pode ser encontrado [aqui](https://github.com/RasaHQ/rasa_core/tree/master/examples/formbot).

### Utilizando FormActions
&emsp;&emsp;
A implementação de um FormAction no bot não é muito diferente dos Slots em si, apesar dele utilizar dos slots para funcionar. Para criar um Form é necessário seguir os seguintes passos:

**1.** Adicionar o "FormPolicy" nas políticas (policies) do Bot
```
policies:
  - name: "FormPolicy"
```

**2.** Declarar o Form no arquivo ```domain.yml```
```
forms:
  - restaurant_form
```

**3.** Criar a intent e stories de acesso ao Form
```
## happy path
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
```
De acordo com o Rasa, é necessário definir o form usado, como mostrado no exemplo, e após o uso declarar ```form{"name": null}``` para finalizar o uso

**4.** Implementar a classe do FormAction nas custonActions do bot
* A classe deverá herdar os dados da classe ```FormAction```, que deverá ser importada no início do código;
* Ela deve possuir as funções ```name```, ```required_slots``` e ```submit```;

As funções serão explicadas no código de exemplo

É recomendado que os slots utilizados sejam do tipo ```unfeaturized``` 

O FormAction só fará requisição de slots ainda não preenchidos.

```
class UserForm(FormAction):
    # Define o nome do form para que o mesmo seja
    # utilizado dentro do arquivo domain.yml
    def name(self):
        return "user_form"

    # Define quais slots fazem parte do formulário
    # ou seja,  quais dados você quer do usuário
    def required_slots(self, tracker):
        return ['username', 'password']

    # Ação realizada pelo bot após receber
    # todos os slots requisitados
    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Coletei todos os slots!')
        # O submit deve retornar uma lista
        # Caso não haja retorno na função,
        # basta colocar uma lista vazia
        return []
```

**5.** É necessário criar uma utter ```utter_ask_{slot_name}``` para cada slot requisitado pelo Form;

**6.** É necessário criar uma intent com nome ```inform``` onde devem ser listados os exemplos de frases com os slots requisitados;

Após alguns testes, foi validado que é possível usar mais de um Form na intent ```inform```

**7.** Caso nada seja extraido do slot, será acionada a action ```ActionExecutionRejection```

Para mais informações sobre FormActions, o Rasa disponibiliza sua documentação na página de [Form](https://rasa.com/docs/rasa/core/forms/) deles.