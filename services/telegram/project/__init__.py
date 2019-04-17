from flask import Flask, jsonify, request, Response
import telepot

bot_name = 'Aix'
bot_username = 'Aix_chatbodebot'
token_telegramm = ''

app = Flask(__name__)
app.config.from_object('project.config.DevelopmentConfig')


@app.route('/', methods=['GET', 'POST'])
def index():

    return '<h1>Podecre</h1>'


@app.route('/ping', methods=['GET'])
def ping():


    return jsonify({
        'status': 'ok',
    })
