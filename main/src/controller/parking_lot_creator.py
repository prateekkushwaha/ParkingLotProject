class ParkingLotCreator:
    __shared_instance = "Parking Lot"

    def __init__(self):
        if ParkingLotCreator.__shared_instance != "Parking Lot":
            raise Exception("Parking lot already created")
        ParkingLotCreator.__shared_instance = self

    @staticmethod
    def getParkingLot(self):
        if ParkingLotCreator.__shared_instance == "Parking Lot":
            ParkingLotCreator()
        return ParkingLotCreator.__shared_instance
