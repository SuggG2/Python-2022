###################
#IMPORTS
###################
from adventurelib import*

###################
#DEFINE ROOMS
###################

office = Room("You are in a small office. There are hallways to your west and to you east.")
dining_areaW = Room("You are in the west half of the dining room. It is eerily empty. The pirate cove is south west and the back stage is the northwest. You see the show stage north. The west hall is to the south")
dining_areaE = Room("You are in the east side of the dining area. It, like the west half, is very empty. You see the faint green glow of the restrooms sign to your east and the stage to the north. The east hall is to the south")
pirate_cove = Room("You are in the pirate cove. There are old chairs and tables piled up in the corner.")
restrooms = Room("You are in the restroom. They have clearly not benn cleaned in a while, the stench is overwhelming. There is an old battered box labeled cleaning suppplies in the south westcorner")
show_stage = Room("You are on the show Stage. The West dining hall is to the south west and the east dining hall to the south east")
Supply_closet = Room("You are in the supply closet")
west_hall = Room("You are in the west hall. The office is to the east and the supply closet is to the west. You see the dining area ahead to the north")
east_hall = Room("You are in the west hall. The office is to the west. You see the dining area ahead to the north")
back_stage = Room("You are on the show Stage. There are old beaten boxes, chairs, tables and food boxes piled up in the west and east corners of the room.")


###################
#DEFINE CONNECTIONS
###################


###################
#DEFINE ITEMS
###################
Item.description = ""

torch = Item("torch")
torch.description

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
