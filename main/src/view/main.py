from src.view.runner import Runner


class Main:
    file_location = "C:\\Users\\Prateekk\\IdeaProjects\\ParkingLotProject\\main\\resources\\parking_lot_simulation.txt"

    def main(self):
        print("Fetching instructions from {}".format(self.file_location))
        file = open(self.file_location, "r")

        for line in file.readlines():
            if not (line.startswith(" ") or line.startswith("\n")):
                commands = line.split(" ")
                Runner.runCommand(commands)
            else:
                break
        print("All instructions executed")


if __name__ == "__main__":
    Main().main()

