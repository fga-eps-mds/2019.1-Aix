import pytest
import os
import sys
import inspect
import api_uva
import requests
import json
from bs4 import BeautifulSoup
from rasa_core_sdk import Tracker
from actions.actions_uva import UserForm
from actions.actions_uva import CodeForm
from actions.actions_uva import ActionFeedbackSubmissao

@pytest.fixture
def custom_domain():
    return {}

@pytest.fixture
def custom_tracker():
    return Tracker('', {}, {}, '', '', '', {}, '')

@pytest.fixture
def custom_tracker_valid_user():
    return Tracker('', {'username':'usuario_teste', 'password' : '123456789'}, {}, '', '', '', {}, '')

@pytest.fixture
def custom_dispatcher():
    class Dispatcher():
        def utter_message(self, text=''):
            pass
    return Dispatcher()


@pytest.fixture
def custom_feedback_submissao():
    return ActionFeedbackSubmissao()

@pytest.fixture
def custom_tracker_feedback():
    return Tracker('', {'username':'usuario_teste'}, {}, '', '', '', {}, '')

def test_name_feedback_submissao(custom_feedback_submissao):
    name = custom_feedback_submissao.name()
    assert name == "action_feedback_submissao_uva"

def test_run_feedback_submissao(custom_feedback_submissao, custom_dispatcher,
                                custom_tracker_feedback, custom_domain):
    username = custom_feedback_submissao.run(custom_dispatcher,
                                             custom_tracker_feedback,
                                             custom_domain)
    assert username == []


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
                          custom_tracker, custom_domain,
                          custom_tracker_valid_user):
    slots = custom_user_form.submit(custom_dispatcher, 
                                custom_tracker, custom_domain)
    assert slots == [{"event": "slot", "timestamp": None,
                     "name": "username", "value": None},
                     {"event": "slot", "timestamp": None,
                     "name": "password", "value": None}]
    slots = custom_user_form.submit(custom_dispatcher, 
                                custom_tracker_valid_user,
                                custom_domain)
    assert slots == []


@pytest.fixture
def custom_code_form():
    return CodeForm();

@pytest.fixture
def custom_tracker_valid_user_and_language():
    return Tracker('', {'username':'usuario_teste', 'password' : '123456789',
                        'codigo':'code', 'problema':'11459', 'linguagem':'C++'},
                        {}, '', '', '', {}, '')

@pytest.fixture
def custom_tracker_invalid_language():
    return Tracker('', {'username':'usuario_teste', 'password' : '123456789',
                        'codigo':'code', 'problema':'11459', 'linguagem':'C--'},
                        {}, '', '', '', {}, '')

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
                          custom_tracker, custom_domain,
                          custom_tracker_valid_user_and_language,
                          custom_tracker_invalid_language):
    slots = custom_code_form.submit(custom_dispatcher, 
                                    custom_tracker, custom_domain)
    assert slots == []
    slots = custom_code_form.submit(custom_dispatcher, 
                                    custom_tracker_valid_user_and_language,
                                    custom_domain)
    assert slots == [{"event": "slot", "timestamp": None,
                     "name": "codigo", "value": None},
                     {"event": "slot", "timestamp": None,
                     "name": "problema", "value": None},
                     {"event": "slot", "timestamp": None,
                     "name": "linguagem", "value": None}]
    slots = custom_code_form.submit(custom_dispatcher, 
                                    custom_tracker_invalid_language,
                                    custom_domain)
    assert slots == [{"event": "slot", "timestamp": None,
                     "name": "codigo", "value": None},
                     {"event": "slot", "timestamp": None,
                     "name": "problema", "value": None},
                     {"event": "slot", "timestamp": None,
                     "name": "linguagem", "value": None}]


@pytest.fixture
def custom_session():
    session = requests.session()
    return session

@pytest.fixture
def custom_url():
    url = 'http://uva.onlinejudge.org/'
    return url


def test_get_params():
    text = "<body><input name='name' /><input pass='pass' /></body>"
    form = BeautifulSoup(text, features="html.parser")
    params = api_uva.get_params(form)
    assert params == {'name': ''}

def test_get_soup(custom_session, custom_url):
    soup = api_uva.get_soup(custom_url)
    request = custom_session.get(custom_url)
    html = request.text
    custom_soup = BeautifulSoup(html, features="html.parser")
    assert soup.title == custom_soup.title

    soup = api_uva.get_soup('http://httpbin.org/post', action='1')
    request = custom_session.post('http://httpbin.org/post')
    html = request.text
    custom_soup = BeautifulSoup(html, features="html.parser")
    assert soup.title == custom_soup.title

    soup = api_uva.get_soup('', action='3')
    assert soup == None

    soup = api_uva.get_soup('')
    custom_soup = BeautifulSoup('', features="html.parser")
    assert soup.title == custom_soup.title

    soup = api_uva.get_soup('', action='1')
    custom_soup = BeautifulSoup('', features="html.parser")
    assert soup.title == custom_soup.title

def test_make_login(custom_url):
    username = 'username'
    password = 'password'
    fake_url = 'https://www.google.com/'
    result = api_uva.make_login(username, password, fake_url)
    assert result == False
    username = 'username'
    password = 'password'
    result = api_uva.make_login(username, password, custom_url)
    assert result == False
    username = 'usuario_teste'
    password = '123456789'
    result = api_uva.make_login(username, password, custom_url)
    assert result == True

def test_get_code():
    path = 'actions/tests/teste.txt'
    result = api_uva.get_code(path)
    assert result == "testepytest"


@pytest.fixture
def custom_data_by_id():
    url = 'http://uhunt.felix-halim.net/api/p/id/2454'
    resp = requests.get(url)
    data = json.loads(resp.text)
    return data

@pytest.fixture
def custom_data_by_number():
    url = 'http://uhunt.felix-halim.net/api/p/num/11459'
    resp = requests.get(url)
    data = json.loads(resp.text)
    return data


def test_get_problem(custom_data_by_id, custom_data_by_number):
    result = api_uva.get_problem(None, None, True, True)
    assert result == None
    result = api_uva.get_problem('2454', None, True, False)
    assert result == custom_data_by_id
    result = api_uva.get_problem(None, '11459', False, True)
    assert result == custom_data_by_number
    result = api_uva.get_problem(None, None, False, False)
    assert result == None

def test_get_problem_by_id(custom_data_by_id):
    result = api_uva.get_problem_by_id('2454')
    assert result == custom_data_by_id 

def test_get_problem_by_number(custom_data_by_number):
    result = api_uva.get_problem_by_number('11459')
    assert result == custom_data_by_number

def test_problem_submit():
    result = api_uva.problem_submit('username', 'password',
                                    '11459', '5', '', 'codigo')
    assert result == 'UVa Online Judge'
    result = api_uva.problem_submit('username', 'password',
                                    '11459', '5', 'actions/tests/teste.txt',
                                    'codigo')
    assert result == 'UVa Online Judge'

def test_username_to_user_id():
    assert api_uva.username_to_user_id('usuario_teste') == '1057837'

def test_last_submit_result():
    assert api_uva.last_submit_result('andreabenf') == 'Olha, o código rodou, mas sua solução não apresenta o resultado esperado para todos os casos de testes dos juízes, arrume e tente de novo!'
    assert api_uva.last_submit_result('none') == 'Bée, não encontrei sua submissão! Espere um pouco e tente novamente.'