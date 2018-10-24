# def add(x,y):
# 	return x+y
# print(add(5,6))

# def is_even(n):
# 	if n%2==0:
# 		return True
# 	return False
# def fact(n):
# 	if n == 0 or n == 1:
# 		return 1
# 	return n*fact(n-1)
# ui = int(input("What number would you like to take a factorial of? "))
# print(fact(ui))

def countx(string):
	if len(string) < 1:
		return 0
	if string[0] == "x":
		return 1 + countx(1:)
	return countx(1:)

print(countx("xxixx"))
print(countx("xixixixhx"))

def crazy_eights(number):
	if number is 0:
		return 0
	if number%10 == 8:
		if number%100 == 88:
			return 2 + crazy_eights(number//10)
		return 1 + crazy_eights(number//10)
	return crazy_eights(n//10)

print(crazy_eights(8918228))
print(crazy_eights(88918))

def gcd(a,b):
	if a == 0:
		return b
	if b == 0:
		return a
	if a == 0 and b == 0:
		return 0


