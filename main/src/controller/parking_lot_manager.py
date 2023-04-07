from src.model.parking_lot import ParkingLot


class ParkingLotManager:

    @classmethod
    def assign_car_to_slot(cls, car, slot):
        # List indexing starts from 0 whereas slot numbers start from 1
        ParkingLot().slots[slot.slot_number - 1].car = car

    @classmethod
    def release_car_from_slot(cls, car, slot):
        if slot.car.registration_number == car.registration_number:
            ParkingLot().slots[slot.slot_number - 1].car = None
