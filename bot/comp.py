import re
import copy
with open('domain.yml') as arquivo:
    domain = arquivo.read()

tudo = re.findall(r'\w+', domain) #regex que captura_todo o texto da domain

utters = re.findall(r'utter_\w+:\n\s+-\stext\s*:\s\|', domain) #regex que captura todas as utters com conteúdo

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