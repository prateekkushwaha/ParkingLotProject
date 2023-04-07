from logging import info


class ParkingLot(object):
    _instance = None
    max_slots = 0
    slots = []

    def __new__(cls):
        if cls._instance is None:
            info('Creating parking lot object')
            cls._instance = super(ParkingLot, cls).__new__(cls)
        return cls._instance

