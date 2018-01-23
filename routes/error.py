# -*-coding:utf-8 -*-
from flask import render_template
from . import error


@error.app_errorhandler(404)
def err_400(err):
    return render_template('error.html', data={
        "code": '404',
        "msg": u"没有你要访问的页面哦~"
    })


@error.app_errorhandler(500)
def err_500(err):
    return render_template('error.html', data={
        "code": '500',
        "msg": u"服务器出错~"
    })
