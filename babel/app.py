from flask import Flask, jsonify,request
from flask_babel import Babel
from flask_babel import gettext

app = Flask(__name__)

app.config['BABEL_DEFAULT_LOCALE'] = 'en' # es, fr
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

babel = Babel(app)

@babel.localeselector
def get_locale():
    lang= request.json('lang')
    return lang or app.config



@app.route('/')
def index():
    print('LLEGO POR AQUI')
    return jsonify({'message': gettext("Hello world!!")})

@app.route('/save')
def save():
    return jsonify(message=gettext("Save sucesfuly"))

@app.route('/update')
def update():
    return jsonify(message=gettext("Saves changes"))



if __name__ == '__main__':
    app.run(port=5000)
