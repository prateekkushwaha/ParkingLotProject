class SlotFinder:

    def __init__(self, parking_lot):
        self.parking_lot = parking_lot

    def find_available_slot(self):
        for slot in self.parking_lot.slots:
            if slot.car is None:
                return slot.slot_number
        return -1
