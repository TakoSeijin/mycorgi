from flask import Flask, g
from views.party import party
from views.static import static
from views.upload_form import upload_form
from controllers.api import api
from database import db_session

mycorgi_app = Flask(__name__)

mycorgi_app.config['SERVER_NAME'] = 'corgiorgy.com'

mycorgi_app.register_blueprint(party)
mycorgi_app.register_blueprint(static)
mycorgi_app.register_blueprint(upload_form)
mycorgi_app.register_blueprint(api)

@mycorgi_app.teardown_appcontext
def shutdown_session(exception=None):
    db = getattr(g, '_database', None)
    if db:
        db_session.remove()

if __name__ == '__main__':
    mycorgi_app.run(host='0.0.0.0', debug=False)
