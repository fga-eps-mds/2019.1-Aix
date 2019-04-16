from flask import Flask, jsonify, request, Response

# instancia aplicativo flask

app = Flask(__name__)

app.config.from_object('project.config.DevelopmentConfig')


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'ok',
    })
