###################
#IMPORTS
###################
from adventurelib import*

Room.items = Bag()
###################
#DEFINE ROOMS
###################

office = Room("You are in a small office. There are hallways to your west and to you east.")
dining_areaW = Room("You are in the west half of the dining room. It is eerily empty. The back stage is the west. You see the show stage north. The west hall is to the south. You see a small room in the corner you can easily access")
dining_areaE = Room("You are in the east side of the dining area. It, like the west half, is very empty. You see the faint green glow of the restrooms sign to your east and the stage to the north. The east hall is to the south")
restrooms = Room("You are in the restroom. They have clearly not benn cleaned in a while, the stench is overwhelming. There is an old battered box labeled cleaning suppplies in the south westcorner")
show_stageE = Room("You are on the East show Stage. The West dining hall is to the south and the East show stage is to the east")
show_stageW = Room("You are on the show West Stage. The east dining hall is to the south and the west show stage is to the west")
Supply_closet = Room("You are in the supply closet")
west_hall = Room("You are in the west hall. The office is to the east and the supply closet is to the west. You see the dining area ahead to the north")
east_hall = Room("You are in the west hall. The office is to the west. You see the dining area ahead to the north")
back_stage = Room("You are on the show Stage. There are old beaten boxes, chairs, tables and food boxes piled up in the west and east corners of the room.")


###################
#DEFINE CONNECTIONS
###################
office.west = west_hall
office.east = east_hall
west_hall.west = Supply_closet
west_hall.north = dining_areaW
east_hall.north = dining_areaE
dining_areaE.north = show_stage
dining_areaW.north = show_stageW
dining_areaW.west = back_stage
dining_areaE.east = restrooms

###################
#DEFINE ITEMS
###################
Item.description = ""

torch = Item("torch")
torch.description = "a pale grey torch that lights up rooms to help you find hidden items"

note = Item("A scribbled note","note","paper","code")
note.description = "you look at the note. The number word  is scribbled on it"
###################
#DEFINE BAGS
###################
player_inv = Bag()

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
