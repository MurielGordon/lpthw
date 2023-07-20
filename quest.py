from sys import exit

# more hello stuff

def start():
    print("""You walk through a lush green forest at twilight. It's getting dark and you know you're far from home.
You find that the path in front of you has come to a fork. 
Do you take the left fork or the right fork?""")

    choice = input("> ")

    if "left" in choice:
        pool()
    elif "right" in choice:
        deeper_forest()
    else:
        import time
        time.sleep(1.8)
        print("\nYou choose neither left nor right. You stand in the same place until you waste away.")
        dead("You have learned a valuable lesson about following directions.")


def deeper_forest():
    import time
    time.sleep(1.8)
    print("\nYou take the right fork. It is growing darker by the minute, but you keep walking farther into the forest.")
    print("You notice a smaller trail branching off the main trail.")
    print("Do you take the side path or do you stick to the main trail?")

    choice = input("> ")

    if "side" in choice:
        manticore_death()
    if "main" in choice:
        cave_entrance()


def pool():
    import time
    time.sleep(1.8)
    print("\nYou take the left fork. After you walk a while you come across a deep, clear pool of water.")
    print("You think you see something glittering at the bottom of the pool.")
    print("Do you jump in or walk around it?")

    choice = input("> ")

    if "jump" in choice:
        fish_death()
    else:
        cave_entrance()


def cave_entrance():
    import time
    time.sleep(1.8)
    print('\nYou decide "no detours" and continue along the trail.')
    print("It is nearly fully dark now. You come to the entrance of a cave. It is set into the side of a mountain.")
    print("There is an old torch in a rusted bracket bolted to the mountain face by the cave entrance.")
    print("What shall you do next?")
    print("Do you go in or stay out?")

    choice = input("> ")

    if choice == "go in":
        cave_door()
    else:
        warg_death()


def cave_door():
    import time
    time.sleep(1.8)
    print("\nYou grab the old torch and you light it with your flint and steel.")
    print("It flares to life, casting flickering shadows on the rock face before you.")
    print("It does nothing to illuminate the stygian blackness of the cave.")
    print("You walk in.")
    import time
    time.sleep(10)
    print("\n\n\nYou walk until you come across a door. It has a knocker on it.")
    print("Do you knock on the door or do you walk past it?")

    choice = input("> ")

    if "knock" in choice:
        wraith()
    else:
        crystal_cavern()


def wraith():
    import time
    time.sleep(1.8)
    print("\nYou knock on the door.")
    print("It creaks open.")
    print("A wraith emerges.")
    print("Do you fight the wraith or flee?")

    choice = input("> ")

    if "fight" in choice:
        wraith_death()
    else:
        crystal_cavern()


def crystal_cavern():
    import time
    time.sleep(1.8)
    print("\nYou are no fool, you make haste and flee deeper into the cave.")
    print("You hear the sound of water dripping in a vast cavern up ahead.")
    print("You round a bend and a sight of unimaginable beauty greets you -")
    import time
    time.sleep(8)
    print("\n\n\nA cavern, large and wide and filled with brilliant red crystals, some taller than you are.")
    print("You pause for a moment, taking it in.")
    print("You know you can't linger here, but you feel compelled to take a crystal with you.")
    print("Do you take a crystal? Yes or no?")

    choice = input("> ")

    if "yes" in choice:
        yes_crystal()
    elif "not" in choice:
        no_crystal()
    else:
        no_crystal()


def no_crystal():
    import time
    time.sleep(1.8)
    print("\nYou leave the crystals be and continue through the cave.")
    print("At the end of the cavern you find a narrow hole, just wide enough for you to squeeze through.")
    print("A sulferous smell wafts through the hole. It is your only way through.")
    import time
    time.sleep(12)
    print("\n\n\nYou squeeze through the hole and find yourself in an even larger cavern.")
    print("This one houses an enormous pile of gold and jewels, antique armor and other finery.")
    print("A loud voice cuts through the stillness, startling you -")
    dragon_speaks_no_crystal()


def dragon_speaks_no_crystal():
    import time
    time.sleep(12)
    print('\n\n\n"WHAT HAVE YOU TO SHOW ME OF WHAT LIES BEYOND MY CAVERN?" the voice bellows.')
    print('"THE PLACE YOU CAME FROM I CANNOT GO. I AM TOO LARGE. WHAT IS THERE IN THAT PLACE?"')
    print("How will you convey what you have seen to this dragon?")
    print("Will you use words or pantomine?")

    choice = input("> ")
    if "words" in choice:
        import time
        time.sleep(1.8)
        print("\nYou begin to tell the dragon about the wonderful cavern you just left.")
        dragon_death()
    else:
        import time
        time.sleep(1.8)
        print('\nYou lift your arms and struggle to find a way to say "crystal" using just your hands.')
        dragon_death()


def yes_crystal():
    import time
    time.sleep(1.8)
    print("\nYou break off one of the crystals and slip it into your pocket.")
    print("At the end of the cavern you find a narrow hole, just wide enough for you to squeeze through.")
    print("A sulferous smell wafts through the hole. It is your only way through.")
    import time
    time.sleep(12)
    print("\n\n\nYou squeeze through the hole and find yourself in an even larger cavern.")
    print("This one houses an enormous pile of gold and jewels, antique armor and other finery.")
    print("A loud voice cuts through the stillness, startling you -")
    dragon_speaks_yes_crystal()


def dragon_speaks_yes_crystal():
    import time
    time.sleep(12)
    print('\n\n\n"WHAT HAVE YOU TO SHOW ME OF WHAT LIES BEYOND MY CAVERN?" the voice bellows.')
    print('"THE PLACE YOU CAME FROM I CANNOT GO. I AM TOO LARGE. WHAT IS THERE IN THAT PLACE?"')
    print("How will you convey what you have seen to this dragon?")
    print("Will you show the dragon or tell the dragon?")

    choice = input("> ")
    if "show" in choice:
        dragon_bribe()
    else:
        print("\nYou begin to tell the dragon about the wonderful cavern you just left.")
        dragon_death()


def dragon_bribe():
    import time
    time.sleep(1.8)
    print("\nFrom out of your pocket you draw the crystal you took from the cystal cavern.")
    print("You hold it aloft. It catches the light and sparkles like captured flame.")
    print('"AH, I SEE. IT IS A CAVERN OF CRYSTAL. NOW I KNOW WHAT THE MYSTERIOUS CAVERN CONTAINS," the dragon says.')
    print('"THIS TRINKET PLEASES ME. THIS I CAN ADD TO MY HOARDE."')
    print('"YOU WILL GIVE THAT TO ME AND I WILL ALLOW YOU TO PASS THROUGH MY CAVE UNHARMED."')
    
    import time
    time.sleep(12)
    cave_travel()


def cave_travel():
    import time
    time.sleep(1.8)
    print("\n\n\nYou pass through the dragon's cave and find yourself in a narrow passage.")
    print("The passage winds left, right, right, then left again.")
    print("You begin to see signs of mining work. A cart track appears,")
    print("then a mine cart, sitting alone on the tracks, half filled with ore.")
    import time
    time.sleep(10)
    print("\n\n\nYou walk further along the tunnel, seeing picks, axes, half-burnt torches, and other signs.")
    print("You come to a door next to which are hung helmets, more tools, and surplus torches.")
    print("Light seeps out from beneath the door.")
    print("You open it.")
    
    import time
    time.sleep(10)
    dwarven_tavern()


def dwarven_tavern():
    import time
    time.sleep(1.8)
    print("\n\n\nAs soon as you open the door you are greeted by a wall of noise.")
    print("The room is filled with dwarves enjoying pints of ale after a long day in the mine.")
    print("They are making jokes and laughing, singing songs and having drinking contests.")
    print("Should you keep to yourself or buy everyone a round?")

    choice = input("> ")
    if "keep" in choice:
        import time
        time.sleep(1.8)
        print("\nYou decide to keep to yourself.")
        get_too_drunk()
    elif "yourself" in choice:
        import time
        time.sleep(1.8)
        print("\nYou decide to keep to yourself.")
        get_too_drunk()
    else:
        dwarf_talk()


def dwarf_talk():
    import time
    time.sleep(1.8)
    print("\nYou buy everyone a round. They cheer and the largest group welcomes you to join them.")
    print("The dwarves are friendly and you have a great evening.")
    print("Talk turns to your quest, and the dwarves learn that you are looking for a way out of the cave.")
    print("They tell you they will show you a way out, on one condition:")
    import time
    time.sleep(10)
    print("\n\n\nYou will come back and visit them sometime.")
    import time
    time.sleep(4)
    print("\n\n\nDo you agree and take their way out or do you go your own way?")

    choice = input("> ")
    if "agree" in choice:
        mine_cart()
    elif "take" in choice:
        mine_cart()
    else:
        import time
        time.sleep(1.8)
        print("\nYou decide to take your own path out of the cave.")
        print("The dwarves are insulted and you start to drink to cover up the awkwardness.")
        get_too_drunk()
        import time
        time.sleep(4)


def get_too_drunk():
    import time
    time.sleep(3)
    print("\nYou down more and more pints of ale until you become very drunk.")
    print("The tavern begins to empty out as dwarves go back to their homes for the night.")
    print("You find yourself in an empty tavern, with the barkeep wiping down tables and putting away glasses.")
    print("Do you go find a way out of the cave tonight or do you sleep it off?")

    choice = input("> ")
    if "sleep" in choice:
        sleep_it_off()
    else:
        import time
        time.sleep(1.8)
        print("\nYou decide to go find a way out tonight.")
        print("You stumble out of the tavern and into the passage you came through.")
        print("You turn down a new passage, too drunk to read the warning signs posted.")
        import time
        time.sleep(8)
        mine_shaft_death()


def sleep_it_off():
    import time
    time.sleep(1.8)
    print("\nYou decide to sleep it off. Exploration can wait until the morning.")

    import time
    time.sleep(4)
    print("\nZzzz")
    import time
    time.sleep(2)
    print("\nZzzz")
    import time
    time.sleep(2)
    print("\nZzzz")
    import time
    time.sleep(2)

    print("\n\n\nYou wake the next day feeling terrible.")
    print("You get up and start on your way.")
    print("You come to a forked passage.")
    print("One smells nice and fresh, but the other appears to have light at the end of it.")
    print("Do you follow your nose or follow your eyes?")

    choice = input("> ")
    if "nose" in choice:
        import time
        time.sleep(1.8)
        print("\nYou decide to follow your nose.")
        import time
        time.sleep(2)
        exit_cave()
    else:
        import time
        time.sleep(1.8)
        print("\nYou decide to follow your eyes.")
        import time
        time.sleep(3)
        print("You walk toward the light, it gets brigther and brighter.")
        print("As you get closer to the light it begins to look strange.")
        print("You get closer and notice the light is flickering, like a lantern.")
        print('A voice cackles "Things are not always what they seem!" and a laugh fills the tunnel.')
        import time
        time.sleep(12)
        mine_shaft_death()


def mine_cart():
    import time
    time.sleep(1.8)
    print("\nYou agree to take the dwarves' way out of the cave.")
    print("You drink for a few more hours, then the dwarves say it's time to go.")
    print("They want to go with you, they say they like taking this route while in their cups.")
    import time
    time.sleep(10)
    print("\n\n\nThey take you to a mine cart at the top of an incline. They tell you to get in it.")
    print("You get in, and the others take up positions on both sides of the cart.")
    print('Together they yell "One! Two! Three!" and on three they begin running full tilt,')
    print("pushing the cart along as they run.")
    import time
    time.sleep(16)
    print("\n\n\nOne by one they hop in with you, and the cart hurtles along the track.")
    print("It twists and turns at terrifying speed. The dwarves shout excitedly.")
    print("Then the cart begins to slow, and one of the dwarves employs the hand brake.")
    print("You slow to a stop and the dwarves get out.")
    print("They point you down a passage and then they leave,")
    print("clapping you on the back one last time in goodbye.")
    import time
    time.sleep(18)
    exit_cave()


def exit_cave():
    import time
    time.sleep(1)
    print("\n\n\nYou follow the passage, noting how sweet and clean the air smells.")
    print("The smell of vegetation and fresh air grows stronger, and the passage grows brighter.")
    print("You find a cave exit, and you walk out to find yourself under the open sky.")
    import time
    time.sleep(10)
    print("\n\n\nYou laugh with relief. You made it!")
    print("You are none the richer in worldly goods,") 
    print("but you've gained memories to last a lifetime.")
    print("THE END.")
    exit(0)

# _______________________________________________________________________________________________
# the main death exit

def dead(why):
    print(why, "\nYou have died. So ends the quest of another traveler.")
    print("\nTHE END.\n")
    exit(0)

# _______________________________________________________________________________________________
# the ways you can die

def fish_death():
    import time
    time.sleep(1.8)
    print("\nYou have chosen the pool. You jump in and begin to swim to the bottom.") 
    print("It is deeper than it looks, but you keep swimming, undeterred.")
    print("You reach your hand out to grasp the sparkling thing at the bottom of the pool. It's a golden crown with jewels.")
    import time
    time.sleep(9)
    print("\nSuddenly, the faint light from above you grows dim. You are in the shadow of a huge fish.")
    dead("The fish eats you, and you join the crown at the bottom of the pool.")

def manticore_death():
    import time
    time.sleep(1.8)
    print("\nYou start down the side path.")
    import time
    time.sleep(3)
    print("\n\nYou hear a sound behind you. Hooves thudding on the forest floor.")
    dead("A manticore has found you. It leaps onto your back and tears your throat out.")

def warg_death():
    import time
    time.sleep(1.8)
    print("\nYou shudder and look away from the cave entrance. Something about it doesn't feel right.")
    print("You decide to make camp in a thicket 40 paces from the cave entrance.")
    print("You light a feeble fire to keep away the cold and damp and settle down to rest for the night.")
    import time
    time.sleep(10)
    print("\n\nAs you sleep, a warg comes upon your slumbering body.")
    dead("She eats you, and you haunt the forest near the cave forever.")

def wraith_death():
    import time
    time.sleep(1.8)
    print("\nYou decide to fight the wraith.")
    print("You unsheathe your knife, but you are a littly rusty with it.")
    print("You are no match for the wraith. It runs a silvery ghost sword through your belly.")
    dead("The cave now has another ghostly resident.")

def dragon_death():
    import time
    time.sleep(4)
    print("\nThe dragon interrupts you:")
    import time
    time.sleep(4)
    print('\n\n\n"YOUR PATHETIC ATTEMPTS AT COMMUNICATION DO NOT PLEASE ME!" the dragon bellows.')
    print('"WHAT GOOD TO ME ARE THESE FEEBLE GESTURES? I CANNOT ADD THEM TO MY HOARDE."')
    dead("The dragon lets loose a torrent of fire from its mouth, burning you to a crisp.")

def mine_shaft_death():
    dead("\nYou take another step when suddenly the ground opens up beneath you and you find yourself plummeting down a mine shaft.")



start()