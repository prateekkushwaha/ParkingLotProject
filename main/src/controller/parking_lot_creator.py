from main.src.model.parking_lot import ParkingLot


class ParkingLotCreator:

    @staticmethod
    def create_parking_lot(max_slots):
        ParkingLot.__single_instance = "Parking_Lot"
        return ParkingLot().create_slots(max_slots)
