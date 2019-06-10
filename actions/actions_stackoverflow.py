from rasa_core_sdk import Action
import requests
import json
import requests.exceptions


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

        try:
            result = requests.get(link, params=payload)
        except requests.exceptions.RequestException:
            return {}

        dictionary = json.loads(result.text)
        return dictionary

    def validate_links(self, dictionary):
        links = []
        if 'items' in dictionary:
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
        return []
