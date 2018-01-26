from flask_admin.contrib.sqla import ModelView
from flask import Flask, url_for, redirect, render_template, request, flash
from flask_admin import Admin, BaseView, expose, helpers, AdminIndexView
import flask_login as login
from wtforms import form, fields, validators
from blog import db, app
from models.User import User
from models.Article import Article
from models.Comment import Comment
from models.Classes import Classes
from models.Img import Img
from werkzeug.security import generate_password_hash, check_password_hash

# login_manager = LoginManager()
# login_manager.session_protection = 'strong'

# Define login and registration forms (for flask-login)
class LoginForm(form.Form):
    username = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        # if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(username=self.username.data).first()


# Create customized model view class
# Add login authentication
class LoginView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated


class MyAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            try:
                form.validate_login(self)
                login.login_user(user)
            except:
                flash('Invalid username or password!!!!')
                return redirect(url_for('.login_view'))

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        # link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        # self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()


    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))

# test online MD editor
class MyView(BaseView):
    @expose('/')
    def index(self):
        arg1 = 'Hello'
        return self.render('editor.html', arg1 = arg1)


admin = Admin(name='Blog',
              base_template='my_master.html',
              index_view=MyAdminIndexView())


admin.add_view(LoginView(User, db.session))
admin.add_view(LoginView(Article, db.session))
admin.add_view(LoginView(Classes, db.session))
admin.add_view(LoginView(Comment, db.session))
admin.add_view(LoginView(Img, db.session))
admin.add_view(MyView(name='Editor'))

