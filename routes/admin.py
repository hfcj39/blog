from flask_admin.contrib.sqla import ModelView
from flask import Flask, url_for, redirect, render_template, request
from flask_admin import Admin, BaseView, expose, helpers, AdminIndexView
import flask_login as login
from flask_login import LoginManager
from wtforms import form, fields, validators
from blog import db,app
from models.User import User
from models.Article import Article
from models.Comment import Comment
from models.Classes import Classes
from models.Img import Img
from werkzeug.security import generate_password_hash, check_password_hash

admin = Admin(name='Blog', template_mode='bootstrap3')

login_manager = LoginManager()
login_manager.session_protection = 'strong'

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Article, db.session))
admin.add_view(ModelView(Classes, db.session))
admin.add_view(ModelView(Comment, db.session))
admin.add_view(ModelView(Img, db.session))


# Define login and registration forms (for flask-login)
class LoginForm(form.Form):
    login = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()

# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

# Create customized model view class
class LoginView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

# Create customized index view class that handles login & registration
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
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()


    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin.html')


admin.add_view(MyView(name='Editor'))
