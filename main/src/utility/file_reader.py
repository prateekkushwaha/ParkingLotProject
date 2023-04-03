import os


class FileReader:
    __file_location = os.getcwd()

    def __init__(self, filename):
        self.file = open(self.__file_location, "r")
