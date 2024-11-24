import os
from celery import Celery

from MiniProj import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MiniProj.settings')

app = Celery('MiniProj')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)