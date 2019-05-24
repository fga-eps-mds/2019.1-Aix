from bs4 import BeautifulSoup
import os
import requests
import json

HOME = 'http://uva.onlinejudge.org/'
URLPROBLEMA = 'https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25&page=submit_problem&problemid='
GET = '0'
POST = '1'


session = requests.session()


def get_params(form):
    params = {}
    inputs = form.find_all('input')
    for i in inputs:
        name = i.get('name')
        value = i.get('value')
        if name:
            params[name] = value if value else ''

    return params


def get_soup (url, action = GET, params={}):
    request = None

    if action == GET:
        request = session.get(url)

    elif action == POST:
        request = session.post(url, params)
        r = requests.post
    html = request.text
    soup = BeautifulSoup(html,features="html.parser")
    return soup


def make_login(username, password, url=HOME):
    soup = get_soup(url)
    form = soup.find(id="mod_loginform")
    if not form:
        return False
    url = form['action']
    params = get_params(form)
    params['username'] = username
    params['passwd'] = password
    soup = get_soup(url, action=POST, params=params)

    if soup.find(id="mod_loginform"):
        return False
    else:
        return True

def get_code(path):
    code = ''
    in_file = open(path, 'r')
    for line in in_file:
        code += line
    in_file.close()
    return code

def process_submission(form, code, language):
    url = HOME + form['action']
    params = get_params(form)
    name = form.textarea['name']
    params[name] = code
    params['language'] = language
    get_soup(url, action=POST, params=params)

def make_submission(url, code, language):
    soup = get_soup(url)
    form = soup.find_all('form')[1]
    process_submission(form, code, language)

def sumbit_problem(usr, pswrd, lang, problem_url, file_name, path=os.getcwd()):
    total_path = os.path.join(path, file_name)
    if not os.path.isfile(total_path):
        print 'Not a file'
        return
    code = get_code(total_path)
    login = make_login(usr, pswrd)
    if login:
        make_submission(problem_url, code, lang)
    else:
        print 'Error while submitting'

def sumbit_problem_with_id(username, password, language, problem_id, file_name, path=os.getcwd()):
    base_url = 'http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=submit_problem&problemid='
    base_url += str(problem_id)
    base_url += '&category='
    sumbit_problem(username, password, language, base_url, file_name, path)

def get_problem(problem_id, problem_number, by_id, by_number):
    url = ''
    resp = None
    data = None
    if by_id and by_number:
        return None
    elif by_id:
        url = 'http://uhunt.felix-halim.net/api/p/id/' + str(problem_id)
    elif by_number:
        url = 'http://uhunt.felix-halim.net/api/p/num/' + str(problem_number)
    if url != '':
        resp = requests.get(url)
        data = json.loads(resp.text)
    return data

def get_problem_by_id(problem_id):

    return get_problem(problem_id, None, True, False)

def get_problem_by_number(problem_number):

    return get_problem(None, problem_number, False, True)

def get_submissions(user_id):
    url = 'http://uhunt.felix-halim.net/api/subs-user/' + str(user_id)
    resp = requests.get(url)
    data = json.loads(resp.text)
    return data

def SubmeterUmProblema(username, password, idproblema, path):
    login = make_login(username, password)
    urldoproblema = URLPROBLEMA + idproblema
    soup = get_soup(urldoproblema)
    form = soup.find_all('form')[1]
    params = get_params(form)
    code = get_code(path)
    params['code'] = code
    params['language'] = '6'
    action = form['action']
    resultado = get_soup('https://uva.onlinejudge.org/'+action, action = '1', params = params)
    return resultado

