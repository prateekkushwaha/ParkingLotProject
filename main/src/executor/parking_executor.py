from main.src.controller.ticket_manager import TicketManager
from main.src.executor.command_executor import CommandExecutor
from main.src.model.car import Car
from main.src.model.parking_lot import ParkingLot


class ParkingExecutor(CommandExecutor):

    def execute(self, params):
        _car = Car(params[0], params[1])
        ticket = ParkingLot().get_ticket_manager().issueTicket(_car)
        ticket.get_slot().assignCar(ticket.get_car())
