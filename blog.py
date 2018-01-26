from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import config.config_dev as config

app = Flask(__name__)
# app.config['TRAP_HTTP_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
# app.config["SQLALCHEMY_ECHO"] = True  # echo raw sql sentence
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.secret_key = config.secret
db = SQLAlchemy(app)
Bootstrap(app)
from routes.admin import admin

admin.init_app(app)


@app.route('/')
def test():
    return redirect('/index')


import routes.error
# @app.errorhandler(404)
# def printerr(err):
#     print('err', err)
#     return render_template('error.html')

from routes import index

# from routes import admin

app.register_blueprint(index, url_prefix='/index')
app.register_blueprint(routes.error.error)
# app.register_blueprint(admin, url_prefix='/admin')


import init_db
from middleware.filter import *

env = app.jinja_env
env.filters['date'] = datetimeformat
env.filters['safe_markdown'] = safe_markdown

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
