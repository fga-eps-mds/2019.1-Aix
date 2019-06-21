import pytest
import os
import sys
import inspect
from rasa_core_sdk import Tracker
from actions.actions_intents_vagas import ActionSetSlotValue
from actions.actions_intents_vagas import ActionUtterVaga
from actions.actions_intents_vagas import ActionUtterSobreVaga
from actions.actions_intents_vagas import ActionUtterExemploVaga
from actions.actions_intents_vagas import ActionUtterCodigoEmPythonVaga
from actions.actions_intents_vagas import ActionUtterExerciciosVaga
from actions.actions_intents_vagas import ActionUtterConteudoExtraVaga
from actions.actions_intents_vagas import ActionUtterDesafioVaga

currentdir = os.path.dirname(os.path.abspath
							(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


@pytest.fixture
def custom_domain():
	return {'intent_properties': {}, 'entities': [],
    		'slots': ['conteudo'], 'templates': {}, 'actions':
    		['utter_sobre_vetores', 'utter_exemplo_vetores',
    		'utter_exercicios_vetores', 'utter_conteudo_extra_vetores',
    		'utter_codigo_em_python_vetores'], 'form_names': []}


@pytest.fixture
def custom_tracker():
	return Tracker('', {'conteudo': 'erro'},
    			  {'intent': {'name': 'sobre_vetores'}},
    			  '', '', '', {}, '')


@pytest.fixture
def custom_tracker_with_slot():
	return Tracker('', {'conteudo': 'vetores'},
    			  {'intent': {'name': 'sobre_vetores'}},
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


def test_run_action_set_slot_value(custom_set_slot_value, custom_dispatcher,
								   custom_tracker, custom_domain):
	slot = custom_set_slot_value.run(custom_dispatcher,
									 custom_tracker, custom_domain)
	assert slot == [{"event": "slot", "timestamp": None,
					 "name": "conteudo", "value": "vetores"}]


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
											   custom_desired_subject) is
		   True)
	assert (custom_utter_vaga.validate_subject(custom_domain,
											   'vetores') is
		   False)


def test_dispatch_message(custom_utter_vaga, custom_dispatcher,
						  custom_tracker, custom_desired_subject):
	assert (custom_utter_vaga.dispatch_message(custom_tracker, custom_dispatcher,
											  True, custom_desired_subject) is
			True)
	assert (custom_utter_vaga.dispatch_message(custom_tracker, custom_dispatcher,
											  False, custom_desired_subject) is
			False)


def test_run_utter_vaga(custom_utter_vaga, custom_dispatcher,
						custom_tracker, custom_domain):
	run = custom_utter_vaga.run(custom_dispatcher, custom_tracker,
								custom_domain)
	assert run == []


@pytest.fixture
def custom_utter_sobre_vaga():
    return ActionUtterSobreVaga()


def test_name_sobre_vaga(custom_utter_sobre_vaga):
	name = custom_utter_sobre_vaga.name()
	assert name == "action_utter_sobre_vaga"


def test_run_sobre_vaga(custom_utter_sobre_vaga, custom_dispatcher,
			 			custom_tracker, custom_domain,
			 			custom_tracker_with_slot):
	slot = custom_utter_sobre_vaga.run(custom_dispatcher, custom_tracker,
									   custom_domain)
	assert slot == []
	slot = custom_utter_sobre_vaga.run(custom_dispatcher,
									   custom_tracker_with_slot,
									   custom_domain)
	assert slot == []


@pytest.fixture
def custom_utter_exemplo_vaga():
    return ActionUtterExemploVaga()


def test_name_exemplo_vaga(custom_utter_exemplo_vaga):
	name = custom_utter_exemplo_vaga.name()
	assert name == "action_utter_exemplo_vaga"


def test_run_exemplo_vaga(custom_utter_exemplo_vaga, custom_dispatcher,
			 			  custom_tracker, custom_domain,
			 			  custom_tracker_with_slot):
	slot = custom_utter_exemplo_vaga.run(custom_dispatcher, custom_tracker,
									   custom_domain)
	assert slot == []
	slot = custom_utter_exemplo_vaga.run(custom_dispatcher,
										 custom_tracker_with_slot,
									   	 custom_domain)
	assert slot == []


@pytest.fixture
def custom_utter_codigo_em_python_vaga():
    return ActionUtterCodigoEmPythonVaga()


def test_name_codigo_em_python_vaga(custom_utter_codigo_em_python_vaga):
	name = custom_utter_codigo_em_python_vaga.name()
	assert name == "action_utter_codigo_em_python_vaga"


def test_run_codigo_em_python_vaga(custom_utter_codigo_em_python_vaga,
								   custom_dispatcher, custom_tracker,
								   custom_domain, custom_tracker_with_slot):
	slot = custom_utter_codigo_em_python_vaga.run(custom_dispatcher,
												  custom_tracker, custom_domain)
	assert slot == []
	slot = custom_utter_codigo_em_python_vaga.run(custom_dispatcher,
												  custom_tracker_with_slot,
									   			  custom_domain)
	assert slot == []


@pytest.fixture
def custom_utter_exercicios_vaga():
    return ActionUtterExerciciosVaga()


def test_name_exercicios_vaga(custom_utter_exercicios_vaga):
	name = custom_utter_exercicios_vaga.name()
	assert name == "action_utter_exercicios_vaga"


def test_run_exercicios_vaga(custom_utter_exercicios_vaga, custom_dispatcher,
			 				 custom_tracker, custom_domain,
			 				 custom_tracker_with_slot):
	slot = custom_utter_exercicios_vaga.run(custom_dispatcher,
											custom_tracker,
									   		custom_domain)
	assert slot == []
	slot = custom_utter_exercicios_vaga.run(custom_dispatcher,
											custom_tracker_with_slot,
									   		custom_domain)
	assert slot == []

def test_verify_if_is_variable(custom_utter_exercicios_vaga):
	variavel = 'strings'
	vetores = 'vetores'
	assert (custom_utter_exercicios_vaga.verify_if_is_variable(variavel) ==
		   'variaveis')
	assert (custom_utter_exercicios_vaga.verify_if_is_variable(vetores) ==
		   vetores)

@pytest.fixture
def custom_utter_conteudo_extra_vaga():
    return ActionUtterConteudoExtraVaga()


def test_name_conteudo_extra_vaga(custom_utter_conteudo_extra_vaga):
	name = custom_utter_conteudo_extra_vaga.name()
	assert name == "action_utter_conteudo_extra_vaga"


def test_run_conteudo_extra_vaga(custom_utter_conteudo_extra_vaga, 
								 custom_dispatcher,
			 					 custom_tracker, custom_domain,
			 					 custom_tracker_with_slot):
	slot = custom_utter_conteudo_extra_vaga.run(custom_dispatcher,
												custom_tracker,
									     		custom_domain)
	assert slot == []
	slot = custom_utter_conteudo_extra_vaga.run(custom_dispatcher,
												custom_tracker_with_slot,
									     		custom_domain)
	assert slot == []


@pytest.fixture
def custom_utter_desafio_vaga():
    return ActionUtterDesafioVaga()


def test_name_desafio_vaga(custom_utter_desafio_vaga):
	name = custom_utter_desafio_vaga.name()
	assert name == "action_utter_desafio_vaga"


def test_run_desafio_vaga(custom_utter_desafio_vaga, custom_dispatcher,
			 			  custom_tracker, custom_domain,
			 			  custom_tracker_with_slot):
	slot = custom_utter_desafio_vaga.run(custom_dispatcher, custom_tracker,
									     custom_domain)
	assert slot == []
	slot = custom_utter_desafio_vaga.run(custom_dispatcher,
										 custom_tracker_with_slot,
										 custom_domain)
	assert slot == []
