from src.controller.slot_finder import SlotFinder
from src.controller.ticket_manager import TicketManager
from src.executor.command_executor import CommandExecutor
from src.instructions.output import Output
from src.model.car import Car
from src.model.parking_lot import ParkingLot


class ParkingExecutor(CommandExecutor):

    def execute(self, params):
        _car = Car(params[0], params[1])
        _slot = SlotFinder().find_available_slot()
        TicketManager().issueTicket(_car, _slot)

        # List indexing starts from 0 whereas slot numbers start from 1
        ParkingLot().slots[_slot.slot_number - 1].car = _car
        print(Output.Allocated_Slot_Number.value.format(_slot.slot_number))
