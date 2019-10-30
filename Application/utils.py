from functools import wraps
from Application.headers import request,app,jsonify
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        else:
            return jsonify({'message':'x-access-token missing'}),403
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
        except Exception as e:
            return jsonify({'message':'invalid x-access-token','error':str(e)}),403
        return f(*args, **kwargs)
    return decorated
