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
#with open('domain.yml') as arquivo:
#    domain = arquivo.read()
domain = """ 
intents:
  - start
  - help
  - cumprimentar
  - despedir
  - tudo_bem
  - manter_conversa
  - out_of_scope
  - assuntos_inapropriados
  - sobre_programaçao

forms:
  - user_form
  - code_form
  
entities:
  - conteudo
  - username
  - password
  - codigo
  - problema
  - linguagem

slots:
    conteudo:
        type: text
        initial_value: "erro"
    username:
        type: unfeaturized
        auto_fill: false
    password:
        type: unfeaturized
        auto_fill: false
    codigo:
        type: unfeaturized
        auto_fill: false
    problema:
        type: unfeaturized
        auto_fill: false
    linguagem:
        type: unfeaturized
        auto_fill: false
templates:
  utter_cumprimentar:
    - text: |
        Oiieee, tudo Bééem?
        Sou a Aix, a chatBode e estou aqui para te ensinar Python!
        Se estiver curioso, pergunte mais sobre mim, o que sei fazer ou como me usar que eu te conto!
        Caso queira saber como ir direto no assunto, digite /help para saber como funciono :)
        Sugiro tambéem dar uma olhada no nosso cronograma de estudos! Digite /cronograma para acessá-lo.

  utter_help:
   - text: |
        Ok! Você é uma pessoa direta e quer ver como funciono por trás dos fenos..
        Beleza! Aqui estão minhas informações:
        Ações que posso fazer:
          1. Explicar um conteúdo;
          2. Citar exemplos;
          3. Enviar um exemplo prático;
          4. Indicar exercícios;
          5. Enviar links extras sobre o conteúdo;
          6. Sugerir desafios para cada conteúdo;
          7. Pesquisar no StackOverflow.
          8. Informar um cronograma de conteúdos de python.
        Conteúdos mapeados:
          - Entrada e saída de dados
          - Variáveis
          - Estruturas Condicionais
          - Estruturas de Repetição
          - Vetores
          - Strings
          - Matrizes
          - Bibliotecas
          - Funções
          - Arquivos
        Como? Escreva algo do tipo:
          Quero saber o que é [Nome do conteúdo]
          Quero um exemplo sobre [Nome do conteúdo]
          Quero um exemplo em código de [Nome do conteúdo]
          Me dê exercícios sobre [Nome do conteúdo]
          Quero saber mais sobre [Nome do conteúdo]
          Quero um desafio de [Nome do conteúdo]
          *Para pesquisar no StackOverflow voce deve digitar:
          pesquise sobre [conteúdo que você quer saber]
          *Para acessar o cronograma:
            /cronograma
        OBS: Eu sei processar linguagem natural! Não perca tempo pensando se vou entender ou não. Desde que a sua mensagem tenha O QUE você quer e SOBRE o que você quer, é provável que eu entenda!

# comentairorsfsdofio

actions:
  - utter_start
  - utter_help
  - utter_cumprimentar
  - utter_despedir
  - utter_tudo_bem
  - utter_manter_conversa
  - utter_default
  - utter_assuntos_inapropriados
  - utter_sobre_programaçao
"""
l = Lark(r""" start: exp
    exp: intents forms entities slots templates actions
        | comment
        | actions
        
    intents: intents_text intents
            | intent_name intents
            | intent_name
    
    forms: forms_text forms
        | form_name forms
        | form_name
        
        
    entities: entities_text entitie_name entities
            | entitie_name entities
            | entitie_name
                
    
    slots: slots_text slot_name type slot_any slots
        | slot_name type slot_any slots
        | slot_name type slot_any
    
    templates: templates_text templates
            | utter_def text_mto
            | utter_def text_mto templates
            | templates comment
            | comment templates
        
    text_mto: text text_mto
            | text
        
    actions:  actions_text actions
            | utter actions
            | utter
            | action actions
            | action
            | comment actions
            | actions comment
            
    comment: /\n*\s*#[^\n]*\n/
    
    utter_def: /\s*\n*utter_\w+:\s*/
    
    text: /\s*- text: \D(\n[^\n]+[.,:!?a-úA-Ú();=&%_\d])*\n/
    
    utter: /\s*-\s((utter_.+)\n?)*/
    
    action: /\s*-\s((action_.*)\n?)*/
    
    actions_text: /\n*\s*actions:\n*/
    
    templates_text: /\n*templates:\n?/
    
    slots_text: /\n\s*slots:\n/
    
    slot_name: /\s*.*:\n?/
    
    type: /\s*.*\n/
    
    slot_any: /\s*([^\n])*\n/
    
    entities_text: /\n*\s*entities:\n/
    
    entitie_name: /\s*-\s[^\n]*\n/
    
    forms_text: /\n*\s*forms:\n/
    
    form_name: /\s*-\s[^\n]*\n/
    
    intents_text: /\n*\s*intents:\n/
    
    intent_name: /\s*-\s[^\n]*\n/
    
    %import common.WS_INLINE
    %ignore WS_INLINE
    """)
#o text está capturando o último caractere em outra expressão
print(l.parse(domain).pretty())



