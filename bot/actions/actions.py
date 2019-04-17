from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random

class ActionOTRS(Action):
    def name(self):
        return "action_otrs"
    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message("Mensagem enviada por uma custom action!")
        except ValueError:
            dispatcher.utter_message(ValueError)
    def createTicket(self, dispatcher, tracker, domain):
        #TODO
        return

    def closeTicket(self, dispatcher, tracker, domain):
        #TODO
        return

class ActionPesquisarNoStackoverflow(Action):
    def name(self):
        return "action_pesquisar_no_stackoverflow"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Conferindo...")
        pesquisa = tracker.get_slot('pesquisa')
        dispatcher.utter_message(pesquisa)
        x = tracker.current_slot_values()['pesquisa']
        dispatcher.utter_message(x)
