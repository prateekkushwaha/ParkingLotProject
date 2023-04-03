from main.src.controller.ticket_manager import TicketManager
from main.src.executor.command_executor import CommandExecutor


class ParkingExecutor(CommandExecutor):

    def __init__(self):
        self.ticket_manager = None

    def execute(self, slots):
        self.ticket_manager = TicketManager()
        ticket = self.ticket_manager.issueTicket()
        ticket.get_slot().assignCar(ticket.get_car())
