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

table1 = PeriodicTable()
print(str(table1))