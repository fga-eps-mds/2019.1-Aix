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
print(l.parse(domain).pretty())