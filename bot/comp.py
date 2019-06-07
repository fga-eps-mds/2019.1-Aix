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
  utter_menu_ajuda:
    - text: |
        Eu sou uma cabra béem inteligente e posso te ajudar com muitas coisas!
        Você pode me perguntar tudo sobre essa maravilhosa cobrinha que chamamos de Python!
        Me pergunta ai sobre algum erro, no seu código, sobre alguma estrutura de python... Qualquer coisa!
        E se quiser começar a aprender, me peça antes o nosso cronograma de estudos!
        Ele vai te ajudar a se localizar no conteúdo!!

    - text: |
        Sabia que você pode me perguntar o que te der na telha?
        Talvez eu peça um pouco de feno em troca hein....
        Brincaderia! hahaha
        E se eu te explicar de um modo que não ficou muito claro, você pode me pedir um link externo
        sobre o conteúdo que eu te mando!
        E se seu desejo for começar a aprender, me peça antes o nosso cronograma de estudos!
        Ele vai te ajudar a se localizar no conteúdo!!
        Mas olha, eu ja estudei tudo sobre Variáveis, Estruturas de repetição, Strings, Estruturas Condicionais, Arquivos, Bibliotecas, Vetores, Matrizes e ainda consigo procurar coisas no StackOverflow!
        É só perguntar!

    - text: |
        Eu te ajudo a aprender python, poxa!
        É só me perguntar a sua duvida sobre a maravilhosa linguagem de programação, que eu respondo!
        E se você achar que já está sabendo, me pede um exercício sobre o conteúdo, ué! Vamos ver se você sabe mesmo. hahahaha
        Eu sou uma cabra bem inteligente, mas ainda estou aprendendo...
        E se seu desejo for começar a aprender, me peça antes o nosso cronograma de estudos!
        Ele vai te ajudar a se localizar no conteúdo!!
        
    - text: |
        Eu te ajudo a aprender python, poxa!
        É só me perguntar a sua duvida sobre a maravilhosa linguagem de programação, que eu respondo!
        E se você achar que já está sabendo, me pede um exercício sobre o conteúdo, ué! Vamos ver se você sabe mesmo. hahahaha
        Eu sou uma cabra bem inteligente, mas ainda estou aprendendo...
        E se seu desejo for começar a aprender, me peça antes o nosso cronograma de estudos!
        Ele vai te ajudar a se localizar no conteúdo!!
    
    - text: |
        Eu sou uma cabra bem inteligente, mas ainda estou aprendendo hahaha!
        Ah, e aí vai uma dica: as vezes se você perguntar a mesma coisa duas vezes,
        pode ser que eu te dê uma resposta diferente!
        E se quiser começar a aprender, me peça antes o nosso cronograma de estudos!
        Ele vai te ajudar a se localizar no conteúdo!!
        Mas ja estudei tudo sobre Variáveis, Estruturas de repetição, Strings, Estruturas Condicionais, Arquivos, Bibliotecas, Vetores, Matrizes e ainda consigo procurar coisas no StackOverflow!
        Pode perguntar!
        
    - text: |
        Como me usar? Pra que eu sirvo? Deixa eu te explicar:
        Eu sou uma cabra super inteligente que sabe tudo sobre Python!
        Tem alguma duvida? É só me perguntar, oras! Só conversar comigo como se eu fosse sua amiga e estivesse ai do seu lado!
        Ah, e deixa eu te dar uma dica... As vezes se você perguntar a mesma coisa duas vezes, pode ser que eu te dê uma resposta diferente!
        Olha, eu já estudei tudo sobre Variáveis, Estruturas de repetição, Strings, Estruturas Condicionais, Arquivos, Bibliotecas, Vetores, Matrizes e ainda consigo procurar coisas no StackOverflow!
        É só perguntar!
        
    - text: |
        Eu sou uma cabra bem inteligente, mas ainda estou aprendendo hahaha!
        Mas ja estudei tudo sobre Variáveis, Estruturas de repetição, Strings, Estruturas Condicionais, Arquivos, Bibliotecas, Vetores, Matrizes e ainda consigo procurar coisas no StackOverflow!
        Pode perguntar!

  utter_curiosidades_python:
    - text: |
        O nome Python não foi inspirado no réptil, mas sim no grupo humorístico britânico Monty Python.

    - text: |
        Existe um poema da linguagem Python chamado Zen do Python que resume as boas práticas.

    - text: |
        Tenta usar o comando "python" e depois "import this" no terminal... você vai ver algo béem legal!!

    - text: |
        O Python serviu de inspiração para muitas linguagens novas!!

    - text: |
        Python foi feita com base na linguagem ABC, com A de aix, Bée de bode e C de capim!

    - text: |
        Você sabia que o Python foi considerado a 3ª linguagem "mais amada" segundo a pesquisa conduzida pelo Stack Overflow em 2018?!

  utter_cronograma:
    - text: |
        Vamos iniciar nossa jornada em aprender python! Veja um cronograma de conteúdos para que você aprenda de forma simples e divertida:
          1º - Conhecer o python. Me envie "o que é python?" ou algo do tipo e te explico..bée
          2º - Instalar ou verificar a versão do python. Me envie "como instalar o python?" ou algo do tipo que te ensino
          3º - Aprender a fazer seu primeiro programa. Me envie "quero fazer meu primeiro programa" ou algo relacionado e então aprenderemos..
          4º - Aprender o que são variáveis e seus tipos. Me envie "o que são variaveis?" ou algo relacionado e você irá entender..
          5º - Aprender a ler dados do usuário. Me envie "como ler dados do usuario?" ou algo assim que te mostro..bée
          6º - Aprender sobre estruturas condicionais. Me envie "o que sao estruturas condicionais?" ou algo do tipo e te explico
          7º - Aprender sobre estruturas de repetição. Me envie "o que sao estrutuas de repeticao?" ou algo relacionado que lhe faço entender
          8º - Aprender sobre vetores. Me envie "o que sao vetores" ou algo assim que te ensino..bée
          9º - Aprender sobre strings. Me envie "o que sao strings" ou algo do tipo que explico certinho..
          10º - Aprender sobre matrizes. Me envie "o que sao matrizes" ou algo do genero que te explico direitinho..
          11º - Aprender sobre bibliotecas. Me envie "como usar bibliotecas em python" ou algo assim que te mostro certinho..
          12º - Aprender sobre funções. Me envie "como fazer uma função em python" ou algo relacionado que te ensino
          13º - Aprender sobre arquivos. Me envie "como usar arquivos em python" ou algo assim que te mostro.
          14º - Aprender sobre o stackoverflow. Me envie "o que é stackoverflow" que te ensino e mostro como pesquisar lá..bée
          Obs: Cada um dos conteúdos possui explicação, exemplos teóricos e práticos, exercícios, desafios e alguns tem até subconteúdos!
          Fácil como comer capim! Não perca tempo e vamos aprender python!

  utter_sobre_aix:
    - text: |
        Você ainda não me conhece?! Por onde é que você navegava esse tempo todo?
        Eu sou a cabra Aix e estou aqui para te auxiliar nos seus estudos e garantir
        sua nota 10 quando o assunto é linguagem de programação Python!
        Mas antes, acho melhor tirar todas suas duvidas de funcionamento comigo antes...
        Me peça o menu ajuda para isso!

    - text: |
        Vou te contar um segredo: sabia que eu fui criada por estudantes da Universidade de Brasília?
        Eu aposto que se você se esforçar e estudar muito junto comigo você tambéem será capaz
        de criar uma ferramenta de estudo tão maneira quanto essa!
        Então para isso acontecer, você tem que começar a entender um pouco mais sobre meu funcionamento.
        É só me pedir o menu ajuda!

    - text: |
        Aí vai uma charada: Quem é, quem é... que te ajuda com a sintaxe Python, tira suas
        dúvidas, e ainda te redireciona exercícios de programação?
        Béem, se você falou seu professor, você acertou...
        Mas sabia que eu também posso te ajudar com isso?
        Sugiro me pedir o menu ajuda, caso qualquer dúvida do meu funcionamento!

    - text: |
        Já vi que você não me conhece muito béem... Mas aposto que você vai gostar de mim!
        Inclusive, se quiser me apresentar aos seus amigos, fala para eles que eles precisam
        ter um desses sistema operacionais: Linux, Windows ou MacOS. E não esqueça, você
        tambéem precisa do ambiente Jupyter instalado!
        Ah!! E agora também estou no telegram!
        Que tal começarmos a aprender? Mas antes, eu sugiro que me peça o menu ajuda para saber
        como eu funciono!

    - text: |
        A cabra que manda exercícios na hora...
        Que tira suas dúvidas sem nenhuma demora...
        Que está todo tempo junto com você...
        Essa cabra sou eu!
        E no meio da noite programa...
        não perde tempo e te chama:
        pro próximo conteúdo do fluxograma!
        Afinal, eu sei que você quer aprender como eu funciono...
        É só me pedir o menu ajuda, não se acanhe!!

    - text: |
        Aí vai uma curiosidade sobre mim: o meu nome veio da mitologia romana!
        Acontece que há muito tempo atrás quem amamentou o deus Júpiter foi a cabra Aix.
        Por eu ter sido criada integrada nessa plataforma Jupyter, nasceu a ideia do meu nome!
        Quanta imaginação, não?
        Mas chega de papo furado... Você quer é aprender como funciono né..
        Beém, tente me perguntar sobre menu ajuda então!
"""
l = Lark(r""" start: exp
    exp: templates
        
    templates: utter_def text_mto
            |   utter_def text_mto templates
        
    text_mto: text text_mto
            | text
    
    utter_def: /\s*\n*utter_\w+:\s*/
    
    text: /\s*- text: \D(\n[^\n]+[.,:!?a-úA-Ú])*\n/
    
    %import common.WS_INLINE
    %ignore WS_INLINE
    """)
#o text está capturando o último caractere em outra expressão
print(l.parse(domain).pretty())



