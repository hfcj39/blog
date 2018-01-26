# coding:utf-8
from . import index
from blog import db
from models.Article import Article
from models.User import User
from models.Img import Img
from models.Comment import Comment
from models.Classes import Classes
from flask import render_template, abort, request, jsonify
import json


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


@index.route('/pictures')
def pic():
    img_list = Img.query.filter_by(visible=1, delete_at=None).order_by(Img.updated_at.desc()).limit(12)
    return render_template('pictures.html', list=img_list)


@index.route('/load_picture', methods=["POST"])
def get_pic():
    offset = int(request.values.get('offset'))
    img = Img.query.filter_by(visible=1, delete_at=None).order_by(Img.updated_at.desc()).limit(8).offset(offset).all()
    tmp = []
    for item in img:
        tmp.append({
            "path": item.path,
            "text": item.text,
            "updated_at": item.updated_at
        })
    return jsonify(rst=tmp)


@index.route('/load_one_picture', methods=["POST"])
def get_one_pic():
    offset = int(request.values.get('offset'))
    img = Img.query.filter_by(visible=1, delete_at=None).order_by(Img.updated_at.desc()).offset(offset).first()
    if img:
        return jsonify({
            "path": img.path,
            "text": img.text,
            "updated_at": img.updated_at
        })
    else:
        abort(404)

