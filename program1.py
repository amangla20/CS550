"""
Date Due: 09/10/2018
Description: This code is a conversation between Terminal (a machine) 
and a human. The machine is a little lonely and wishes it could adopt 
human characteristics like emotions and aging. It genuinely cares 
about the human it has the conversation with.
Sources: Class. Also, learned how to multi-line comment from https://www.pythonforbeginners.com/comments/comments-in-python.
"""
print("Hello World!")
username = input("What's your name? ")
print("Nice to meet you, " + username + "!")
age = input("How old are you? ")
print("If I could age, I would be " + age + " years old.")
place = input("Where are you from? ")
print("I've never been to " + place + ". I should visit sometime!")
attribute = input("If you could choose one adjective to describe you, what would it be? ")
print("I can definitely sense that you are a " + attribute + " person.")
subject = input("What's your favorite subject? ")
print("Seriously? " + subject + " is my favorite subject too!")
emotion = input("How are you feeling right now? ")
print("Wow. It must be cool to be able to feel " + emotion + ".")
activity = input("What would you like to do today? ")
print("I love to " + activity + " too!")
print("We actually have so much in common, " + username + ".")
hang = input("Would you like to hang out again like this sometime? ")
if (hang == "yes"):
	print("Yay! So happy to hear that!")
elif (hang == "sure"):
	print("Ok, I'll take that.")
elif (hang == "no"):
	print("Oh, ok. If you really feel that way...")
else:
	print("OK, a " + hang + ". I'll take that. It was nice talking to you!")
