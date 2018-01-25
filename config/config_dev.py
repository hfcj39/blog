import os

# DATABASE_USER = 'root'
# DATABASE_PASSWORD = 'root'
# DATABASE_URL = 'localhost:3306'

basedir = os.path.abspath(os.path.dirname(__file__))[0:-7]
print('database_path:'+basedir)

# sqlite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')

# MySQL
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+DATABASE_USER+':'+DATABASE_PASSWORD+'@'+DATABASE_URL+'/cambricon'

# PostgreSQL
# SQLALCHEMY_DATABASE_URI = 'postgresql://fhiutc:123456788@115.159.43.33/fhiutc'

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_POOL_SIZE = 10

secret = 'aGVsbG8gd29ybGQ='
