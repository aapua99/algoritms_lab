from printer import Printer


class Read:
    def read(self):
        file = open("printer_input_data.csv", "r")
        array = []
        for i in file:
            lib = i.split(",")
            array.append(Printer(str(lib[0]), int(lib[1]), int(lib[2])))
        return array
