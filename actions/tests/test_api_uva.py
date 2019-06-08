import pytest
import os
import sys
import inspect
import api_uva
from rasa_core_sdk import Tracker
from actions.actions import UserForm
from actions.actions import CodeForm


@pytest.fixture
def custom_domain():
    return {}

@pytest.fixture
def custom_tracker():
    return Tracker('', {}, {}, '', '', '', {}, '')

@pytest.fixture
def custom_dispatcher():
    class Dispatcher():
        def utter_message(self, text=''):
            pass
    return Dispatcher()

@pytest.fixture
def custom_user_form():
    return UserForm();


def test_name_user_form(custom_user_form):
    name = custom_user_form.name();
    assert name == "user_form"

def test_required_slots_user_form(custom_user_form):
    slots = custom_user_form.required_slots(custom_tracker)
    assert slots == ['username', 'password']

def test_submit_user_form(custom_user_form, custom_dispatcher,
                          custom_tracker, custom_domain):
    slots = custom_user_form.submit(custom_dispatcher, 
                                custom_tracker, custom_domain)
    assert slots == [{"event": "slot", "timestamp": None,
                     "name": "username", "value": None},
                     {"event": "slot", "timestamp": None,
                     "name": "password", "value": None}]


@pytest.fixture
def custom_code_form():
    return CodeForm();

def test_name_code_form(custom_code_form):
    name = custom_code_form.name()
    assert name == "code_form"

def test_required_slots_code_form(custom_code_form):
    slots = custom_code_form.required_slots(custom_tracker)
    assert slots == ['problema', 'linguagem', 'codigo']

def test_map_linguagem(custom_code_form):
    assert custom_code_form.map_linguagem('C') == '1'
    assert custom_code_form.map_linguagem('Java') == '2'
    assert custom_code_form.map_linguagem('C++') == '3'
    assert custom_code_form.map_linguagem('Pascal') == '4'
    assert custom_code_form.map_linguagem('C++ 11') == '5'
    assert custom_code_form.map_linguagem('Python 3') == '6'
    assert custom_code_form.map_linguagem('Sublime') == 'erro'

def test_submit_code_form(custom_code_form, custom_dispatcher,
                          custom_tracker, custom_domain):
    slots = custom_code_form.submit(custom_dispatcher, 
                                    custom_tracker, custom_domain)
    assert slots == []
"""
def test_get_params():
    api_uva.get_params()


def test_get_soup():
    api_uva.get_soup()


def test_make_login():
    api_uva.make_login()


def test_get_code():
    api_uva.get_code()


def test_get_problem():
    api_uva.get_problem()


def test_get_problem_by_id():
    api_uva.get_problem_by_id()


def test_get_problem_by_number():
    api_uva.get_problem_by_number()


def test_submeter_um_problema():
    api_uva.submeter_um_problema()


def test_username_para_userid():
    api_uva.username_para_userid()


def test_resultado_ultima_submissao():
    api_uva.resultado_ultima_submissao()"""