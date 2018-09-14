import math
import random

number = random.randrange(0,100,10) #random number between 0 and 100 inclusive, multiple of 10
print(number)

# random() is a random number between 0 and 1 (including 0)

# if you have a long library name you can type into terminal,
#import libraryName as abbreviation

theta = input("pick any number in radians: ")

result = math.cos(float(theta))**2 + math.sin(float(theta))**2

print(result)