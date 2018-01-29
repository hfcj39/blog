# coding:utf-8
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import BaseFileAdmin, LocalFileStorage
from flask import url_for, render_template
from flask_admin import Admin, BaseView, expose
from blog import db
import os.path as op
from models.User import User
from models.Article import Article
from models.Comment import Comment
from models.Classes import Classes
from models.Img import Img

pic_path = op.join(op.dirname(__file__)[0:-7], 'static/pictures')
# a = op.abspath(op.dirname(__file__))[0:-7]

admin = Admin(name='Blog', template_mode='bootstrap3')

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Article, db.session))
admin.add_view(ModelView(Classes, db.session))
admin.add_view(ModelView(Comment, db.session))
admin.add_view(ModelView(Img, db.session))


class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin.html')


class MyFileAdmin(BaseFileAdmin):
    def __init__(self, base_path, *args, **kwargs):
        storage = LocalFileStorage(base_path)
        super(MyFileAdmin, self).__init__(*args, storage=storage, **kwargs)

    can_mkdir = False

    def on_file_upload(self, directory, path, filename):
        # TODO:上传成功后修改文件名插入数据库，并且生成一份压缩后的缩略图,暂时先手动命名
        # print('directory', directory)  # 不含文件名的路径
        # print('name', filename)  # 包含文件名的路径
        name = filename.partition(directory+'/')[2]
        db.session.add(Img(path=name))
        db.session.commit()

    def on_rename(self, full_path, dir_base, filename):
        # TODO:修改文件名后更新数据库
        print('full_path', full_path)  # 包含旧文件名的路径
        print('dir_base', dir_base)  # 文件路径，不含文件名
        print('filename', filename)  # 新文件名

    def on_file_delete(self, full_path, filename):
        # TODO:删除后从数据库删除
        print('full_path', full_path)  # 包含文件名的完整路径
        print('filename', filename)  # 文件名


admin.add_view(MyFileAdmin(pic_path, '/static/pictures/', name='Static Files'))

admin.add_view(MyView(name='Editor'))
