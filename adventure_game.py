import random
import time
import sys
items = []
enemies = ["Pirate", "Oldman", "Zombie"]
gender = ["male", "female"]
tops = ["red shirt", "nothing", "crop white shirt"]
unders = ["jeans", "nothing", "shorts"]
# varaibles for places
b = "beach"
g = "graveyard"
t = "temple"
o = "oldhouse"


# prints a message and sleeps for 2 seconds
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# intro
def intro():
    print_pause("You wake up finding yourself in front three ways with names"
                " of places on")
    print_pause("You are a " + random.choice(gender) + ".\n" +
                "you wear " + random.choice(tops) +
                " and " + random.choice(unders) + ".")
    print_pause("You find a shotgun and knife and some grenades with you")
    print_pause("Maybe you will use them")
    print_pause("you read signs beach , graveyard , temple , oldhouse")


# where to go
def place_go():
    print_pause("You can go to the beach , the graveyard , the temple or "
                "the oldhouse")
    where = input("Where do yo want to go now ?")
    if o in where.lower()and t and b and g not in where.lower():
        if "coin" in items:
            print_pause("You have already killed the Oldman and there is"
                        " nothing to do here")
            place_go()
        else:
            oldhouse_go()
    if g in where.lower() and o and b and t not in where.lower():
        if "skin" in items:
            print_pause("You have already killed the Zombie and there is"
                        " nothing to do here")
            place_go()
        else:
            graveyard_go()
    if b in where.lower() and t and o and g not in where.lower():
        if "necklace" in items:
            print_pause("You have already killed the Pirate and there is"
                        " nothing to do here")
            place_go()
        else:
            beach_go()
    if t in where.lower() and o and b and g not in where.lower():
        if len(items) == 3:
            temple_go2()
        elif len(items) < 3:
            temple_go1()
    if o and b and g and t not in where.lower():
        print_pause("There is no place with that name , you have to choose one"
                    " of the places mentioned below")
        place_go()


# You go to the beach
def beach_go():
    if "Pirate" in enemies:
        print_pause("You go to the beach")
        print_pause("Suddenly you see a pirate in front of you!")
        print_pause("The pirate takes his sword and attacks you")

        def weapon_call():
            enemy_choice = input("Enter attack if you want to attack\n"
                                 "Enter escape if you want to escape")
            if enemy_choice == "":
                weapon_call()
            else:
                if enemy_choice == "attack":
                    print_pause("You can attack with a shotgun or a knife"
                                " or grenades")
                    weapon = input("which weapon do you attack with ?")
                    if "shotgun" in weapon.lower():
                        print_pause("You hit the pirate with your shotgun !")
                        print_pause("Well done, you killed the pirate")
                        enemies.remove("Pirate")
                        print_pause("You get the golden necklace")
                        items.append("necklace")
                        place_go()
                    else:
                        print_pause("You attack with " + weapon +
                                    " and it seems that you did not harm him")
                        print_pause("You are dead!")
                        the_end()
                else:
                    print_pause("You escape and go the place where were"
                                " you at first")
                    place_go()
        weapon_call()
    else:
        print_pause("There is nothing to do here , "
                    "you go back to the first place")
        place_go()


# you go to the old house
def oldhouse_go():
    if "Oldman" in enemies:
        print_pause("You go to the oldhouse")
        print_pause("You see an oldman sitting in front of a window")
        print_pause("He stand and looks at you")
        print_pause("He grabs his shovel and hits you hard")
        print_pause("What do you want to do ?")

        def weapon_call():
            enemy_choice = input("Enter attack if you want to attack\n"
                                 "Enter escape if you want to escape")
            if enemy_choice == "":
                weapon_call()
            else:
                if enemy_choice == "attack":
                    print_pause("You can attack with a shotgun or a"
                                " knife or grenades")
                    weapon = input("which weapon do you attack with ?")
                    if "knife" in weapon.lower():
                        print_pause("You attack with your " + weapon + "!")
                        print_pause("You cut his throat")
                        print_pause("Great job, you killed the oldman")
                        enemies.remove("Oldman")
                        print_pause("You get the coin")
                        items.append("coin")
                        place_go()
                    else:
                        print_pause("You attack with " + weapon +
                                    " and it seems that you did not harm him")
                        print_pause("You are dead!")
                        the_end()
                else:
                    print_pause("You escape and go the place where "
                                "were you at first")
                    place_go()
        weapon_call()
    else:
        print_pause("There is nothing to do here , "
                    "you go back to the first place")
        place_go()


def graveyard_go():
    if "Zombie" in enemies:
        print_pause("You go to the graveyard")
        print_pause("You walk slowly")
        print_pause("It is almost dark, and you hear nothing")
        print_pause("At once, you find a hand appears under")
        print_pause("Uh , it is a zombie")
        print_pause("He gets out of the ground and starts running towards you")

        def weapon_call():
            enemy_choice = input("Enter attack if you want to attack\n"
                                 "Enter escape if you want to escape")
            if enemy_choice == "":
                weapon_call()
            else:
                if enemy_choice == "attack":
                    print_pause("You can attack with a shotgun or "
                                "a knife or grenades")
                    weapon = input("which weapon do you attack with ?")
                    if "grenade" in weapon.lower():
                        print_pause("You through a grenade and "
                                    "it explodes and kills the zombie")
                        print_pause("Well done, you killed the zombie")
                        enemies.remove("Zombie")
                        print_pause("You get the coin")
                        items.append("skin")
                        place_go()
                    else:
                        print_pause("You attack with a grenade and "
                                    "it seems that you did not harm him")
                        print_pause("You are dead!")
                        the_end()
                else:
                    print_pause("You escape and go the place "
                                "where were you at first")
                    place_go()
        weapon_call()
    else:
        print_pause("There is nothing to do here , "
                    "you go back to the first place")
        place_go()


# The temple at the first time
def temple_go1():
    print_pause("You get inside the temple")
    print_pause("you find a huge door with a sign")
    print_pause("You read the sign")
    print_pause("You need to find a necklace and a piece of skin and a coin"
                " to enter")
    place_go()


# The temple at the end
def temple_go2():
    print_pause("You enter the temple with the three items")
    print_pause("you put them in the door")
    print_pause("A huge earthquake hits the ground and the door opens")
    print_pause("You see a huge throne with a man above")
    print_pause("He seems like the king")
    print_pause("He tells you are the chosen heir of the throne")
    print_pause("and that you are the first to complete the maze")
    print_pause("Congrats you won the game and became the king")
    the_end()
# The end of The game


def the_end():
    print_pause("GAME END")
    game_end = input("Do you want to play again ?")
    if "yes" in game_end.lower():
        play_game()
    elif "no" in game_end.lower():
        sys.exit()
    else:
        print_pause("That is not a right input .")
        the_end()


def play_game():
    intro()
    place_go()


play_game()
