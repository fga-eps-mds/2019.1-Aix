"""
import re
import copy
excessoes_intents=[]
excessoes_intents.append('out_of_scope')
excessoes_intents.append('pesquisa_stackoverflow')
excessoes_intents.append('utter_sobre_vaga')
excessoes_intents.append('intent_utter_exemplo_vaga')
excessoes_intents.append('intent_utter_codigo_em_python_vaga')
excessoes_intents.append('intent_utter_exercicios_vaga')
excessoes_intents.append('intent_utter_conteudo_extra_vaga')
excessoes_intents.append('login_no_uva')
excessoes_intents.append('inform')
excessoes_intents.append('submissao_de_exercicio')
excessoes_intents.append('feedback_uva')

excessoes_actions = []
excessoes_actions.append('utter_default')
excessoes_actions.append('action_utter_vaga')
excessoes_actions.append('action_utter_sobre_vaga')
excessoes_actions.append('action_utter_exemplo_vaga')
excessoes_actions.append('action_utter_codigo_em_python_vaga')
excessoes_actions.append('action_utter_exercicios_vaga')
excessoes_actions.append('action_utter_conteudo_extra_vaga')
excessoes_actions.append('utter_ask_username')
excessoes_actions.append('utter_ask_password')
excessoes_actions.append('utter_ask_codigo')
excessoes_actions.append('utter_ask_problema')
excessoes_actions.append('utter_ask_linguagem')

excessoes_utters = []
excessoes_utters.append('action_utter_vaga')
excessoes_utters.append('action_utter_sobre_vaga')
excessoes_utters.append('action_utter_exemplo_vaga')
excessoes_utters.append('action_utter_codigo_em_python_vaga')
excessoes_utters.append('action_utter_exercicios_vaga')
excessoes_utters.append('action_utter_conteudo_extra_vaga')

with open('domain.yml') as arquivo:
    domain = arquivo.read()

tudo = re.findall(r'\w+', domain) #regex que captura_todo o texto da domain

utters = re.findall(r'utter_\w+:\n\s+-\stext\s*:\s\|', domain) #regex que captura todas as utters com conteúdo
print(utters)

intents = [] #lista que armazenará todas as intents declaradas na domain
actions = [] #lista que armazenará todas as utters e actions declaradas na domain
copia_tudo = copy.copy(tudo) #realiza uma cópia da regex que captura tudo para que nada seja perdido

#capturando declaração das intents
i = 0
while not ('forms' in copia_tudo[i]):
    intents.append(copia_tudo[i])
    i += 1
del intents[0]

i = 0
copia_tudo = copy.copy(tudo)
while not ('actions' in copia_tudo[i]):
    i += 1
inicio_actions = i

while inicio_actions < len(copia_tudo):
    if ('utter' in copia_tudo[inicio_actions]):
        actions.append(copia_tudo[inicio_actions])
    inicio_actions += 1

print(actions)



i = 0
j = 0
encontrado = False
while i < len(intents):
    while j < len(actions):
        if 'utter_'+intents[i] == actions[j] or 'action_'+intents[i] == actions[j]:
            encontrado = True
        j+=1
    j = 0
    if encontrado == False:
        print("não encontrada utter ou action de "+intents[i])
    encontrado = False
    i+=1

print("---------------------------")


i = 0
j = 0
encontrado = False
while i < len(actions):
    while j < len(intents):
        if 'utter_'+intents[j] == actions[i] or 'action_'+intents[j] == actions[i]:
            encontrado = True
        j+=1
    j = 0
    if encontrado == False:
        print("não foi encontrada a intent de "+actions[i])
    encontrado = False
    i+=1
print('---------------------------')
i = 0
j = 0
encontrado = False
while i < len(actions):
    while j < len(utters):
        if actions[i] in utters[j] :
            encontrado = True
        j+=1
    j = 0
    if encontrado == False:
        print("não foi encontrado o conteúdo de "+actions[i])
    encontrado = False
    i+=1
print('---------------------------')
while i < len(utters):
    while j < len(actions):
        if actions[i] in utters[j] :
            encontrado = True
        j+=1
    j = 0
    if encontrado == False:
        print("não foi encontrada a declaração "+utters[i])
    encontrado = False
    i+=1


print(len(intents))
print(len(actions))
"""
from lark import Lark
with open('domain.yml') as arquivo:
    domain = arquivo.read()

l = Lark(r""" start: exp
    ?exp: utter
        | action
        | intent
        | form
        | entities
        | slots
        | templates
    templates: utter_d text
    utter_d: /utter_\w+:$/
    text: /-\stext:\s\|\s+(.\n?\n?)*\n/

""")
#o text está capturando o último caractere em outra expressão