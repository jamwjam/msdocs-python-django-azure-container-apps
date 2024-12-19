import os

from .get_token import get_token
from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = os.getenv('LOCAL_SECRET_KEY')

# Don't use Whitenoise to avoid having to run collectstatic first.
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

ALLOWED_HOSTS = ['*']

# Configure connection setting for local PostgreSQL instance.
# Set these environment variables in the .env file for this project.  

if 'USE_REMOTE_POSTGRESQL' in os.environ:
    # Configure database connection for remote PostgreSQL instance.
    DBHOST=os.environ['DBHOST'] + ".postgres.database.azure.com"
    DBNAME=os.environ['DBNAME']
    DBUSER=os.environ['DBUSER']
    DBPASS='set with get_token()'
else:
    # Configure database connection for local PosgreSQL instance.
    DBHOST=os.environ['DBHOST']
    DBNAME=os.environ['DBNAME']
    DBUSER=os.environ['DBUSER']
    DBPASS=os.environ['DBPASS']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DBNAME,
        'HOST': DBHOST,
        'USER': DBUSER,
        'PASSWORD': DBPASS,
    }
}
get_token()
