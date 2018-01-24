from flask import Blueprint

index = Blueprint('index', __name__)
error = Blueprint('error', __name__)
# admin = Blueprint('admin', __name__)

import error, front, admin
