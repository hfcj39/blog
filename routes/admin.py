from flask_admin.contrib.sqla import ModelView
from flask import url_for, render_template
from flask_admin import BaseView, expose
from blog import admin, db
from models.User import User
from models.Article import Article
from models.Comment import Comment
from models.Classes import Classes


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Article, db.session))
admin.add_view(ModelView(Classes, db.session))
admin.add_view(ModelView(Comment, db.session))


# class MyView(BaseView):
#     @expose('/')
#     def index(self):
#         url = url_for('.test')
#         return self.render('admin.html', url = url)
