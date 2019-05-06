from rasa_core_sdk import Action
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
        dispatcher.utter_message(action_message);
        dictionary = self.stackoverflow_request(research)
        self.dispatch_links(dictionary, dispatcher)