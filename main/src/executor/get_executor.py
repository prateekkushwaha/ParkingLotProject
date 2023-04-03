from main.src.executor.car_exit_executor import CarExitExecutor
from main.src.executor.create_parking_lot_executor import CreateParkingLotExecutor
from main.src.executor.parking_executor import ParkingExecutor


class ExecutorFactory:

    @staticmethod
    def get_executor(param):
        if param == "create_parking_lot":
            return CreateParkingLotExecutor.__class__

        elif param == "park":
            return ParkingExecutor.__class__

        elif param == "leave":
            return CarExitExecutor.__class__

        """
        elif command == "status":
            return ParkingLotStatusExecutor.__class__

        elif command == "registration_numbers_for_cars_with_colour":
            return FindCarByColorExecutor.__class__

        elif command == "slot_numbers_for_cars_with_colour":
            return FindSlotNumberByCarColour.__class__

        elif command == "slot_number_for_registration_number":
            return FindSlotNumberByRegistrationNumber.__class__"""






