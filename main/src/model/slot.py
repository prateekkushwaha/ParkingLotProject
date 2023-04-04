class Slot:

    def __init__(self, slotNumber, entryPointDistance):
        self.slotNumber = slotNumber
        self.entryPointDistance = entryPointDistance
        self.car = None

    def get_slot_number(self):
        return self.slotNumber

    def assignCar(self, car):
        if self.car is None:
            self.car = car

    def release_car(self):
        if self.car is not None:
            self.car = None
        else:
            raise Exception("Slot already empty")
