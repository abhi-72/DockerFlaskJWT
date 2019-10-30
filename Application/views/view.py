from flask import Blueprint

from Application.headers import *
from Application.utils import token_required

appview = Blueprint('appview','__name__')

#app.logger.debug/info/warning/error/critical

@appview.route('/tokentest/', methods=['POST'])
@token_required
def token_test():
    return make_response({'message':'Success'}),200
