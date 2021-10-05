
class Route:
    def __init__(self, directions, start_pos = None, end_pos = None):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.directions = directions
        self.tolls = directions["route"]["hasTollRoad"]
        self.distance = directions["route"]["distance"]
        self.time = directions["route"]["time"]
        self.fuel_use = directions["route"]["fuelUsed"]
        # self.start_lng = directions["route"][]
        # self.end_pos = end_pos

    # Helper Methods
    def calculate_fuel_cost(self):
        # take fuel use and calculate fuel cost based on local fuel prices
        pass

    def get_toll_price(self):
        # find toll on route and determine price based on other database
        pass

    def get_distance(self, unit):
        # take distance and return in preferred unit
        pass

    def get_time(self, format):
        # take time format from Json and return in local time format
        pass