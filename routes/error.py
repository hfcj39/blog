from flask import render_template
from . import error


@error.app_errorhandler(404)
def printerr(err):
    return render_template('error.html', data={
        "code": '404',
        "msg": "meiyou"
    })
