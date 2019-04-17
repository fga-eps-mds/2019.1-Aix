from flask import Flask, jsonify, request, Response
import telepot,json
from project.tokensz import telegram_token

bot_name = 'Aix'
bot_username = 'Aix_chatbodebot'
aix = telepot.Bot(telegram_token)

def write_json(data, filename = 'Resposta.json'):
    with open(filename , 'w') as f:
        json.dump(data,f,indent=4, ensure_ascii=False)



app = Flask(__name__)
app.config.from_object('project.config.DevelopmentConfig')
write_json(aix.getMe())

@app.route('/', methods=['GET', 'POST'])
def index():

    return '<h1> lhul </h1>'


@app.route('/ping', methods=['GET'])
def ping():


    return jsonify({
        'status': 'ok',
    })
