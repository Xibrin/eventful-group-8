

class Location:

    def __init__(self, address1, city, zip_code, state, country, display):
        self.address1 = address1
        self.city = city
        self.zip_code = zip_code
        self.state = state
        self.country = country
        self.display = display

    def display_address(self):
        print(self.display)
        return self.display