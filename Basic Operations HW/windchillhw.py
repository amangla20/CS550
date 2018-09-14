# National Weather Service Calculation
# Anjali Mangla

# Introduction of program
print("What's the wind chill today?")

# user input of temperature and speed
t = input("Enter temperature in Farenheit: ")
v = input("Enter wind speed in mph: ")

# windchill calculation formula
w = 35.74 + 0.6215*float(t) + (0.4275*float(t) - 35.75)*float(v)**0.16

# result
if (float(t) > 50 or float(t) < -50):
	print("Sorry, the formula doesn't work for that temperature.")
elif (float(v) > 120 or float(v) < 3):
	print("Sorry, the formula doesn't work for that speed.")
else:
	print("The estimated wind chill is:",w)




