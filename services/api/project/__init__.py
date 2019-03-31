from flask import Flask, jsonify

# instatiates flask app

app = Flask(__name__)

# sets as development config
app.config.from_object('project.config.DevelopmentConfig')


@app.route('/message-handler/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'ok',
    })
