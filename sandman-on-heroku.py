from functools import wraps
from os import getenv
from sandman import app, auth
from sandman.model import activate
from werkzeug.contrib.fixers import ProxyFix


def redirect_to_ssl(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        criteria = [
            not request.is_secure,
            not request.headers.get('X-Forwarded-Proto', 'http') == 'https',
            request.url.startswith('http://')
        ]
        if all(criteria):
            url = request.url.replace('http://', 'https://', 1)
            return redirect(url, code=301)
        return f(*args, **kwargs)
    return decorated


@app.before_request
@redirect_to_ssl
@auth.login_required
def before_request():
    pass


@auth.get_password
def get_password(username):
    if username == getenv('SANDMAN_USERNAME'):
        return getenv('SANDMAN_PASSWORD')
    return None


app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
app.wsgi_app = ProxyFix(app.wsgi_app)
app.debug = True
activate(browser=False)
