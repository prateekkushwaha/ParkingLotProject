from src.controller.slot_creator import SlotCreator
from src.executor.command_executor import CommandExecutor
from src.instructions.output import Output


class CreateParkingLotExecutor(CommandExecutor):

    def __init__(self):
        pass

    def execute(self, params):
        _slots = int(params[0])
        _slot_creator = SlotCreator()
        _slot_creator.create_slots(_slots)
        print(Output.Created_Parking_Lot.value.format(_slots))
