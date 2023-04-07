from src.executor.command_executor import CommandExecutor
from src.model.car import Car
from src.model.parking_lot import ParkingLot


class ParkingExecutor(CommandExecutor):

    def execute(self, params):
        _car = Car(params[0], params[1])
        ticket = ParkingLot().get_ticket_manager().issueTicket(_car)
        ticket.get_slot().assignCar(ticket.get_car())
