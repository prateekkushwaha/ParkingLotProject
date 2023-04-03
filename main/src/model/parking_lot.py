from main.src.controller.parking_lot_manager import ParkingLotManager
from main.src.controller.ticket_manager import TicketManager
from main.src.model.slot import Slot


class ParkingLot:

    __single_instance = ""

    def __init__(self):
        if self.__single_instance == "":
            raise Exception("Parking lot already created")
        else:
            self.maxSlots = 0
            self.ticket_manager = TicketManager()
            self.parking_lot_manager = ParkingLotManager()
            self.slots = []

    def get_slots(self):
        return self.slots

    def get_ticket_manager(self):
        return self.ticket_manager

    def get_parking_lot_manager(self):
        return self.parking_lot_manager

    def create_slots(self, maxSlots):
        for i in range(1, maxSlots + 1):
            self.slots.append(Slot(i, i))







