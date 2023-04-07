class ParkingLotManager:

    def __init__(self, parking_lot):
        self.parking_lot = parking_lot

    """
    def get_slot_by_slot_number(self, slotNumber):
        from src.model.parking_lot import ParkingLot
        self.slots = ParkingLot().get_slots()

        for _slot in self.slots:
            if _slot.slotNumber == slotNumber:
                return _slot
        raise Exception("Illegal slot number")

    def get_car_by_slot_number(self, slotNumber):
        slot = self.get_slot_by_slot_number(slotNumber)
        return slot.car"""

    def assign_car_to_slot(self, car, slot_assigned):
        for slot in self.parking_lot.slots:
            if slot.slot_number == slot_assigned.slot_number:
                slot.car = car

    def release_car_from_slot(self, car, slot_assigned):
        for slot in self.parking_lot.slots:
            if slot.slot_number == slot_assigned.slot_number:
                slot.car = None
