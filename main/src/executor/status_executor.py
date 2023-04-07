from src.executor.command_executor import CommandExecutor
from src.instructions.output import Output
from src.model.parking_lot import ParkingLot


class StatusExecutor(CommandExecutor):

    def execute(self, params):
        print(Output.Status_Table_Cols)
        slots = ParkingLot().get_slots()

        for slot in slots:
            if slot.car is not None:
                print("%s %s %s", slot.slotNumber, slot.car.registrationNumber, slot.car.carColour)
