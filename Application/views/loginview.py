from Application.headers import *

from flask import Blueprint
from datetime import datetime,timedelta

import jwt

applogin = Blueprint('applogin','__name__')

@applogin.route('/logout/', methods=['GET'])
def logout():
    return jsonify({'message':'You are successfully logged out'}),200

@applogin.route('/login/',methods=['POST'])
def login():
    try:
        auth = request.json
        app.logger.info(f'auth-{auth}')
        if auth is not None: #and auth.password == 'password':
            token = jwt.encode({'user':auth['username'],'exp': datetime.utcnow() + timedelta(minutes=30)},app.config['SECRET_KEY'])
            return make_response({'message':'Login Success','token':token.decode('utf-8')}),200
        return make_response({'message':'Login failed'}),401
    except Exception as e:
         return make_response({'error':str(e)})
