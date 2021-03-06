from ..models import User
from ..models import Event
from . import travel
from functools import cmp_to_key


# def check_conflict_today(event1, event2):
#     if event1.end_time < event2.start_time:
#         return False
#     elif event2.end_time < event1.start_time:
#         return False
#     else:
#         return True

class travelTimeMatrix:
    # events are pre-sorted since this is being called in ALGO
    def __init__(self, origin, events):
        self.num_map = {}
        for i, val in enumerate(events):
            self.num_map[val] = i

        self.origin = origin
        self.events = events
        self.time_array = self.compare_dist()

    def compare_dist(self):
        event_list = self.events
        q = len(event_list)
        w = len(event_list) + 1
        distance = [[0 for x in range(w)] for y in range(w)]
        for i in range(q):
            curr_travel_time = travel.get_travel_time(self.origin, event_list[i].address1)
            print("THIS IS CURR TRAVEL TIME:")
            print(curr_travel_time, "\n")
            distance[0][i] = curr_travel_time
            distance[i][0] = curr_travel_time
        for i in range(1, q):
            for j in range(i + 1, q):
                curr_travel_time = travel.get_travel_time(event_list[i].address1, event_list[j].address1)
                print("Event 1: ", str(event_list[i]), " Event 2: ", str(event_list[j]), " Travel time between: ", str(curr_travel_time))
                distance[i][j] = curr_travel_time
                distance[j][i] = curr_travel_time

        # print("TIME ARRAY:")
        # print(distance)
        return distance

    def get_time(self, event1, event2):
        index1 = self.num_map[event1]
        index2 = self.num_map[event2]
        print("This is what is in time array: ")
        print(self.time_array[index1][index2])
        return self.time_array[index1][index2]


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


def check_conflict(event1, event2, time_matrix):
    travel_time = time_matrix.get_time(event1,event2)

    if travel_time == 0:
        if event1.end_time < event2.start_time:
            # print("Event 1 : ", event1, " ", event1.end_time," Event 2: ", event2, " ", event2.start_time)
            # print("False")
            return False
        elif event2.end_time < event1.start_time:
            # print("Event 1 : ", event1.end_time, " Event 2: ", event2.start_time)
            # print("False")
            return False
        else:
            # print("True")
            return True
    else:
        if event1.end_time + travel_time < event2.start_time:
            # print("Event 1 : ", event1, " ", event1.end_time," Event 2: ", event2, " ", event2.start_time)
            # print("False")
            return False
        elif event2.end_time + travel_time < event1.start_time:
            # print("Event 1 : ", event1.end_time, " Event 2: ", event2.start_time)
            # print("False")
            return False
        else:
            # print("True")
            return True


# event list is a list of events sorted by end time, event index is the index of the current event in the list
def closest_non_conflict(time_matrix, event_index):
     curr_index = event_index - 1
     event_list = time_matrix.events
     e = event_list[event_index]
     while curr_index >= 0:
         curr_event = event_list[curr_index]
         if not check_conflict(curr_event, e, time_matrix):
             return curr_event
         curr_index -= 1
     return None


def closest_non_conflict_index(time_matrix, event_index):

    # event_list = time_matrix.events
    # print("EVENT INDEX: " + str(event_index))
    # print(len(event_list))
    if event_index >= len(time_matrix.events):
        return -1
    # e = event_list[event_index]
    e = time_matrix.events[event_index] #e is the current event; trying to find event immediately before e
    curr_index = event_index - 1  # start one index before event index
    while curr_index >= 0:
        # curr_event = event_list[curr_index]
        curr_event = time_matrix.events[curr_index]
        if not check_conflict(curr_event, e, time_matrix):
            return curr_index
        curr_index -= 1
    return -1


def compCategory(event, user):
    internal_name = event.category
    # internal_name = categoryDict[category_for_dictionary]
    weight = 5
    if internal_name == 'music':
        weight = user.music
    if internal_name == 'visual-arts':
        weight = user.visual
    if internal_name == 'performing-arts':
        weight = user.performing
    if internal_name == 'film':
        weight = user.film
    if internal_name == 'lectures-books':
        weight = user.lectures
    if internal_name == 'fashion':
        weight = user.fashion
    if internal_name == 'food-and-drink':
        weight = user.food
    if internal_name == 'charities':
        weight = user.charity
    if internal_name == 'sports-active-life':
        weight = user.sports
    if internal_name == 'nightlife':
        weight = user.nightlife
    if internal_name == 'kids-family':
        weight = user.family
    if internal_name == 'festivals-fairs':
        weight = user.festivals
    if internal_name == 'other':
        return 5
    return weight


def compareCost(event1, max_cost):
    if event1.cost > max_cost:
        return 0
    else:
        return 1


# distance[0][1] is travel time between origin to event 1
# distance[1][0] is travel time between event 1 to origin
# event_list is all valid events (start, end, state)


def less_than(event1, event2):
    if event1.end_time < event2.end_time:
        return -1
    elif event2.end_time < event1.end_time:
        return 1
    else:
        return 0


def sortEventsByTime(event_list):
    return sorted(event_list, key=cmp_to_key(less_than))


def get_schedule(origin, event_list, user):
    events = sortEventsByTime(event_list)
    t = travelTimeMatrix(origin, events)
    # print("Does this even run")
    n = len(events)
    optimal = [0] * (n + 1)
    opt_list = []
    for i in range(n + 1):
        opt_list.append([])

    for i in range(1, n + 1):
        prev_no_conflict = closest_non_conflict_index(t, i - 1)  # last index where event does not conflict
        prev_no_conflict_event = closest_non_conflict(t, i - 1) # last event with no conflict with index in events

        # print("Current index: " + str(i))
        # print("Current event: " + str(events[i - 1]))
        # print("Prev no conflict event: " + str(prev_no_conflict_event))
        # print("Index of prev no conflict: " + str(prev_no_conflict))
        include_curr = compCategory(events[i - 1], user)
        if prev_no_conflict >= 0:
            include_curr += optimal[prev_no_conflict+1]  # value of including curr



        exclude_curr = optimal[i - 1]  # value of excluding curr
        # print("Include curr: " + str(include_curr))
        # print("Exclude curr: " + str(exclude_curr))
        if include_curr > exclude_curr:
            if prev_no_conflict >= 0:
                opt_list[i].extend(opt_list[prev_no_conflict+1])
            opt_list[i].append(events[i - 1])
            optimal[i] = include_curr
            # print("INCLUDED")
        else:
            opt_list[i].extend(opt_list[i - 1])
            optimal[i] = exclude_curr
            # print("EXCLUDED")
        # print("Current optimal: ")
        print(opt_list[i])

    # print("All event lists:")
    # for val in opt_list:
    #     print(val)
    # print(optimal[n])
    # print(opt_list[n])
    return opt_list[n]
