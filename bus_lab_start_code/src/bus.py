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
        #self.passenger.clear()
    def pick_up_passenger_from_bus_stop(self, bus_stop_to_pick_up_from):
        for passenger in bus_stop_to_pick_up_from.queue:
            self.pick_up(passenger)
        self.passenger.append(bus_stop_to_pick_up_from.queue)
        
