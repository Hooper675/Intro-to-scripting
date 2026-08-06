# Student name : David An Tran
# Course IT-140 Intro to Scripting
# Assignment Project Two - Text Based Game (TextGameStoryboard.py)

import random

def game_instructions():
    print(" The play will need to collect six items to defeat the demon king")
    print("or be defeated. The world future is in your hands")
    print("Move commands: move East, move West, move North, move South")
    print(" To collect the items: pickup ' item name'. item is currently 0")

floor_layout = {
    "Living room":{"East":"Mess Hall"},
    "Mess Hall":{"West":"Living room", "North":"Armory", "South":"Basement", "East":"Pond",
                 "item":"Holy Water"},
    "Armory":{"South":"Mess Hall","East":"Shrine","item":"Sword"},
    "Shrine":{"West":"Armory","item":"Armor"},
    "Basement":{"North":"Mess Hall","East":"Library","item":"Medical Kit"},
    "Library":{"West":"Basement","item":"Sutra Book"},
    "Pond":{"East":"Great Hall","West":"Mess Hall","item": "Lotus"},
    "Great Hall": {"West":"Pond", "Villain":"Demon King"}
}
# Set place-holders for the variables inventory and counter. So each time the player picks up an item
# The program will count how many times or items the player pick up. It will also remove the item from the room
# using the pop() method.
current_location = "Living room"
inventory = []
counter = 0
# Display the status of the inventory, player's location, and an item if detected
def status():
    print("----------------------------------------")
    print("Current location: ", current_location)
    print("Inventory: ", inventory)
    if "item" in floor_layout[current_location]:
        print(f"Item is detected: {floor_layout[current_location]['item']}")
    print("----------------------------------------")
# Define the location and the player's move
def get_current_location(starting_location, move ):
    newlocation = starting_location
    # loop through each key and value
    for location, player_move in floor_layout.items():
        if location == starting_location and move in player_move:
            newlocation = player_move[move]
    return newlocation

# Main function of the game where it will call on the function above to make the game work
# This gives the player the flexibility

def main():
    global current_location
    global inventory
    global counter
    game_instructions()
    while counter < 6:
        #Define the user action with if-else statement. The player can freely
        #choose what their next action would be
        status()
        prompt_player = input("Make your move: ")
        if prompt_player.startswith("move"):
            direction = prompt_player.replace("move","").strip().title()
            # Move using dictionary look up
            target_location = get_current_location(current_location, direction)
            if target_location != current_location:
                current_location = target_location
                # Check if player stumbled into the Villain's room early!
                if "Villain" in floor_layout[current_location]:
                    print("\nNOM NOM... GAME OVER!")
                    print("You confronted the Demon King without all 6 items!")
                    print("Thanks for playing the game. Hope you enjoyed it.")
                    return  # Ends main() early
            else:
                print("You can't move that way")
        # Here, we will give the player the power to pick up or detect an item
        elif prompt_player.startswith("pickup"):
            requested_item = prompt_player.replace("pickup","").strip().title()
            # Check if each room has the item
            if ( "item" in floor_layout[current_location]
                 and requested_item == floor_layout[current_location]["item"]
                 and requested_item not in inventory ):
                 inventory.append(requested_item)
                 counter += 1
                 floor_layout[current_location].pop("item")
                 print(f"You collected: {requested_item}")
            else:
                print("You already collected this item or There is no item to collect here")

        # This part of the program will output errors when player chooses
        # an action that's not available for them
        else:
            print("Invalid command!Use 'move[direction]' or 'pickup[item]'")

    # Ready to battle the final boss. Check if the player moves East
    # If yes, the player will be prepared before the battle begins.
    # If the player enters anything other than East, the player will be prompted
    # to move east. Once they collected all 6 items, the game becomes more restrictive.
    print("You have collected all 6 items and are ready for battle!")
    print("Move East to enter the Great Hall and confront the Demon King")
    prompt_player = input("Make your move: ")
    if prompt_player.startswith("move") and current_location == "Pond":
        direction = prompt_player.replace("move","").strip().title()
        if direction == "East":
            current_location = get_current_location(current_location, direction)
            status()
            print("Battle begins! Enter a number between 1 and 13")
            number_guess = input("Enter a number: ")
            if number_guess.isdigit():
                number_guess = int(number_guess)
                random_number = random.randint(1, 13)
                if number_guess == random_number:
                    print("You have defeated the Demon King!")
                elif number_guess < random_number:
                    print("You inflict low damage on the Demon King! ")
                else:
                    print("You are exhausted!You need more energy")
            else:
                print("Invalid input. Please enter a number:")
        else:
            print("you must move East to confront the Demon king")
    else:
        print("Demon King hurts you.")

if __name__ == "__main__":
    main()





















