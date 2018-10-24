# Anjali Mangla
# 09/14/2018
import sys
import math

# first number is t, then P, and then r

t = sys.argv[1]
p = sys.argv[2]
r = sys.argv[3]

interest = float(p) * math.e**(float(r) * float(t))

print("In " + str(t) + " years, you will have " + str(interest) + " dollars.")