from main.src.executor.command_executor import CommandExecutor
from main.src.model.parking_lot import ParkingLot


class CarExitExecutor(CommandExecutor):

    def __init__(self):
        self.ticket_manager = None
        self.slot = None
        self.parking_lot_manager = None
        self.parking_lot = None

    def execute(self, params):
        # Remove car slot slot
        _slot_number = params[0]
        self.parking_lot_manager = ParkingLot().get_parking_lot_manager()
        self.slot = self.parking_lot_manager.get_slot_by_slot_number(_slot_number)
        self.slot.release_car()

        self.ticket_manager = ParkingLot().get_ticket_manager()
        self.ticket_manager.releaseTicket(_slot_number)
