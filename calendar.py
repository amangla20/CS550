# introduction
print("Welcome! Enter the date you wish to know more about.")
# this code allows user to input month's name instead of number (they can do number too)
m = input("Enter the month: ")
if (m=="January"):
	m = 1
elif (m == "February"):
	m = 2
elif (m == "March"):
	m = 3
elif (m == "April"):
	m = 4
elif (m == "May"):
	m = 5
elif (m == "June"):
	m = 6
elif (m == "July"):
	m = 7
elif (m=="August"):
	m = 8
elif (m=="September"):
	m = 9
elif (m == "October"):
	m = 10
elif (m == "November"):
	m = 11
elif (m == "December"):
	m = 12

# input date and year
d = input("Enter the date: ")
y = input("Enter the year: ")

# Gregorian calendar calculation
y0  =  int(y) - int((14  -  int(m))/12)  
x =  (int(y0))  +  (int(y0)/4)  -  (int(y0)/100)  +  (int(y0)/400) 
m0  =  int(m)  +  12*(int((14  -  int(m))/12))  -  2  
d0  =  int((int(d) +  int(x)  +  (31*int(m0))/12)) % 7 

# if-statement that controls the result of which day of the week
if (d0 == 0):
	print("The date fell on a Sunday!")
elif (d0 == 1):
	print("The date fell on a Monday!")
elif (d0 == 2):
	print("The date fell on a Tuesday!")
elif (d0 == 3):
	print("The date fell on a Wednesday!")
elif (d0 == 4):
	print("The date fell on a Thursday!")
elif (d0 == 5):
	print("The date fell on a Friday!")
elif (d0 == 6):
	print("The date fell on a Saturday!")
