#1
money = 200
hat = 20
top = 30
pants = 15
belt = 60
shoes = 40
#2
print("You have", money,"dollars")
#3
print("Buying a hat")
#4
money -= hat
#5 and 6
print(f"You now have {money} left")
#7
print("Buying a top")
money -= top
print(f"You now have {money} left")

print("Buying pants")
money -= pants
print(f"You now have {money} left")

print("Buying a belt")
money -= belt
print(f"You now have {money} left")

print("Buying shoes")
money -= shoes
print(f"You now have {money} left")