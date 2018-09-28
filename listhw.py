# PROBLEM 1
import random
# create empty list called "a"
a = []
# add 10 random numbers to this list
for x in range(10):
	a.append(random.randrange(100))

# reverse the sorting order, so make it from largest to smallest
a.sort(reverse = True)

# if x is divisible by 3, remove it. Go through all the items in this list and check.
for x in a:
	if x%3 == 0:
		a.remove(x)

#print the list!
print(a)

# you could make this more compact by storing random number in another variable making an if statement in the first for loop that only appends the variable if variable%3 != 0, but the instructions said to first generate the 10 item list so I didn't do the short way.

# PROBLEM 2
# List comp.: https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
# Shuffling: https://stackoverflow.com/questions/976882/shuffling-a-list-of-objects
# create list using list comprehension
b = [i for i in range(100)]
# shuffle around the order
random.shuffle(b)
# print the list!
print(b)

# PROBLEM 3
# ask for base
base = int(input("Enter an integer to be the base. "))
# ask for exponent
exponent = int(input("Enter an integer to be the exponent. "))

calc = []
# append the powers
for number in range(exponent + 1):
	calc.append(base**number)
# print list
print(calc)
