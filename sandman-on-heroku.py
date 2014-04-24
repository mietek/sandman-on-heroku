from flask_sslify import SSLify
from os import getenv
from sandman import app, auth
from sandman.model import activate
from werkzeug.contrib.fixers import ProxyFix

@auth.get_password
def get_password(username):
    if username == getenv('SANDMAN_USERNAME'):
        return getenv('SANDMAN_PASSWORD')
    return None

@app.before_request
@auth.login_required
def before_request():
    pass

sslify = SSLify(app, permanent=True)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
app.debug = True
app.wsgi_app = ProxyFix(app.wsgi_app)
activate(browser=False)
