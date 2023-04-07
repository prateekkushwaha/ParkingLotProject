from src.model.ticket import Ticket


class TicketManager:

    def __init__(self, parking_lot):
        self._carsInParkingLot = 0
        self.tickets = []
        self.parking_lot = parking_lot

    def issueTicket(self, car, slot):
        self._carsInParkingLot += 1
        self.tickets.append(Ticket(car, slot))

    """
    def get_ticket_by_slot_number(self, slotNumber):
        for ticket in self.tickets:
            if ticket.get_slot().get_slot_number() == slotNumber:
                return ticket

        raise Exception("Invalid slot number...")
    """

    def releaseTicket(self, assigned_car, assigned_slot):
        for ticket in self.tickets:
            if ticket.slot.slot_number == assigned_slot.slot_number and \
                    ticket.car.registration_number == assigned_car.registration_number:
                self.tickets.remove(ticket)
                self._carsInParkingLot -= 1
                return 0
        return -1
