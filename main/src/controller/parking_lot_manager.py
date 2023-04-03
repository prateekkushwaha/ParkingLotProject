class ParkingLotManager:

    def get_slot_by_slot_number(self, slotNumber):
        slots = self.parkingLot.get_slots()

        for slot in slots:
            if slot.slotNumber == slotNumber:
                return slot
        raise Exception("Illegal slot number")

    def get_car_by_slot_number(self, slotNumber):
        slot = self.get_slot_by_slot_number(slotNumber)
        return slot.car

    def get_available_slot(self, slots):
        """

        :rtype: Slot object if free slot is found, else -1
        """
        for i in range(len(slots)):
            if slots[i] is None:
                return i + 1
        return -1
