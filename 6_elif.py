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

#5
nerd = input("Have you heard of Darth Plageuis?\n").lower()
if nerd == "no":
	print("Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself. - Sheev Palpatine or Darth Sidious.")
else:
	print("You must be a fan?")
"""
#6
passionofthenerd = input("Who directed Passion of The Christ?").lower()
if passionofthenerd == "mel gibson":
	print(f"Correct {passionofthenerd} directed passion of the christ")
else:
	print("No lol")