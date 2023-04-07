from src.model.parking_lot import ParkingLot
from sys import maxsize


class SlotFinder:

    def __init__(self):
        self.parking_lot = ParkingLot()

    def find_available_slot(self):
        _desired_slot = None
        _distance = maxsize
        for slot in self.parking_lot.slots:
            if slot.car is None and slot.entryPointDistance < _distance:
                _desired_slot = slot
                _distance = slot.entryPointDistance

        return _desired_slot

    def find_slot(self, slot_number):
        for slot in self.parking_lot.slots:
            if slot.slot_number == int(slot_number):
                return slot
