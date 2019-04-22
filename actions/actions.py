from rasa_core_sdk import Action
import requests
import json


class ActionOTRS(Action):
    def name(self):
        return "action_otrs"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message(
                "Mensagem enviada por uma custom action!!")
        except ValueError:
            dispatcher.utter_message(ValueError)

    def createTicket(self, dispatcher, tracker, domain):
        # TODO
        return

    def closeTicket(self, dispatcher, tracker, domain):
        # TODO
        return


class ActionPesquisaStackoverflow(Action):
    def name(self):
        return "action_pesquisa_stackoverflow"

    def run(self, dispatcher, tracker, domain):
        pesquisa = tracker.latest_message['text']
        pesquisa = pesquisa.replace('pesquise', '')
        pesquisa = pesquisa.replace('sobre', '')
        pesquisa = pesquisa.strip()
        dispatcher.utter_message('Então você quer saber sobre ' +
                                 pesquisa + '''... Vou ver o que acho \
                                 aqui entre meu fenos!''')

        if str(type(pesquisa)) != "<class 'NoneType'>":
            link = """
            https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=
            """
            site = '&site=stackoverflow'
            resultado = requests.get(link+str(pesquisa)+site)
            dicionario = json.loads(resultado.text)
            links = []
            for item in dicionario['items']:
                if str((item)['is_answered']) == 'True':
                    links.append(item['link'])
                if len(links) == 5:
                    break
            if links:
                for link in links:
                    dispatcher.utter_message(link)
            else:
                dispatcher.utter_message("""
                    Bééé, infelizmente não encontrei nada
                    sobre isso em minhas pesquisas.
                    Poderia me perguntar com outras palavras?""")
