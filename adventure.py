#import all the functions from adventurelib
from adventurelib import *

#rooms
Room.items = Bag()

space = Room("You are drifting in space. You see a spaceship.")
airlock = Room("You are in an airlock")
cargo = Room("You are in the cargo bay")
docking = Room("You are in the docking bay")
hallway = Room("You are in a hallway with four exits")
bridge = Room("You stand in the bridge if a ship. There is a dead body here")
mess = Room("You are in the kitchen")
quarters = Room("You are in the crew quarters. There is a locker.")
escape = Room("You are in an escape pod")

#room connections
docking.west = cargo
hallway.north = cargo
hallway.east = bridge
hallway.south = mess
hallway.west = airlock
bridge.south = escape
mess.west = quarters
quarters.north = airlock

#items
Item.description = "" #make sure each item has a description
keycard = Item("A red keycard","keycard","card","key","red keycard")
keycard.description = "You look at the keycard and see it is labelled escape pod"

note = Item("A scribbled note","note","paper","code")
note.description = "youu look at the note. The numbers 2,3,5,4 are scribbled on it"

#add items to room
quarters.item.add(note)

#variables
current_room = space

#binds
@when("jump")
def jump():
	print("You jump")


@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_airlock():
	global current_room
	if current_room == space:
		print("You haul yourself into the airlock")
		current_room = airlock 
	else:
		print("there is no airlock here")
	print(current_room)

@when("go DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		#checks if the current room list of exits has the diretion the plater wnats to go
		current_room = current_room.exit(direction)
		print(f"You go {direction}")
		print(current_room)
	else:
		print("You cant go that way")

@when("look")
def look():
	print(current_room)
	print("There are exits to the ",current_room.exits())
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)

#EVERYTHING GOES ABOVE HERE - DO NOT CHANGE
#ANYTHING BELOW THIS LINE
#the main function
def main():
	print(current_room)
	start()
	#start the main loop

main()