from . import index


@index.route('/')
def getIndexPage():
    return 'index'
