
class eventStorage:

    def __init__(self, name, start_time, end_time, location, category, info, price, outdoor, tickets, id, picture):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        if end_time is None:
            self.duration  = 7200 #manually set as 2 hours for events with no end time,  may need future adjustment
            end_time = start_time + 7200
        else:
            self.duration = end_time - start_time
        self.location = location
        self.category = category
        self.info = info
        self.price = price
        self.outdoor = outdoor
        self.tickets = tickets
        self.id = id
        self.picture = picture

    def print_name(self):
        return self.name

    def __str__(self):
        return self.name