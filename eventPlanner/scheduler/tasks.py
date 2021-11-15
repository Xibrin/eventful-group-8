import celery
from .support import event_finder
import models
from finished_project import project

@app.task
def refresh(states):
    print('Request: {0!r}'.format(self.request))
    Event.objects.all().delete()
    for state in states:
        new_event_finder = event_finder.EventFinder(location=state, start_time=int(
            parser.parse(datetime.datetime.now().isoformat()).timestamp()))
        new_event_finder.save_all_events()