import random 
# Constants 
MISSION_TYPES = ["Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"] 
# Ship systems, resources, and crew 
ship = { 
		"systems": { 
		"shields": 100, 
		"weapons": 100, 
		"engines": 100, 
		"sensors": 100 
		}, 
		"resources": { 
			"energy": 1000, 
			"torpedoes": 10 
		}, 
		"crew": { 
			"Picard": "Command", 
			"Riker": "Command", 
			"Data": "Operations", 
			"Worf": "Operations", 
			"La Forge": "Operations", 
			"Crusher": "Sciences", 
			"Troi": "Sciences" 
		} 
	} 

def main(): 
	print("Welcome to the Star Trek: TNG Mission Simulator!") 
	score = 0 
	turns = 0 

	while True: 
		display_status() 
		action = get_user_action() 

	if action == "1": 
		score += run_mission() 
	elif action == "2": 
		repair_system() 
	elif action == "3": 
		add_crew_member() 
	elif action == "4": 
		print(f"Simulation ended. Final score: {score}") break 
	else: 
		print("Invalid action. Please try again.") 
		
	turns += 1 
	handle_random_event() 

	if turns % 3 == 0: 
		replenish_resources() 

def display_status(): 
# TODO: Implement function to display ship status, resources, and crew 
	while ship !=0 :
		print(ship["system"] ["resources"] ["crew"])
def get_user_action(): 
# TODO: Implement function to get and return user's chosen action 
	global action #get the thing from main (this is just local)
	action = int(input("Choose a number from 1-4 to do an action."))
def run_mission(): 
	mission_type = random.choice(MISSION_TYPES) 
	print(f"\nNew mission: {mission_type}") 
	# TODO: Implement mission logic for different mission types 
	# Return the score earned from the mission 
	match mission_type :
		case "Exploration" :
			ship ["crew"] ["Picard"]
			ship["systems"] ["shields"]
			ship["resources"] ["energy"]
		case "Diplomacy" :
			ship ["crew"] ["Riker"]
			ship["systems"] ["weapons"]
			ship["resources"] ["energy"]
		case "Combat" :
			ship ["crew"] ["Data"]
			ship["systems"] ["engines"]
			ship["resources"] ["energy"]
		case "Rescue" :
			ship ["crew"] ["Worf"] 
			ship["systems"] ["sensors"]
			ship["resources"] ["torpedoes"]
		case "System Research" :
			ship ["crew"] ["Crusher"]
			ship["systems"] ["shields"]
			ship["resources"] ["torpedoes"]									


def repair_system(): 

# TODO: Implement system repair functionality
	2
def add_crew_member(): 
# TODO: Implement functionality to add a new crew member 
	3
def handle_random_event():
# TODO: Implement random events that can occur during the simulation 
	1
def use_resource(resource, amount): 
# TODO: Implement resource usage logic 
	4
def replenish_resources(): 
# TODO: Implement resource replenishment logic 
	1
main()
