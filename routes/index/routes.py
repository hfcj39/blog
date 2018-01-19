from . import index


@index.route('/getIndexPage')
def getIndexPage():
    return '1'
