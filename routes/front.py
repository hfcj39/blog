from . import index
from blog import db
from models.Article import Article
from models.User import User
from models.Classes import Classes
from flask import render_template


@index.route('/')
def _index():
    return render_template('index.html')


@index.route('/tst')
def t():
    userinfo = User.query.get(1)
    rst = userinfo.articles
    print(rst)
    return render_template('test.html')


@index.route('/blog')
@index.route('/blog/<int:page>')
def blog(page=1):
    rst = Article.query.filter_by(visible=1, delete_at=None) \
        .order_by(Article.updated_at.desc()).paginate(page, 5, True)
    classes = Classes.query.all()
    return render_template('blog.html', data=rst, classes=classes)


@index.route('/class')
@index.route('/class/<int:c_id>')
@index.route('/class/<int:c_id>/<int:page>')
def classification(c_id=1, page=1):
    class_name = Classes.query.get(c_id).classification
    rst = Article.query.filter_by(visible=1, delete_at=None, classification=class_name) \
        .order_by(Article.updated_at.desc()).paginate(page, 5, True)
    classes = Classes.query.all()
    return render_template('class.html', data=rst, classes=classes, c_id=c_id)


@index.route('/article/<int:a_id>')
def get_article(a_id):
    rst = Article.query.get(a_id)
    return render_template('article.html', data=rst)
