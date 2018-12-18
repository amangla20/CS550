'''
    On this assignment, you should work with a partner. You must submit what you have completed at the end of the class period, but you do not need to complete any leftover problems for homework. 
 
    For some of these problems you will need to create a class; for others, you will need to use a library. 
    You do NOT need to put all your solutions in this file, however you should keep all your solutions together, clearly labeled with descriptive file names, in one folder. 
'''
import numpy
from sympy import *
from sympy.geometry import *
from turtle import *
 
''' 1.
    Create a class, Point, that keeps track of two properties: x and y
    When a point is created, values for x and y should be provided.
 
    The methods for this class are as follows:
    rotate90: rotate the point 90° about the origin
    rotate180: rotate the point 180° about the origin
    rotaten90: rotate -90° about the origin
    translate: given 2 values, translate the point by the given amount.
    flip_horizontally: flip the point on the x-axis
    flip_vertically: flip the point on the y-axis
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotaten90(self):
        tempx = self.x
        tempy = self.y
        self.y = -1*tempx
        self.x = tempy

    def rotate180(self):
        self.x *= -1
        self.y *= -1

    def rotate90(self):
        tempx = self.x
        tempy = self.y
        self.y = tempx
        self.x = -1*tempy   

    def translate(self, orx, ory):
        self.x += orx
        self.y += ory

    def flip_vertically(self):
        self.y *= -1

    def flip_horizontally(self):
        self.x *= -1

 
 
''' 2.
    Create a class, Bicycle, that keeps track of three properties: cadence, gear, speed. 
    When a Bicycle is created, cadence, gear, and speed are accepted as arguments.
 
    The methods for this class are as follows:
    set_gear: given a value, set the gear to that value
    set_cadence: given a value, set the cadence to that value
    apply_brake: given a value, decrease the speed of the bike by that value
    speed_up: given a value, increase the speed of the bike by that value
'''
class Bicycle:
    def __init__(self, cadence, gear, speed):
        self.cadence = cadence
        self.gear = gear
        self.speed = speed

    def set_gear(self, gear):
        self.gear = gear

    def set_cadence(self, cadence):
        self.cadence = cadence

    def apply_brake(self, speed):
        self.speed -= speed

    def speed_up(self, speed):
        self.speed += speed
 
''' 3.
    Create a class, student, that keeps track of four properties: energy, hunger, stress, and hours.
    These properties have a range from 0-100, except hours, which has a range from 0-24. 100 energy means they are energetic; 100 hunger means they are very hungry; 100 stress means they are extremely stressed. When you create a new student, assume they have moderate hunger, low stress, a lot of energy, and 24 hours.
 
    The methods for the student class are as follows:
    study: Given a value (to adjust hours), study for that given length of time. Studying decreases energy and increases hunger based on the length of the study.
    sports: Given a value (to adjust hours), play sports for that given length of time. This decreases energy, increases hunger, and decreases stress based on the length of the sports.
    class: Given a value (to adjust hours), attend classes for a given length of time. This decreases energy, increases hunger, and increases stress based on the length of the class.
    take_test: Given a value (to adjust hours), this increases stress. 
    submit_paper: this decreases stress.
    eat_meal: Given a value (to adjust hours), this decreases stress, decreases hunger, and increases energy.
    sleep: Given a time (to adjust hours), this decreases stress, increases energy, and increases hunger.
    new_day: resets the hours in a day.
 
    You may not let a student do more than 24 hours worth of activities in a given day. 
'''
class Student():

    def __init__(self):
        self.energy = 90
        self.hunger = 50
        self.stress = 10
        self.hours = 0

    def study(self, timespec):
        if hours+timespec > 24:
            status = "Sorry, you can only do 24 hours of activity a day!"
        elif energy-timespec*8 <= 0:
            status = "You need sleep!"
        elif hunger+timespec*8 >= 100:
            status = "No! Eat!"
        else:
            energy -= timespec*8
            hunger += timespec*8
            hours += timespec

    def sports(self, timespec):
        if hours+timespec >= 24:
            status = "Sorry, you can only do 24 hours of activity a day!"
        elif energy-timespec*11 <= 0:
        else: 
            hours += timespec
            stress -= timespec*11
            energy -= timespec*10
            hunger += timespec*8

    def take_test(self):
        if hours+1 > 24:
            status = "Sorry, you can only do 24 hours of activity a day!"
        elif stress+33 >= 100:
            status = "You should probably go to the health center..."
        else:
            hours += 1
            stress += 33

    def submit_paper(self, timespec):
        if hours+timespec >= 24:
            status = "Sorry, you can only do 24 hours of activity a day!"
        else:
            stress -= 30

    def eat_meal(self, timespec):
        if hours+timespec >= 24:
            status = "Sorry, you can only do 24 hours of activity a day!"
        if hunger - timepec*50<0:
            status = "that's a lot of food, you didn't finish it all"
            hunger = 0
        else:
            hunger -= timespec*50
        if energy += 40*timespec > 100:
            status = "woah! you're super energized"
            energy = 100
        else:
            energy += timespec*40

        hours += timespec
            stress -= 20*timespec

    def sleep(self, timespec):
        if hours+timespec >= 24:
            status = "Sorry, you can only do 24 hours of activity a day!"
        else:
            self.energy += timespec*11
            self.hunger += timespec *6
            self.stress -= timespec*6
              
    def newday(self):
        self.hours = 0
 
 
''' 4. 
    Use numpy to create an array of numbers going from 20 to 100 by increments of .25
    Then, multiply all the values in the array by 4. 
    Then. find the sum of all the values.
'''
numbers = numpy.arange(20,100,0.25)
nsum = 0
for n in numbers:
    n *= 4
    nsum += n

print(nsum)
 
 
''' 5.
    Use turtle to draw a star.
'''
color('orange', 'green')
begin_fill()
left(60)
forward(100)
right(120)
forward(100)
right(150)
forward(120)
right(150)
forward(100)
right(150)
forward(120)
end_fill()
done()
 
 
 
''' 6.
    Use SymPy to determine the area of a triangle given points a, b and c.
'''
a = (0,0)
b = (0,12)
c = (3,0)

t = Triangle(a,b,c)
print(abs(t.area))
 
 
 
 
''' 7. 
    Use VPython to build a 3D snowman.
'''
 
 
 
 
''' Sources:
    https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html
    https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.arange.html
    https://docs.sympy.org/latest/modules/geometry/index.html
    https://docs.python.org/3/library/turtle.html
'''