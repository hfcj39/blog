# coding=utf-8
from models import *
from os import path

# check if db exist

# print(path.abspath(path.dirname(__file__)+'/database.db'))

if path.isfile(path.abspath(path.dirname(__file__)+'/database.db')):
    print('database found!')
else:
    print('creating database!')
    db.drop_all()
    db.create_all()
