from main.src.controller.parking_lot_manager import ParkingLotManager
from main.src.controller.ticket_manager import TicketManager
from main.src.model.slot import Slot


class ParkingLot:

    def __init__(self, maxSlots):
        self.maxSlots = maxSlots
        self.ticket_manager = TicketManager()
        self.parking_lot_manager = ParkingLotManager()
        self.slots = self.create_slots(self.maxSlots)

    def get_slots(self):
        return self.slots

    def get_ticket_manager(self):
        return self.ticket_manager

    def get_parking_lot_manager(self):
        return self.parking_lot_manager

    def create_slots(self, maxSlots):
        self.slots = []
        for i in range(1, maxSlots + 1):
            self.slots.append(Slot(i, i))
        return self.slots







