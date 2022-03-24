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
current_room = office

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

blue_note = Item("A scribbled note","note","paper","code")
note.description = "you look at the blue note. "

red_note = Item("A scribbled note","note","paper","code")
note.description = "you look at the red note. "

yellow_note = Item("A scribbled note","note","paper","code")
note.description = "you look at the yellow note. "

green_note = Item("A scribbled note","note","paper","code")
note.description = "you look at the green note. "

maroon_note = Item("A scribbled note","note","paper","code")
note.description = "you look at the maroon note. "
###################
#DEFINE BAGS
###################
player_inv = Bag()

###################
#ADD ITEMS TO BAGS
###################
back_stage.items.add(blue_note)
show_stageE.items.add(red_note)
dining_areaW.items.add(yellow_note)
restrooms.items.add(green_note)
Supply_closet.items.add(maroon_note)
dining_areaE.items.add(torch)

###################
#DEFINE ANY VARIABLES
###################
 

###################
#BINDS
###################
@when("enter west hall")
@when("enter east hall")
def enter_west_hall():
	global current_room
	if current_room is not office:
		say("You cannot enter")
		return
	else:
		current_room = office 
@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)
@when("look")
def look():
	print(current_room)
	print(current_room.exits())
	if len(current_room.items) > 0 :
		print("You see:")
		for item in current_room.items:
			print(item)
@when ("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
###################
#MAIN FUNCTION
###################
def main():
	start()

if __name__ == '__main__':
	main()
