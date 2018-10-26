import random as r
# running balance
# pin number
# unique-ish account number
# open or closed - when closed, money is transferred and you can't use it anymore
# deposit and withdraw
# transfers
# names of account holders
# security questions and answers
# User interaction
# multiple accounts
# receipts
# no printing or requesting input from within the class

class BankAccount:
	def __init__(self, balance, pin):
		self.balance = balance
		self.pin = pin
		self.acc = r.randrange(10000, 100000)
		self.status = accopen # boolean, open or closed open = True closed = False
		# can't take out more money than they have
		balstatus = "Your account currently has a balance of " + str(self.balance) + " dollars."
		return balstatus

	def deposit(self, amount):
		self.balance += amount
		balstatus = "Your account currently has a balance of " + str(self.balance) + " dollars."
		return balstatus

	def withdraw(self, amount):

while True:
	print("Welcome to Bank of Anjali! At this ATM, you can create a bank account.")
	setpin = int(input("What would you like the 4-digit pin number of your account to be? "))
	acc1 = BankAccount(0, setpin)
	dep = input("Would you like to make a deposit to set the beginning balance? Type Y or N. ")
	if dep == "Y":
		deposit = int(input("How much would you like to deposit into your account? "))
		print(acc1.deposit(deposit))
	else:
		print("Ok! Thank you for working with us today!")
		break
	choice = input("Would you like to withdraw or make a deposit? ")



