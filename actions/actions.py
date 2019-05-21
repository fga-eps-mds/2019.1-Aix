from rasa_core_sdk import Action
import requests
import json


class ActionPesquisaStackoverflow(Action):
    def name(self):
        return "action_pesquisa_stackoverflow"

    def format_research(self, last_message):
        research = last_message
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

    def validate_links(self, dictionary):
        links = []
        for item in dictionary['items']:
            if str(item['is_answered']) == 'True':
                links.append(item['link'])
            if len(links) == 5:
                break
        return links

    def run(self, dispatcher, tracker, domain):
        last_message = tracker.latest_message['text']
        research = self.format_research(last_message)
        action_message = 'Então você quer saber sobre ' + research
        action_message += '... Vou ver o que acho aqui entre meus fenos!!'
        dispatcher.utter_message(action_message)
        dictionary = self.stackoverflow_request(research)
        links = self.validate_links(dictionary)

        if links:
            for link in links:
                dispatcher.utter_message(link)
        else:
            dispatcher.utter_message(
                'Bééé, infelizmente não encontrei nada ' +
                'sobre isso em minhas pesquisas. ' +
                'Poderia me perguntar com outras palavras?'
            )


class ActionSetSlotValue(Action):
    def name(self):
        return "action_set_slot_value"

    def run(self, dispatcher, tracker, domain):
        last_intent_name = tracker.latest_message['intent'].get('name')
        slot_content = last_intent_name.replace('sobre_', '')
        slot_content = slot_content.replace('exemplo_', '')
        slot_content = slot_content.replace('exercicios_', '')
        slot_content = slot_content.replace('conteudo_extra_', '')

        slot_content = self.verify_if_is_variable(slot_content)
        return [SlotSet('conteudo', slot_content)]

    def verify_if_is_variable(self, slot_content):
        variable_types = ['inteiros', 'pontos_flutuantes', 'booleanos', 
        'caracteres', 'strings']
        if any(word == slot_content for word in variable_types):
            return 'variaveis'
        else:
            return slot_content
        

class ActionUtterVaga(Action):
    def name(self):
        return "action_utter_vaga"  
        
    def run(self, dispatcher, tracker, domain):
        pass

    def validate_subject(self, domain, desired_subject):
        utter_index = domain['actions'].index(desired_subject)
        if(type(utter_index) is int):
            return True
        else:
            return False

    def dispatch_message(self, tracker, dispatcher, is_valid, desired_subject):
        if(is_valid):
            dispatcher.utter_template(desired_subject, tracker)
        else:
            dispatcher.utter_message('Santo capim! Acho que ainda não sei falar' +
            ' sobre esse conteúdo! Pois béem, tente me perguntar' +
            ' outra coisa')


class ActionUtterSobreVaga(ActionUtterVaga):
    def name(self):
        return "action_utter_sobre_vaga"

    def run(self, dispatcher, tracker, domain):
        slot_content = tracker.get_slot('conteudo')
        if(slot_content == 'erro'):
            dispatcher.utter_message('Estou confusa, bée... Você ainda não perguntou' +
            ' sobre nada! Defina um assunto primeiro!')
        else:
            desired_subject = 'utter_sobre_' + slot_content
            is_valid = self.validate_subject(domain, desired_subject)
            self.dispatch_message(tracker, dispatcher, is_valid, desired_subject)


class ActionUtterExemploVaga(ActionUtterVaga):
    def name(self):
        return "action_utter_exemplo_vaga"

    def run(self, dispatcher, tracker, domain):
        slot_content = tracker.get_slot('conteudo')
        if(slot_content == 'erro'):
            dispatcher.utter_message('Estou confusa, bée... Você ainda não perguntou' +
            ' sobre nada! Defina um assunto primeiro!')
        else:
            desired_subject = 'utter_exemplo_' + slot_content
            is_valid = self.validate_subject(domain, desired_subject)
            self.dispatch_message(tracker, dispatcher, is_valid, desired_subject)


class ActionUtterExerciciosVaga(ActionUtterVaga):
    def name(self):
        return "action_utter_exercicios_vaga"

    def run(self, dispatcher, tracker, domain):
        slot_content = tracker.get_slot('conteudo')
        if(slot_content == 'erro'):
            dispatcher.utter_message('Estou confusa, bée... Você ainda não perguntou' +
            ' sobre nada! Defina um assunto primeiro!')
        else:
            desired_subject = 'utter_exercicios_' + slot_content
            is_valid = self.validate_subject(domain, desired_subject)
            self.dispatch_message(tracker, dispatcher, is_valid, desired_subject)


class ActionUtterConteudoExtraVaga(ActionUtterVaga):
    def name(self):
        return "action_utter_conteudo_extra_vaga"

    def run(self, dispatcher, tracker, domain):
        slot_content = tracker.get_slot('conteudo')
        if(slot_content == 'erro'):
            dispatcher.utter_message('Estou confusa, bée... Você ainda não perguntou' +
            ' sobre nada! Defina um assunto primeiro!')
        else:
            desired_subject = 'utter_conteudo_extra_' + slot_content
            is_valid = self.validate_subject(domain, desired_subject)
            self.dispatch_message(tracker, dispatcher, is_valid, desired_subject)