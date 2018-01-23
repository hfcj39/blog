from . import index
from blog import db
from models.Article import Article
from flask import render_template


@index.route('/')
def _index():
    return render_template('index.html')


@index.route('/tst')
def t():
    return render_template('test.html')


@index.route('/blog')
@index.route('/blog/<int:page>')
def blog(page=1):
    rst = Article.query.filter_by(visible=1, delete_at=None) \
        .order_by(Article.updated_at.desc()).paginate(page, 5, True)
    return render_template('blog.html', data=rst)
