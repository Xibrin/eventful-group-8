
def check_conflict_today(event1, event2):
    if event1.end_time < event2.start_time:
        return False
    elif event2.end_time < event1.start_time:
        return False
    else:
        return True


def check_conflict(event1, event2):
    if event1.end_date_time < event2.start_date_time:
        return False
    elif event2.end_date_time < event1.start_date_time:
        return False
    else:
        return check_conflict_today(event1, event2)


def closest_non_conflict(event_list, event_index):
    curr_index = event_index-1
    e = event_list[event_index]
    while curr_index >= 0:
        curr_event = event_list[curr_index]
        if not check_conflict(curr_event, e):
            return curr_event
        curr_index -= 1
    return None

def sort(event_list){

}
