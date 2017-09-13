from django_vaultkeeper_adaptor import vaultkeeper_adaptor
import json
from gem.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'gem_test.db',
    }
}

with open ('./data/creds.json') as f:
    data = json.loads(f)

vk_adaptor = vaultkeeper_adaptor.VKAdaptor(data=data,
                                           DATABASES=DATABASES,
                                           BROKER_URL=BROKER_URL)
vk_adaptor.process_all()

DEBUG = True
CELERY_ALWAYS_EAGER = True

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
