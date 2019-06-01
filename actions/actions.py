from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.forms import FormAction
from actions import api_uva
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


class UserForm(FormAction):
    def name(self):
        return "user_form"

    def required_slots(self, tracker):
        return ['username', 'password']

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Consegui receber os dados!')
        username = tracker.get_slot('username')
        password = tracker.get_slot('password')
        login = api_uva.make_login(username, password)
        if(login):
            dispatcher.utter_message('Login realizado com sucesso!')
        else:
            reset_slots = []
            reset_slots.append(SlotSet('username', None))
            reset_slots.append(SlotSet('password', None))
            dispatcher.utter_message('Falha ao tentar logar.\n' +
                                     'Verifique o username e o' +
                                     ' password!')
            return reset_slots

        return []


class ActionFeedbackSubmissao(Action):
    def name(self):
        return "action_feedback_submissao_uva"

    def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot('username')
        resposta = api_uva.resultado_ultima_submissao(username)
        next_content = "Se conseguiu: muito bem! Se não: tente encontrar seu erro e tente novamente. Você vai conseguir!\nSe você quiser, eu posso pesquisar alguma dúvida restante em um site de referência chamado StackOverflow!\nAinda não conhece o StackOverflow? Posso te explicar, é só me pedir!\nOu caso você ache que já esteja pronto pro próximo conteúdo, me peça o cronograma e você poderá visualizar o próximo conteúdo.\n"
        dispatcher.utter_message(resposta)
        dispatcher.utter_message(next_content)


class CodeForm(FormAction):
    def name(self):
        return "code_form"

    def required_slots(self, tracker):
        return ['problema', 'linguagem', 'codigo']

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Consegui receber o código!')
        username = tracker.get_slot('username')
        password = tracker.get_slot('password')
        if username is None:
            dispatcher.utter_message('Você esquece de fazer' +
                                     'login no UVa! Se conecte' +
                                     ' antes de submeter algo!')
            return []
        codigo = tracker.get_slot('codigo')
        problema = tracker.get_slot('problema')
        linguagem = tracker.get_slot('linguagem')
        response = api_uva.submeter_um_problema(username=username,
                                                password=password,
                                                problem_num=str(problema),
                                                lang=str(linguagem),
                                                codigo=str(codigo))
        if(response == 'UVa Online Judge'):
            dispatcher.utter_message('Submissão realizada!')
        else:
            dispatcher.utter_message('Béeeee, algo deu errado!!!' +
                                     ' Por favor tente novamente!')
        reset_slots = []
        reset_slots.append(SlotSet('codigo', None))
        reset_slots.append(SlotSet('problema', None))
        reset_slots.append(SlotSet('linguagem', None))

        return reset_slots


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
            dispatcher.utter_message('Santo capim! Acho que ainda' +
                                     'não sei falar sobre esse conteúdo!' +
                                     ' Pois béem, tente me perguntar outra' +
                                     'coisa')


class ActionUtterSobreVaga(ActionUtterVaga):
    def name(self):
        return "action_utter_sobre_vaga"

    def run(self, dispatcher, tracker, domain):
        slot_content = tracker.get_slot('conteudo')
        if(slot_content == 'erro'):
            dispatcher.utter_message('Estou confusa, bée...' +
                                     ' Você ainda não perguntou' +
                                     ' sobre nada! Defina um assunto' +
                                     ' primeiro!')
        else:
            desired_subject = 'utter_sobre_' + slot_content
            is_valid = self.validate_subject(domain, desired_subject)
            self.dispatch_message(tracker, dispatcher,
                                  is_valid, desired_subject)


class ActionUtterExemploVaga(ActionUtterVaga):
    def name(self):
        return "action_utter_exemplo_vaga"

    def run(self, dispatcher, tracker, domain):
        slot_content = tracker.get_slot('conteudo')
        if(slot_content == 'erro'):
            dispatcher.utter_message('Estou confusa, bée...' +
                                     ' Você ainda não perguntou' +
                                     ' sobre nada! Defina um assunto' +
                                     ' primeiro!')
        else:
            desired_subject = 'utter_exemplo_' + slot_content
            is_valid = self.validate_subject(domain, desired_subject)
            self.dispatch_message(tracker, dispatcher,
                                  is_valid, desired_subject)


class ActionUtterExerciciosVaga(ActionUtterVaga):
    def name(self):
        return "action_utter_exercicios_vaga"

    def run(self, dispatcher, tracker, domain):
        slot_content = tracker.get_slot('conteudo')
        if(slot_content == 'erro'):
            dispatcher.utter_message('Estou confusa, bée...' +
                                     ' Você ainda não perguntou' +
                                     ' sobre nada! Defina um assunto' +
                                     ' primeiro!')
        else:
            desired_subject = 'utter_exercicios_' + slot_content
            is_valid = self.validate_subject(domain, desired_subject)
            self.dispatch_message(tracker, dispatcher,
                                  is_valid, desired_subject)


class ActionUtterConteudoExtraVaga(ActionUtterVaga):
    def name(self):
        return "action_utter_conteudo_extra_vaga"

    def run(self, dispatcher, tracker, domain):
        slot_content = tracker.get_slot('conteudo')
        if(slot_content == 'erro'):
            dispatcher.utter_message('Estou confusa, bée...' +
                                     ' Você ainda não perguntou' +
                                     ' sobre nada! Defina um assunto' +
                                     ' primeiro!')
        else:
            desired_subject = 'utter_conteudo_extra_' + slot_content
            is_valid = self.validate_subject(domain, desired_subject)
            self.dispatch_message(tracker, dispatcher,
                                  is_valid, desired_subject)
