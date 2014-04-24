from os import getenv
from sandman import app
from sandman.model import activate
from werkzeug.contrib.fixers import ProxyFix

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
app.debug = True
app.wsgi_app = ProxyFix(app.wsgi_app)
activate(browser=False)
