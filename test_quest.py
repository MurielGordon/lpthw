from sys import exit

def dwarven_tavern():
    print("\nAs soon as you open the door you are greeted by a wall of noise.")
    print("The room is filled with dwarves enjoying pints of ale after a long day in the mine.")
    print("They are making jokes and laughing, singing songs and having drinking contests.")
    print("Should you keep to yourself or buy everyone a round?")

    choice = input("> ")
    if "keep" in choice:
        print("\nYou decide to keep to yourself.")
        get_too_drunk()
    elif "yourself" in choice:
        print("\nYou decide to keep to yourself.")
        get_too_drunk()
    else:
        dwarf_talk()

def dwarf_talk():
    print("\nYou buy everyone a round. They cheer and the largest group welcomes you to join them.")
    print("The dwarves are friendly and fun, and you have a great evening.")
    print("Talk turns to your quest, and the dwarves learn that you are looking for a way out of the cave.")
    print("They tell you they will show you a way out, on one condition:")
    print("You will come back and visit them sometime.")
    print("\n")
    print("Do you agree and take their way out or do you go your own way?")

    choice = input("> ")
    if "agree" or "take" in choice:
        mine_cart()
    else:
        print("\nYou decide to take your own path out of the cave.")
        print("The dwarves are insulted and you start to drink to cover up the awkwardness.")
        get_too_drunk()


def get_too_drunk():
    print("\nYou down more and more pints of ale until you become very drunk.")
    print("The tavern begins to empty out as dwarves go back to their homes for the night.")
    print("You find yourself in an empty tavern, with the barkeep wiping down tables and putting away glasses.")
    print("Do you go find a way out of the cave tonight or do you sleep it off?")

    choice = input("> ")
    if "sleep" in choice:
        sleep_it_off()
    else:
        print("\nYou decide to go find a way out tonight.")
        print("You stumble out of the tavern and into the passage you came through.")
        print("You turn down a new passage, too drunk to read the warning signs posted.")
        mine_shaft_death()


dwarven_tavern()