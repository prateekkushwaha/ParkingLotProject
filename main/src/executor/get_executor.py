from src.executor.status_executor import StatusExecutor
from src.executor.car_exit_executor import CarExitExecutor
from src.executor.create_parking_lot_executor import CreateParkingLotExecutor
from src.executor.parking_executor import ParkingExecutor


class ExecutorFactory:

    @staticmethod
    def get_executor(param):
        if param == "create_parking_lot":
            return CreateParkingLotExecutor()

        elif param == "park":
            return ParkingExecutor()

        elif param == "leave":
            return CarExitExecutor()

        elif param == "status":
            return StatusExecutor()

        """
        elif command == "registration_numbers_for_cars_with_colour":
            return FindCarByColorExecutor.__class__

        elif command == "slot_numbers_for_cars_with_colour":
            return FindSlotNumberByCarColour.__class__

        elif command == "slot_number_for_registration_number":
            return FindSlotNumberByRegistrationNumber.__class__"""
