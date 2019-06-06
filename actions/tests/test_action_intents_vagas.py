import logging

import requests
import json

import pytest
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from rasa_core.channels import OutputChannel
from rasa_core.nlg import NaturalLanguageGenerator
from rasa_core_sdk import Tracker
from rasa_core.domain import Domain
from rasa_core.dispatcher import Dispatcher

from actions.actions import ActionSetSlotValue

@pytest.fixture
def custom_set_slot_value():
    return ActionSetSlotValue()

@pytest.fixture
def custom_domain():
    return Domain({}, [], [], {}, ['utter_sobre_vetores', 
    			  'utter_exemplo_vetores', 'utter_exercicios_vetores',
    			  'utter_conteudo_extra_vetores', 
    			  'utter_codigo_em_python_vetores'], [])

@pytest.fixture
def custom_tracker():
    return Tracker('', {}, {'intent':{'name':'sobre_vetores'}},
    							'', '', '', {}, '')

@pytest.fixture
def custom_dispatcher():
    return Dispatcher('', OutputChannel(), NaturalLanguageGenerator())

def test_name_action_set_slot_value(custom_set_slot_value):
	name = custom_set_slot_value.name()
	assert name == 'action_set_slot_value'

def test_verify_if_is_variable(custom_set_slot_value):
	variavel = 'strings'
	vetores = 'vetores'
	assert (custom_set_slot_value.verify_if_is_variable(variavel) ==
		   'variaveis')
	assert (custom_set_slot_value.verify_if_is_variable(vetores) ==
		   vetores)

def test_run_action_set_slot_value(custom_set_slot_value, custom_dispatcher,
								   custom_tracker, custom_domain):
	slot = custom_set_slot_value.run(custom_dispatcher,
									 custom_tracker, custom_domain)
	assert slot == [{"event": "slot", "timestamp": None,
					 "name": "conteudo", "value": "vetores"}]