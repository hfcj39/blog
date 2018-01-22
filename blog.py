from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
import config.config_dev as config

app = Flask(__name__)
# app.config['TRAP_HTTP_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config["SQLALCHEMY_ECHO"] = True # echo raw sql sentence
# app.secret_key = config.secret
db = SQLAlchemy(app)


@app.route('/')
def test():
    return redirect('/index')


import routes.error
# @app.errorhandler(404)
# def printerr(err):
#     print('err', err)
#     return render_template('error.html')


import routes
app.register_blueprint(routes.index, url_prefix='/index')
app.register_blueprint(routes.error.error)


import init_db


if __name__ == '__main__':
    app.run(debug=True)
