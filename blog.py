from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config.config_dev as config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config["SQLALCHEMY_ECHO"] = True # echo raw sql sentence
# app.secret_key = config.secret
db = SQLAlchemy(app)

import routes.index
app.register_blueprint(routes.index.index, url_prefix='/index')

import init_db

if __name__ == '__main__':
    app.run()
