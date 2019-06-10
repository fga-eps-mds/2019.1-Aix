from bs4 import BeautifulSoup
import requests
import json

HOME = 'http://uva.onlinejudge.org/'
PROBLEMURL = 'https://uva.onlinejudge.org/index.php?option'
PROBLEMURL += '=com_onlinejudge&Itemid=25&page=submit_problem'
PROBLEMURL += '&problemid='
SUBMISSIONURL = "https://uhunt.onlinejudge.org/api/subs-user/"
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
    sucess_request = True
    if action == GET:
        try:
            request = session.get(url)
        except requests.exceptions.RequestException:
            sucess_request = False
    elif action == POST:
        try:
            request = session.post(url, params)
        except requests.exceptions.RequestException:
            sucess_request = False
    else:
        return None

    if sucess_request:
        html = request.text
    else:
        html = ''

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


def problem_submit(username, password,
                   problem_num, lang,
                   path='', user_code=''):
    make_login(username, password)
    problem = get_problem_by_number(problem_num)
    problem_id = str(problem[u'pid'])
    problem_url = PROBLEMURL + problem_id
    soup = get_soup(problem_url)
    form = soup.find_all('form')[1]
    params = get_params(form)
    if(path != ''):
        code = get_code(path)
    else:
        code = user_code
    params['code'] = code
    params['language'] = lang
    action = form['action']
    result = get_soup('https://uva.onlinejudge.org/'+action,
                      action='1', params=params)
    response = result.title.text
    return response


def username_to_user_id(username):
    url = URLUNAMETOID+str(username)
    try:
        resp = requests.get(url)
    except requests.exceptions.RequestException:
        return '0'
    data = json.loads(resp.text)
    return str(data)


def last_submit_result(username):
    user_id = username_to_user_id(username)
    url = SUBMISSIONURL + str(user_id)
    try:
        resp = requests.get(url)
    except requests.exceptions.RequestException:
        return 'Algo deu errado! Espere um pouco e tente novamente!'
    data = json.loads(resp.text)
    data = data[u'subs']
    data.sort(key=lambda x: x[0], reverse=True)
    try:
        data = data[0]
        answer = data[2]
    except IndexError:
        answer = -1

    dct = {10: 'Submission error',
           15: 'Can\'t be judged',
           20: 'A sua submissão está na fila para ser julgada,' +
               ' espere um pouco!',
           30: 'O código-fonte foi submetido com erro' +
               ' de compilação, tente rodar no jupyter antes' +
               'de me mandar!',
           35: 'Restricted function',
           40: 'Deu Runtime error, um erro típico quando' +
               'você define um vetor ou array com menos capacidade' +
               ' do que o necessário para o problema, ou quando você' +
               ' tenta acessar uma de memória inválida.',
           45: 'Output limit',
           50: 'A solução que você submeteu demorou mais tempo' +
               ' do que o permitido para rodar todos os testes dos juízes.',
           60: 'Memory limit',
           70: 'Olha, o código rodou, mas sua solução não apresenta' +
               ' o resultado esperado para todos os casos de testes dos' +
               ' juízes, arrume e tente de novo!',
           80: 'Olha, sua respostas está praticamente correta,' +
               ' apenas há erro na quantidade de espaços ou letras' +
               ' inversão de letras maiúsculas / minúsculas.' +
               ' Arrume e tente de novo! ',
           90: 'A submissão passou por todos os casos de teste, Parabéns!'
           }
    if answer in dct:
        answer = dct[answer]
    else:
        answer = 'Bée, não encontrei sua submissão!'
        answer += ' Espere um pouco e tente novamente.'
    return answer
