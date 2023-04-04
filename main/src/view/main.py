from view.runner import Runner


class Main:
    file_location = "C:\\Users\\Prateekk\\IdeaProjects\\ParkingLotProject\\main\\resources\\parking_lot_simulation.txt"

    def __main__(self):
        print('Fetching instructions from %s', self.file_location)
        file = open(self.file_location, "r")

        for line in file.readline():
            if not line.startswith(" "):
                commands = line.split(" ")
                Runner.runCommand(commands)

            else:
                break

        print("All instructions executed")
