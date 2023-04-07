from src.model.ticket import Ticket


class TicketManager:
    carsInParkingLot = 0
    tickets = []

    @classmethod
    def issueTicket(cls, car, slot):
        cls.carsInParkingLot += 1
        cls.tickets.append(Ticket(car, slot))

    @classmethod
    def releaseTicket(cls, car, slot):
        for ticket in cls.tickets:
            if ticket.car.registration_number == car.registration_number \
                    and ticket.slot.slot_number == slot.slot_number \
                    and ticket.is_valid is True:
                ticket.is_valid = False
                break
