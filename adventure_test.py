###################
#IMPORTS
###################
from adventurelib import*

###################
#DEFINE ROOMS
###################

office = Room("You are in a small office. There are hallways to your west and to you east.")
dining_areaW = Room("You are in the west half of the ")
dining_areaE = Room()
pirate_cove = has one note in the south part of the room connected to the west dining area
restrooms = has a note in the south part of the room connected to east dining area
show_stage = split into 2 sides west side has a note east side has an npc
Supply_closet = has a note in the south part of the room connected to the west hall 
west_hall = hallway / room connecting the office, supply closet, and dining area
east_hall = hallway / room connecting the office and dining area and has an npc at the end

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
