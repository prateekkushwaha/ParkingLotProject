from model.parking_lot import ParkingLot


class ParkingLotManager:

    def __init__(self):
        self.slots = None

    def get_slot_by_slot_number(self, slotNumber):
        self.slots = ParkingLot().get_slots()

        for _slot in self.slots:
            if _slot.slotNumber == slotNumber:
                return _slot
        raise Exception("Illegal slot number")

    def get_car_by_slot_number(self, slotNumber):
        slot = self.get_slot_by_slot_number(slotNumber)
        return slot.car

    def get_available_slot(self, slots):
        for i in range(len(slots)):
            if slots[i] is None:
                return i + 1
        return -1
