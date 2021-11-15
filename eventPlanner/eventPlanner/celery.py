import os
from celery import Celery
from celery.schedules import crontab
# from ..scheduler.models import State
from .eventPlanner.eventPlanner.scheduler.models import State
# from eventPlanner.scheduler.models import State

# from ..scheduler.models import State
# from .scheduler.models import State

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventPlanner.settings')

app = Celery('eventPlanner')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'refresh-events-twice-a-day': {
        'task': 'scheduler.tasks.refresh',
        # 'schedule': crontab(minute=0, hours='4,14'),
        'schedule': crontab(minute=1),
        'args': State.objects
    },
}
# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
