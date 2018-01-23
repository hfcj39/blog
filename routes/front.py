from . import index
from flask import render_template


@index.route('/')
def _index():
    return render_template('index.html')


@index.route('/tst')
def t():
    return render_template('test.html')


@index.route('/blog')
def blog():
    return render_template('blog.html')
