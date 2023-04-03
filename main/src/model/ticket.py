class Ticket:

    def __init__(self, car, slot):
        self.valid = False
        self.slot = slot
        self.car = car

    def get_car(self):
        return self.car

    def get_slot(self):
        return self.slot

    def set_status_of_ticket(self, status):
        self.valid = status

    def get_ticket_status(self):
        return self.valid

