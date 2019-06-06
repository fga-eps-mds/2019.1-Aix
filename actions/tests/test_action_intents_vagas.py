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
def custom_domain():
    return {'intent_properties' : {}, 'entities' : [],
    		'slots' : ['conteudo'], 'templates' : {}, 'actions' :
    		['utter_sobre_vetores', 'utter_exemplo_vetores',
    		 'utter_exercicios_vetores', 'utter_conteudo_extra_vetores',
    		 'utter_codigo_em_python_vetores'], 'form_names' : []}

@pytest.fixture
def custom_tracker():
    return Tracker('', {'conteudo':'erro'}, {'intent':{'name':'sobre_vetores'}},
    							'', '', '', {}, '')

@pytest.fixture
def custom_dispatcher():
	class Dispatcher():
		def utter_template(self, desired_subject, tracker):
			pass
		def utter_message(self, text=''):
			pass

	return Dispatcher()


@pytest.fixture
def custom_set_slot_value():
    return ActionSetSlotValue()

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


from actions.actions import ActionUtterVaga

@pytest.fixture
def custom_utter_vaga():
    return ActionUtterVaga()

@pytest.fixture
def custom_desired_subject():
	return 'utter_sobre_vetores'

def test_name_utter_vaga(custom_utter_vaga):
	name = custom_utter_vaga.name()
	assert name == "action_utter_vaga"

def test_validate_subject(custom_utter_vaga, custom_domain,
						  custom_desired_subject):
	assert (custom_utter_vaga.validate_subject(custom_domain,
											   custom_desired_subject) ==
		   True)
	assert (custom_utter_vaga.validate_subject(custom_domain,
											   'vetores') ==
		   False)

def test_dispatch_message(custom_utter_vaga, custom_dispatcher,
						  custom_tracker, custom_desired_subject):
	assert (custom_utter_vaga.dispatch_message(custom_tracker, custom_dispatcher,
											  True, custom_desired_subject) ==	
			True)
	assert (custom_utter_vaga.dispatch_message(custom_tracker, custom_dispatcher,
											  False, custom_desired_subject) ==	
			False)


from actions.actions import ActionUtterSobreVaga

@pytest.fixture
def custom_utter_sobre_vaga():
    return ActionUtterSobreVaga()

def test_name_sobre_vaga(custom_utter_sobre_vaga):
	name = custom_utter_sobre_vaga.name()
	assert name == "action_utter_sobre_vaga"

def test_run_sobre_vaga(custom_utter_sobre_vaga, custom_dispatcher,
			 custom_tracker, custom_domain):
	slot = custom_utter_sobre_vaga.run(custom_dispatcher, custom_tracker,
									   custom_domain)
	assert slot == 'erro'


from actions.actions import ActionUtterExemploVaga

@pytest.fixture
def custom_utter_exemplo_vaga():
    return ActionUtterExemploVaga()

def test_name_exemplo_vaga(custom_utter_exemplo_vaga):
	name = custom_utter_exemplo_vaga.name()
	assert name == "action_utter_exemplo_vaga"

def test_run_exemplo_vaga(custom_utter_exemplo_vaga, custom_dispatcher,
			 custom_tracker, custom_domain):
	slot = custom_utter_exemplo_vaga.run(custom_dispatcher, custom_tracker,
									   custom_domain)
	assert slot == 'erro'


from actions.actions import ActionUtterCodigoEmPythonVaga

@pytest.fixture
def custom_utter_codigo_em_python_vaga():
    return ActionUtterCodigoEmPythonVaga()

def test_name_codigo_em_python_vaga(custom_utter_codigo_em_python_vaga):
	name = custom_utter_codigo_em_python_vaga.name()
	assert name == "action_utter_codigo_em_python_vaga"

def test_run_codigo_em_python_vaga(custom_utter_codigo_em_python_vaga, custom_dispatcher,
			 custom_tracker, custom_domain):
	slot = custom_utter_codigo_em_python_vaga.run(custom_dispatcher, custom_tracker,
									   custom_domain)
	assert slot == 'erro'


from actions.actions import ActionUtterExerciciosVaga

@pytest.fixture
def custom_utter_exercicios_vaga():
    return ActionUtterExerciciosVaga()

def test_name_exercicios_vaga(custom_utter_exercicios_vaga):
	name = custom_utter_exercicios_vaga.name()
	assert name == "action_utter_exercicios_vaga"

def test_run_exercicios_vaga(custom_utter_exercicios_vaga, custom_dispatcher,
			 custom_tracker, custom_domain):
	slot = custom_utter_exercicios_vaga.run(custom_dispatcher, custom_tracker,
									   custom_domain)
	assert slot == 'erro'


from actions.actions import ActionUtterConteudoExtraVaga

@pytest.fixture
def custom_utter_conteudo_extra_vaga():
    return ActionUtterConteudoExtraVaga()

def test_name_conteudo_extra_vaga(custom_utter_conteudo_extra_vaga):
	name = custom_utter_conteudo_extra_vaga.name()
	assert name == "action_utter_conteudo_extra_vaga"

def test_run_conteudo_extra_vaga(custom_utter_conteudo_extra_vaga, custom_dispatcher,
			 custom_tracker, custom_domain):
	slot = custom_utter_conteudo_extra_vaga.run(custom_dispatcher, custom_tracker,
									   custom_domain)
	assert slot == 'erro'


from actions.actions import ActionUtterDesafioVaga

@pytest.fixture
def custom_utter_desafio_vaga():
    return ActionUtterDesafioVaga()

def test_name_desafio_vaga(custom_utter_desafio_vaga):
	name = custom_utter_desafio_vaga.name()
	assert name == "action_utter_desafio_vaga"

def test_run_desafio_vaga(custom_utter_desafio_vaga, custom_dispatcher,
			 custom_tracker, custom_domain):
	slot = custom_utter_desafio_vaga.run(custom_dispatcher, custom_tracker,
									   custom_domain)
	assert slot == 'erro'