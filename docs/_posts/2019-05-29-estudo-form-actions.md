---
layout: post
title: Estudo de FormActions
tags: estudo formActions customAction mds 
category: Estudo
---
| Data       | Versão | Descrição                                   | Autor            |
| :--------: | :----: | :-----------------------------------------: | :--------------: |
| 29/05/2019 | 0.0.1  | Criação do documento             |  Iuri   |
| 31/05/2019 | 0.0.2  | Inserção de dos sobre a implementação do FormAction             |  André, Iuri   |


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


### Implementação dos FormActions
&emsp;&emsp;
A implementação dos Forms pode ser encontrada no github do [Rasa](https://github.com/RasaHQ/rasa-sdk), tendo a base do Form e o FormValidation no arquivo ```events.py``` e a implementação no arquivo ```forms.py```.
&emsp;&emsp;
Dentro do arquivo ```forms.py``` tem a classe ```FormAction```, que possui herança da classe ```Action```, e que é a base desse estudo. Logo no início do arquivo também ser visto a variável ```REQUESTED_SLOT``` que possui o valor ```"requested_slot"```, sendo ela uma constate para o nome do slot que guarda a lista de slots que o formulário irá utilizar.

A classe possui as seguintes funções:
* ```name(self)```: Por padrão do Rasa, é uma função obrigatória em todas Actions é define o nome da mesma.
* ```required_slots(tracker)```: Retorna a lista de slots que o formulário deve preencher, sendo essa uma função obrigatória em todos os FormActions.
* ```from_entity(self, entity, intent=None, not_intent=None)``` : Retorna um dicionário para mapear o modo de extração dos slots.
* ```from_trigger_intent(self, value, intent=None, not_intent=None)``` : Retorna um dicionário para mapear o modo de extração dos slots.
* ```from_intent(self, value, intent=None, not_intent=None)``` : Retorna um dicionário para mapear o modo de extração dos slots.
* ```from_text(self, intent=None, not_intent=None)``` : Retorna um dicionário para mapear o modo de extração dos slots.
* ```slot_mappings(self)```: Retorna um dicionário que mapeia os slots requeridos pelo forms.
* ```get_mappings_for_slot(self, slot_to_fill)```: Retorna uma lista de dicionários que mapeia os slots requeridos com o modo como devem ser extraídos.
* ```intent_is_desired(requested_slot_mapping, tracker)```: Valida se a intent do usuário combina com as condições de intent do formulário.
* ```get_entity_value(name, tracker)```: Verfica se uma entidade específica já está preenchida e, caso esteja, extrai seu valor.
* ```extract_other_slots(self, dispatcher, tracker, domain)```: Extrai o valor dos slots definidos pelo usuário como "subslots" de algum slot listado entre os requeridos.
* ```extract_requested_slot(self, dispatcher, tracker, domain)```: Extrai o valor dos slots necessário para o formulário. Utiliza o mapa gerado pelas outras funções para válidar os slots desejados e como extraí-los. Retorna um dicionário com os valores.
* ```validate_slots(self, slot_dict, dispatcher, tracker, domain)```: Valida os slots utilizando as funções de ajuda de validação. Chama a função ```validade_{slot}``` para cada um dos slots e, caso a função não esteja implementada, define o slot com o valor mapeado.
* ```validate(self, dispatcher, tracker, domain)```: Extrai e valida o valor de cada slot. Caso nenhum valor seja extraído, retorna a execução de rejeição da FormAction.
    * Pode ser sobrescrita para customizar a validação e o retorno.
* ```request_next_slot(self, dispatcher, tracker, domain)```: Solicita o próximo slot listado e o template da utter, se necessário. Caso não haja mais slots, retorna ``None```.
* ```deactivate(self)```: Retorna um evento `Form` com nome ```None``` para desativar o formulário e resetar os slots.
* ```submit(self, dispatcher, tracker, domain)```: Define quais ações serão tomadas após a extração dos valores dos slots.
* ```_to_list(x)```: Converte um objeto para uma lista, caso seja algo do tipo ```None```, retorna uma lista vazia.
* ```_list_intents(self, intent=None,     not_intent=None)```: Verifica se uma intent pode ou não ser acessada durante o preenchimento do formulário.
* ```_log_form_slots(self, tracker)```: Registra os valores de todos os slots necessários antes de enviar o formulário.
* ```_activate_if_required(self, dispatcher, tracker, domain)```: Ativa o formulário caso ele tenha sido chamado pela primeira vez. Se ativado, valida os slots necessários que foram preenchidos antes da ativação do formulário e retorna o evento `Form` com o nome do formulário, bem como qualquer evento `SlotSet` da validação de slots pré-preenchidos.
* ```_validate_if_required(self, dispatcher, tracker, domain)```: Retorna uma lista de eventos do tipo ```self.validate(...)``` e se a validação é requerida:
    * o formulário é ativado;
    * o formulário é chamado após a `action_listen`;
    * a validação do formulário não é cancelada.
* ``` _should_request_slot(tracker, slot_name)```: Verifica se a ação do formulário deve solicitar o slot fornecido
* ```run(self, dispatcher, tracker, domain)```: Executa os efeitos colaterais do formulário. Passos:
    * Ativa o ```Form```, se necessário;
    * Valida a entrada do usuário, se necessário;
    * Define os slots validados;
    * Template utter_ask_{slot} ativada para o próximo slot;
    * Entra na função ```submit``` caso os slots estejam preenchidos;
    * Desativa o formulário.
* ```__str__(self)```: Define o modo como o formulário é printado.
