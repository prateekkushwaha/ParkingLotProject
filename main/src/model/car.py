class Car:

    def __init__(self, registrationNumber, carColour):
        self.registrationNumber = registrationNumber
        self.carColour = carColour

    def getCarRegistrationNumber(self):
        return self.registrationNumber

    def getCarColour(self):
        return self.carColour
