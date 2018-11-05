# https://realpython.com/python-csv/
import csv
from elements import Element

class PeriodicTable:
    def __init__(self):
        self.elements = []
        with open('elements.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.elements.append(Element(row[0], row[1], row[2], row[3]))
                # print(f'\t{row[0]} has an atomic number of {row[1]}. Its periodic symbol is {row[2]}, and its atomic weight is {row[3]} g.')
    def __str__(self):
        result = ""
        for i in self.elements:
            result += str(i) + "\n"
        return result

    def elchoice(self, elchoice):
        for elementdata in self.elements:
            if elementdata.element.upper() == elchoice.upper():
                return elementdata

    def weight(self):
        # be able to divide the molecular formula into elements and add their weights by that and multiplying by the number after it
        pass


table1 = PeriodicTable()
# print(str(table1))


print("Welcome to the Periodic Table Mastery Chart! This program is designed to help the user with chemistry homework and become well-equipped with the elements.\n")
elchoice = input("Enter an element name to get its data: ")

print(table1.elchoice(elchoice))
