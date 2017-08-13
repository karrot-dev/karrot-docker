import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'db',
        'PASSWORD': 'db',
        'HOST': 'db',
        'PORT': '',
    }
}

INFLUXDB_DISABLED = False
INFLUXDB_HOST = 'influxdb'
INFLUXDB_PORT = '8086'
INFLUXDB_USER = ''
INFLUXDB_PASSWORD = ''
INFLUXDB_DATABASE = 'fstool'
INFLUXDB_TAGS_HOST = 'docker'
INFLUXDB_TIMEOUT = 2
INFLUXDB_USE_CELERY = False
INFLUXDB_USE_THREADING = True

SHELL_PLUS_PRE_IMPORTS = (
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'maildev'

DEFAULT_FROM_EMAIL = "fstool@yunity.org"

SECRET_KEY = 'c*#4=n$s4!*gdgq3nora#a$*xznctg-6=4_edeg9^dsxk&=p=$'
DEBUG = True
HOSTNAME = 'http://localhost:8000'

ALLOWED_HOSTS = ['*']
