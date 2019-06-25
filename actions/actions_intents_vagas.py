from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class ActionSetSlotValue(Action):
    def name(self):
        return "action_set_slot_value"

    def run(self, dispatcher, tracker, domain):
        last_intent_name = tracker.latest_message['intent'].get('name')
        slot_content = last_intent_name.replace('sobre_', '')
        slot_content = slot_content.replace('exemplo_', '')
        slot_content = slot_content.replace('codigo_em_python_', '')
        slot_content = slot_content.replace('exercicios_', '')
        slot_content = slot_content.replace('conteudo_extra_', '')

        return [SlotSet('conteudo', slot_content)]


class ActionUtterVaga(Action):
    def name(self):
        return "action_utter_vaga"

    def run(self, dispatcher, tracker, domain):
        return []

    def validate_subject(self, domain, desired_subject):
        try:
            domain['actions'].index(desired_subject)
            return True
        except ValueError:
            return False

    def dispatch_message(self, tracker, dispatcher, is_valid, desired_subject):
        if(is_valid):
            dispatcher.utter_template(desired_subject, tracker)
        else:
            dispatcher.utter_message('Santo capim! Acho que ainda' +
                                     ' não sei falar sobre esse conteúdo!' +
                                     ' Pois béem, tente me perguntar outra' +
                                     ' coisa')
        return is_valid


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
            return []
        else:
            desired_subject = 'utter_sobre_' + slot_content
            is_valid = self.validate_subject(domain, desired_subject)
            self.dispatch_message(tracker, dispatcher,
                                  is_valid, desired_subject)
            return []


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
            return []
        else:
            desired_subject = 'utter_exemplo_' + slot_content
            is_valid = self.validate_subject(domain, desired_subject)
            self.dispatch_message(tracker, dispatcher,
                                  is_valid, desired_subject)
            return []


class ActionUtterCodigoEmPythonVaga(ActionUtterVaga):
    def name(self):
        return "action_utter_codigo_em_python_vaga"

    def run(self, dispatcher, tracker, domain):
        slot_content = tracker.get_slot('conteudo')
        if(slot_content == 'erro'):
            dispatcher.utter_message('Estou confusa, bée...' +
                                     ' Você ainda não perguntou' +
                                     ' sobre nada! Defina um assunto' +
                                     ' primeiro!')
            return []
        else:
            desired_subject = 'utter_codigo_em_python_' + slot_content
            is_valid = self.validate_subject(domain, desired_subject)
            self.dispatch_message(tracker, dispatcher,
                                  is_valid, desired_subject)
            return []


class ActionUtterExerciciosVaga(ActionUtterVaga):
    def name(self):
        return "action_utter_exercicios_vaga"

    def run(self, dispatcher, tracker, domain):
        slot_content = tracker.get_slot('conteudo')
        slot_content = self.verify_if_is_variable(slot_content)

        if(slot_content == 'erro'):
            dispatcher.utter_message('Estou confusa, bée...' +
                                     ' Você ainda não perguntou' +
                                     ' sobre nada! Defina um assunto' +
                                     ' primeiro!')
            return []
        else:
            desired_subject = 'utter_exercicios_' + slot_content
            is_valid = self.validate_subject(domain, desired_subject)
            self.dispatch_message(tracker, dispatcher,
                                  is_valid, desired_subject)
            return []

    def verify_if_is_variable(self, slot_content):
        variable_types = ['inteiros', 'pontos_flutuantes', 'booleanos',
                          'caracteres', 'strings']
        if any(word == slot_content for word in variable_types):
            return 'variaveis'
        else:
            return slot_content


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
            return []
        else:
            desired_subject = 'utter_conteudo_extra_' + slot_content
            is_valid = self.validate_subject(domain, desired_subject)
            self.dispatch_message(tracker, dispatcher,
                                  is_valid, desired_subject)
            return []


class ActionUtterDesafioVaga(ActionUtterVaga):
    def name(self):
        return "action_utter_desafio_vaga"

    def run(self, dispatcher, tracker, domain):
        slot_content = tracker.get_slot('conteudo')
        if(slot_content == 'erro'):
            dispatcher.utter_message('Estou confusa, bée...' +
                                     ' Você ainda não perguntou' +
                                     ' sobre nada! Defina um assunto' +
                                     ' primeiro!')
            return []
        else:
            desired_subject = 'utter_desafio_' + slot_content
            is_valid = self.validate_subject(domain, desired_subject)
            self.dispatch_message(tracker, dispatcher,
                                  is_valid, desired_subject)
            return []
