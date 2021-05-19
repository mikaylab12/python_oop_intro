# python Examples:

class UberEats():

    def __init__(self):
        self.fare = 0
        self.distance = 0

    def request_uber(self):
        return "Uber Requested"

    def start_trip(self):
        return "Trip Started"

toyota = UberEats()
print(toyota.request_uber())
print(toyota.fare)