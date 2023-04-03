from main.src.controller.parking_lot_creator import ParkingLotCreator
from main.src.executor.command_executor import CommandExecutor
from main.src.instructions.output import Output


class CreateParkingLotExecutor(CommandExecutor):

    def execute(self, params):
        __slots = int(params[0])
        ParkingLotCreator.create_parking_lot(__slots)
        print(Output.Created_Parking_Lot, __slots)

