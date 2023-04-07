from src.controller.parking_lot_manager import ParkingLotManager
from src.controller.slot_finder import SlotFinder
from src.controller.ticket_manager import TicketManager
from src.executor.command_executor import CommandExecutor
from src.instructions.output import Output
from src.model.car import Car


class ParkingExecutor(CommandExecutor):

    def execute(self, params):
        _car = Car(params[0], params[1])
        _slot = SlotFinder().find_available_slot()
        TicketManager.issueTicket(_car, _slot)
        ParkingLotManager.assign_car_to_slot(_car, _slot)
        print(Output.Allocated_Slot_Number.value.format(_slot.slot_number))
