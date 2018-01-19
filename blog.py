from flask import Flask, render_template

app = Flask(__name__)


import routes.index
app.register_blueprint(routes.index.index, url_prefix='/index')


if __name__ == '__main__':
    app.run()
