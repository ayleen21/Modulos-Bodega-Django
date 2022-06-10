import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
#SQL LITE
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}
#MYSQL
MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dba_ges',
        'USER': 'user_ges',
        'PASSWORD': '97Emc@l1',
        'HOST': 'ges_db',
        'PORT': '3306',
    }
}