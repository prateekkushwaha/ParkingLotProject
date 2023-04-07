from src.controller.parking_lot_manager import ParkingLotManager
from src.controller.slot_finder import SlotFinder
from src.controller.ticket_manager import TicketManager
from src.executor.command_executor import CommandExecutor
from src.instructions.output import Output


class CarExitExecutor(CommandExecutor):

    def execute(self, params):
        _slot_number = params[0]
        _slot = SlotFinder().find_slot(_slot_number)
        _car = _slot.car
        TicketManager.releaseTicket(_car, _slot)
        ParkingLotManager.release_car_from_slot(_car, _slot)
        print(Output.Slot_Number_Free.value.format(_slot.slot_number))
