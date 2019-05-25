from bs4 import BeautifulSoup
import requests
import json

HOME = 'http://uva.onlinejudge.org/'
URLPROBLEMA = 'https://uva.onlinejudge.org/index.php?option'
URLPROBLEMA += '=com_onlinejudge&Itemid=25&page=submit_problem'
URLPROBLEMA += '&problemid='
URLSUBMISSAO = "https://uhunt.onlinejudge.org/api/subs-user/"
URLUNAMETOID = "http://uhunt.felix-halim.net/api/uname2uid/"
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


def get_soup(url, action=GET, params={}):
    request = None

    if action == GET:
        request = session.get(url)

    elif action == POST:
        request = session.post(url, params)

    html = request.text
    soup = BeautifulSoup(html, features="html.parser")
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


def submeter_um_problema(username, password,
                         problem_num, lang,
                         path='', codigo=''):
    make_login(username, password)
    problem = get_problem_by_number(problem_num)
    problem_id = str(problem[u'pid'])
    urldoproblema = URLPROBLEMA + problem_id
    soup = get_soup(urldoproblema)
    form = soup.find_all('form')[1]
    params = get_params(form)
    if(path != ''):
        code = get_code(path)
    else:
        code = codigo
    params['code'] = code
    params['language'] = lang
    action = form['action']
    resultado = get_soup('https://uva.onlinejudge.org/'+action,
                         action='1', params=params)
    response = resultado.title.text
    return response

def username_para_userid(username):
    url = URLUNAMETOID+str(username)
    resp = requests.get(url)
    data = json.loads(resp.text)
    return str(data)


def resultado_ultima_submissao(username):
    user_id = username_para_userid(username)
    url = URLSUBMISSAO + str(user_id)
    resp = requests.get(url)
    data = json.loads(resp.text)
    data = data[u'subs']
    data.sort(key = lambda x : x[0], reverse = True)
    data = data[0]
    veredito = data[2]

    dct =   {   10 : 'Submission error',
                15 : 'Can\'t be judged',
                20 : 'In queue',
                30 : 'Compile error',
                35 : 'Restricted function',
                40 : 'Runtime error',
                45 : 'Output limit',
                50 : 'Time limit Exceeded',
                60 : 'Memory limit',
                70 : 'Wrong answer',
                80 : 'PresentationE',
                90 : 'Accepted'
            }
    veredito = dct[veredito]
    return veredito

