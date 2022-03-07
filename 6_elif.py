"""
#1
user_ice = int(input("How many ice creams would you like\n"))
if user_ice <= 20:
	print("We will have those ready in no time")
else:
	print("we dont have that many in stock sorry")
#2
travel = int(input("How far do you intend to travel(as a number)?\n"))
if travel >= 200:
	print("Remember to fill up your gas")
else:
	print("Have fun")
#3
age = int(input("What is your age?\n"))
if age >= 18:
	print("You are an adult")
else:
	print("You are a minor")

#4
fav_mov = input("What is your favourite movie?\n").lower()
if fav_mov == "lord of the rings":
	print("Ok loser")
else:
	print("Ok")
"""
#5
nerd = input("Have you heard of Darth Plageuis?\n")
if nerd == ""