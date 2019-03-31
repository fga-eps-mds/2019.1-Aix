from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random

class ActionOTRS(Action):
  def name(self):
        return "action_otrs"
  def run(self, dispatcher, tracker, domain):
    try:
      dispatcher.utter_message("Mensagem enviada por uma custom action.")
    except ValueError:
      dispatcher.utter_message(ValueError)
  def createTicket(self, dispatcher, tracker, domain):
    #TODO
    return

  def closeTicket(self, dispatcher, tracker, domain):
    #TODO
    return