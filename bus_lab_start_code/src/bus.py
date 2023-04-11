class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passenger =[]

    def drive(self):
        return "Brum brum"
    def passenger_count(self):
        return len(self.passenger)
    
    def pick_up(self, new_passenger):
        self.passenger.append(new_passenger)

    def drop_off(self, passenger):
        self.passenger.remove(passenger)

    def empty_bus(self):
        self.passenger = []

        
