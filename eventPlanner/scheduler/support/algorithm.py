from ..models import User
from ..models import Event
from . import travel

# def check_conflict_today(event1, event2):
#     if event1.end_time < event2.start_time:
#         return False
#     elif event2.end_time < event1.start_time:
#         return False
#     else:
#         return True

categoryDict = {
    "music": "music",
    "visual-arts": "visual",
    "performing-arts": "performing",
    "film": "film",
    "lectures-books": "lectures",
    "fashion": "fashion",
    "food-and-drink": "food",
    "festivals-fairs": "festivals",
    "charities": "charity",
    "sport-active-life": "sports",
    "nightlife": "nightlife",
    "kids-family": "family"
}


def check_conflict(event1, event2):
    if event1.end_time < event2.start_time:
        return False
    elif event2.end_time < event1.start_time:
        return False
    else:
        return True
        # check_conflict_today(event1, event2)


def closest_non_conflict(event_list, event_index):
    curr_index = event_index - 1
    e = event_list[event_index]
    while curr_index >= 0:
        curr_event = event_list[curr_index]
        if not check_conflict(curr_event, e):
            return curr_event
        curr_index -= 1
    return None


def sort(event_list):
    weight = 0


def compCategory(event, user):
    category_for_dictionary = event.category
    weight = user.categoryDict[category_for_dictionary]
    return weight


def compareCost(event1, max_cost):
    if event1.cost > max_cost:
        return 0
    else:
        return 1


# distance[0][1] is origin to event 1
# distance[1][0] is event 1 to origin
def compareDist(origin, event_list):
    w = len(event_list) + 1
    distance = [[0 for x in range(w)] for y in range(w)]
    for i in range(w - 1):
        curr_travel_time = travel.get_travel_time(origin, event_list[i].address1)
        distance[0][i] = curr_travel_time
        distance[i][0] = curr_travel_time

    for i in range(1, w):
        for j in range(i + 1, w):
            curr_travel_time = travel.get_travel_time(event_list[i].address1, event_list[j].address1)
            print("Event 1: " + str(event_list[i]) + " Event 2: " + str(event_list[j]))
            distance[i][j] = curr_travel_time
            distance[j][i] = curr_travel_time

    return distance
