import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fit_track_pro.settings')

app = Celery('fit_track_pro')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'training_reminder': {
        'task': 'workouts.tasks.training_reminder',
        'schedule': crontab(hour="7", minute="0")

    }
}
