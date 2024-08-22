from flask import Flask, jsonify,request,g
from flask_babel import Babel
from flask_babel import gettext
from flask_cors import CORS




class user:
    def __init__(self,locale='es') -> None:
        self.locale = locale



def get_locale():
        
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    locale= request.headers.get('Accept-Language')
    if locale:
        return locale.split(',')[0][:2]
    
    return request.accept_languages.best_match(['es','en'])
    

app = Flask(__name__)
CORS(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'es' # es, fr
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'     

babel = Babel(app,locale_selector=get_locale)

    
    
    

@app.route('/')
def index():
    print('LLEGO POR AQUI')
    data=request.get_json()
    locale= data.get('locale')
    if locale:
        g.user = user(locale)
    return jsonify({'message': gettext("Hello world!!")})

@app.route('/save', methods =['POST'])
def save():
    data=request.get_json()
    locale= data.get('locale')
    if locale:
        g.user = user(locale)
    
    return jsonify(message=gettext("Save sucesfuly"))

@app.route('/update', methods =['POST'])
def update():
    data=request.get_json()
    locale= data.get('locale')
    if locale:
        g.user = user(locale)
    return jsonify(message=gettext("Update changes"))

@app.route('/delete', methods =['DELETE'])
def delete():
    data=request.get_json()
    locale= data.get('locale')
    if locale:
        g.user = user(locale)
    return jsonify(message=gettext("Delete  sucesfully"))

@app.route('/change')
def change():
    data=request.get_json()
    locale= data.get('locale')
    if locale:
        g.user = user(locale)
    return jsonify(message=gettext("Saves changes"))



if __name__ == '__main__':
    app.run(port=5000)
