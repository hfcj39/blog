# coding=utf-8
from models import *
from os import path

# check if db exist

# print(path.abspath(path.dirname(__file__)+'/database.db'))

if path.isfile(path.abspath(path.dirname(__file__) + '/database.db')):
    print('database found!')
else:
    print('creating database!')
    db.drop_all()
    db.create_all()
    db.session.add(User.User(username='admin', password='admin'))
    db.session.add(Classes.Classes(classification=u'默认分类'))
    for i in range(50):
        db.session.add(Article.Article(user_id=1, title='Hello World', content=u'## 这是一篇样例', classification=u'默认分类'))
        db.session.add(Img.Img(path=str(i+1) + '.jpg', text='test'))
    db.session.commit()
