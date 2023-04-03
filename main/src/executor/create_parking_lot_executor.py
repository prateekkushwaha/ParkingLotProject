from main.src.controller.parking_lot_creator import ParkingLotCreator
from main.src.executor.command_executor import CommandExecutor
from main.src.instructions.output import Output


class CreateParkingLotExecutor(CommandExecutor):

    def execute(self, slots):
        parkingLot = ParkingLotCreator.getParkingLot(slots)
        print(Output.Created_Parking_Lot, slots)

