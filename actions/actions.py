from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import json


class ActionPesquisaStackoverflow(Action):
    def name(self):
        return "action_pesquisa_stackoverflow"

    def format_research(self, tracker):
        research = tracker.latest_message['text']
        research = research.lower()
        research = research.replace('pesquise', '')
        research = research.replace('sobre', '')
        research = research.strip()

        return research

    def stackoverflow_request(self, research):
        link = 'https://api.stackexchange.com/2.2/search'
        order = 'desc'
        sort = 'activity'
        intitle = research
        site = 'stackoverflow'

        payload = {
            'order': order, 'sort': sort, 'intitle': intitle, 'site': site
        }

        result = requests.get(link, params=payload)
        dictionary = json.loads(result.text)

        return dictionary

    def dispatch_links(self, dictionary, dispatcher):
        links = []
        for item in dictionary['items']:
            if str(item['is_answered']) == 'True':
                links.append(item['link'])
            if len(links) == 5:
                break
        if links:
            for link in links:
                dispatcher.utter_message(link)
        else:
            dispatcher.utter_message(
                'Bééé, infelizmente não encontrei nada ' +
                'sobre isso em minhas pesquisas. ' +
                'Poderia me perguntar com outras palavras?'
            )

    def run(self, dispatcher, tracker, domain):
        research = self.format_research(tracker)
        action_message = 'Então você quer saber sobre ' + research
        action_message += '... Vou ver o que acho aqui entre meus fenos!!'
        dispatcher.utter_message(action_message)
        dictionary = self.stackoverflow_request(research)
        self.dispatch_links(dictionary, dispatcher)

class ActionSobre(Action):
  def name(self):
    return "action_sobre"



  def run(self, dispatcher, tracker, domain):
    text = tracker.latest_message['text']
    text.lower()
    slot_value = tracker.get_slot('conteudo')

    if('aix' in text):
        dispatcher.utter_template('utter_sobre_aix', tracker)
        return [SlotSet('conteudo', 'aix')]

    elif('python' in text):
        dispatcher.utter_template('utter_sobre_python', tracker)
        return [SlotSet('conteudo', 'python')]

    elif('variave' in text):
        dispatcher.utter_template('utter_sobre_variaveis', tracker)
        return [SlotSet('conteudo', 'variaveis')]

    elif('inteiro' in text):
        dispatcher.utter_template('utter_sobre_inteiros', tracker)
        return [SlotSet('conteudo', 'inteiros')]

    elif('flutuante' in text or 'float' in text or 'double' in text):
        dispatcher.utter_template('utter_sobre_pontos_flutuantes', tracker)
        return [SlotSet('conteudo', 'pontos_flutuantes')]

    elif('caracter' in text or 'char' in text):
        dispatcher.utter_template('utter_sobre_caracteres', tracker)
        return [SlotSet('conteudo', 'caracteres')]

    elif('bool' in text or 'boleano' in text):
        dispatcher.utter_template('utter_sobre_booleanos', tracker)
        return [SlotSet('conteudo', 'booleanos')]

    elif('condic' in text):
        dispatcher.utter_template('utter_sobre_condicionais', tracker)
        return [SlotSet('conteudo', 'condicionais')]

    elif('arquivo' in text):
        dispatcher.utter_template('utter_sobre_arquivos', tracker)
        return [SlotSet('conteudo', 'arquivos')]

    elif('repetic' in text or 'repetiç' in text):    
        dispatcher.utter_template('utter_sobre_repeticao', tracker)
        return [SlotSet('conteudo', 'repeticao')]

    elif('func' in text or 'funç' in text):
        dispatcher.utter_template('utter_sobre_funcao', tracker)
        return [SlotSet('conteudo', 'funcao')]

    elif('vetor' in text):
        dispatcher.utter_template('utter_sobre_vetores', tracker)
        return [SlotSet('conteudo', 'vetores')]

    elif('matriz' in text):
        dispatcher.utter_template('utter_sobre_matrizes', tracker)
        return [SlotSet('conteudo', 'matrizes')]

    elif('world' in text):
        dispatcher.utter_template('utter_sobre_hello_world', tracker)
        return [SlotSet('conteudo', 'hello_world')]
    
    elif('biblioteca' in text):
        dispatcher.utter_template('utter_sobre_importar_bibliotecas', tracker)
        return [SlotSet('conteudo', 'importar_bibliotecas')]

    elif(slot_value == 'erro'):
        dispatcher.utter_message('Erro')

    else:
        utter_text = 'utter_sobre_' + slot_value
        dispatcher.utter_template(utter_text, tracker)