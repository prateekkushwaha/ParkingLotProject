from main.src.controller.parking_lot_creator import ParkingLotCreator
from main.src.exceptions.parking_lot_full_exception import ParkingLotFullException
from main.src.model.ticket import Ticket


class TicketManager:

    def __init__(self):
        self.carsInParkingLot = 0
        self.tickets = []

    def issueTicket(self, car):
        if self.carsInParkingLot == self.parkingLot.maxSlots:
            raise ParkingLotFullException
        else:
            self.carsInParkingLot += 1
            availableSlot = self.parkingLot.getAvailableSlot()
            self.tickets.append(Ticket(car, availableSlot))

    def get_ticket_by_slot_number(self, slotNumber):
        for ticket in self.tickets:
            if ticket.get_slot().get_slot_number() == slotNumber:
                return ticket

        raise Exception("Invalid slot number...")