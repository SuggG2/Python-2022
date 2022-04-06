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
exit = Room("The exit. When you have gathered all the notes you may leave.")
current_room = office

###################
#DEFINE CONNECTIONS
###################
office.west = west_hall
office.east = east_hall
west_hall.west = Supply_closet
west_hall.north = dining_areaW
east_hall.north = dining_areaE
dining_areaE.north = show_stageE
dining_areaW.north = show_stageW
dining_areaW.west = back_stage
dining_areaE.east = restrooms
dining_areaE.west = dining_areaW
show_stageE.west = show_stageW

###################
#DEFINE ITEMS
###################
Item.description = ""

torch = Item("torch", "flashlight")
torch.description = "a pale grey torch that lights up rooms to help you find hidden items"

blue_note = Item("A blue note", "blue note")
blue_note.description = "you look at the blue note. It reads: "

red_note = Item("A red note", "red note")
red_note.description = "you look at the red note. It reads: "

yellow_note = Item("A yellow note", "yellow note")
yellow_note.description = "you look at the yellow note. It reads: "

green_note = Item("A green note", "green note")
green_note.description = "you look at the green note. It reads: "

maroon_note = Item("A maroon note", "maroon note")
maroon_note.description = "you look at the maroon note. It reads: "
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
#OBJECTIVES
###################
maroon_note_got = False
yellow_note_got = False
green_note_got = False
red_note_got = False
blue_note_got = False

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
	global maroon_note_got
	global yellow_note_got 
	global green_note_got
	global red_note_got 
	global blue_note_got
	if item in current_room.items:
		t = current_room.items.take(item)
		player_inv.add(t)
		print(f"you pick up the {item}")
	elif item in player_inv and current_room == Supply_closet and t == maroon_note:
		maroon_note_got = True 
	elif item in player_inv and current_room == show_stageE and t == red_note:
		red_note_got = True 
	elif item in player_inv and current_room == dining_areaW and t == yellow_note:
		yellow_note_got = True 
	elif item in player_inv and current_room == back_stage and t == blue_note:
		blue_note_got = True 
	elif item in player_inv and current_room == restrooms and t == green_note:
		green_note_got = True 
	else:
		print(f"You dont see a {item}")
@when("inventory")
@when("show inventory")
@when("what is in my pocket")
def inventory():
	print("You are carrying")
	for item in player_inv:
		print(item)
@when("look at ITEM")
def look_at(item):
	if item in player_inv:
		t - inventory.find(item)
		print(t.description)
	else:
		print(f"you arent carrying a {item}")
@when("use ITEM")
def use(item):
	if item in player_inv and current_room == "show_stageW" and item == "torch":
		print("")

###################
#MAIN FUNCTION
###################

def main():
	print(current_room)
	start()

main()
