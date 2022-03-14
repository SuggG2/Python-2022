#import all the functions from adventurelib
from adventurelib import *

#rooms
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


#EVERYTHING GOES ABOVE HERE - DO NOT CHANGE
#ANYTHING BELOW THIS LINE
#the main function
def main():
	print(current_room)
	start()
	#start the main loop

main()