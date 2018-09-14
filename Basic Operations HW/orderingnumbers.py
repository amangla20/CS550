#import the library required to take command line arguments
import sys

"""
# old interpretation of instructions
x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]
"""

# take command-line arguments
x = input("First number: ")
y = input("Second number: ")
z = input("Third number: ")

# if-statement that prints true or false
if ((float(x) < float(y) and float(y) < float(z)) or (float(x) > float(y) and float(y) > float(z))):
	print("True")
else:
	print("False")


