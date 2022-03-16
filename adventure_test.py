###################
#IMPORTS
###################
from adventurelib import*

###################
#DEFINE ROOMS
###################

spce = Room("""
	You are drifinting in space. it feels very cold.
	A slate-blue spaceship sits completely)
###################
#DEFINE CONNECTIONS
###################


###################
#DEFINE ITEMS
###################
Item.description = ""

knife = Item("a dirty knife","knife")
knife.description

###################
#DEFINE BAGS
###################


###################
#ADD ITEMS TO BAGS
###################


###################
#DEFINE ANY VARIABLES
###################
 

###################
#BINDS
###################
@when("brush teeth")
def brush_teeth():
	print("You brush your teeth")

###################
#MAIN FUNCTION
###################
def main():
	start()

if __name__ == '__main__':
	main()
