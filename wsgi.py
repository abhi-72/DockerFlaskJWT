from Application import app
import os

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=os.environ.get('APP_PORT',5000),
        debug=os.environ.get('APP_DEBUG',True))
