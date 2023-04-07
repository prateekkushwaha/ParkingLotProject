from src.model.parking_lot import ParkingLot
from src.model.slot import Slot
import logging


class SlotCreator:

    @classmethod
    def create_slots(cls, max_slots):
        for i in range(1, max_slots + 1):
            logging.debug("Creating slot number {})".format(i))
            ParkingLot().slots.append(Slot(i, i))
