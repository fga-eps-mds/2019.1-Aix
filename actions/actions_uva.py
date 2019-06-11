from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from actions import forms
from actions import api_uva


class UserForm(forms.CustomFormAction):
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


class CodeForm(forms.CustomFormAction):
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
        code = tracker.get_slot('codigo')
        problem = tracker.get_slot('problema')
        language = tracker.get_slot('linguagem')

        language = self.map_linguagem(language)

        if(language != 'erro'):
            response = api_uva.problem_submit(username=username,
                                              password=password,
                                              problem_num=str(problem),
                                              lang=str(language),
                                              user_code=str(code))
        else:
            response = 'erro'

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

    def map_linguagem(self, language):
        language = language.lower()
        if(language == 'c'):
            language = '1'
        elif(language == 'java'):
            language = '2'
        elif(language == 'c++'):
            language = '3'
        elif(language == 'pascal'):
            language = '4'
        elif(language == 'c++11' or language == 'c++ 11'):
            language = '5'
        elif(language == 'python3' or language == 'python 3'):
            language = '6'
        else:
            language = 'erro'
        return language


class ActionFeedbackSubmissao(Action):
    def name(self):
        return "action_feedback_submissao_uva"

    def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot('username')
        answer = api_uva.last_submit_result(username)

        next_content = """Se conseguiu: muito bem! Se não:
        tente encontrar seu erro e tente novamente.
        Você vai conseguir!\nSe você quiser, eu posso
        pesquisar alguma dúvida restante em um site de
        referência chamado StackOverflow!\nAinda não conhece
        o StackOverflow? Posso te explicar, é só me pedir!\n
        Ou caso você ache que já esteja pronto pro próximo conteúdo,
        me peça o cronograma e você poderá visualizar o próximo conteúdo.\n"""

        dispatcher.utter_message(answer)
        dispatcher.utter_message(next_content)
        return []
