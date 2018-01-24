# coding:utf-8
from . import index
from blog import db
from models.Article import Article
from models.User import User
from models.Comment import Comment
from models.Classes import Classes
from flask import render_template, abort, request


@index.route('/')
def _index():
    return render_template('index.html')


@index.route('/about')
def t():
    rst = Article.query.filter_by(classification='about').first()
    if rst:
        return render_template('article.html', data=rst)
    else:
        abort(500)


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
    comment = Comment.query.filter_by(Article_id=a_id)
    return render_template('article.html', data=rst, comment=comment, a_id=a_id)


@index.route('/comment', methods=["POST"])
def sub_comment():
    text = request.values.get('text')
    name = request.values.get('name')
    mail = request.values.get('mail')
    a_id = request.values.get('a_id')
    if name and mail and text and a_id:
        db.session.add(Comment(Article_id=a_id, name=name, content=text, mail=mail))
        db.session.commit()
        return '0'
    else:
        return '1'
