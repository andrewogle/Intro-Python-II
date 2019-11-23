import cmd
import textwrap
import sys
import os
import time
import random


from room import Room
from player import Player
from item import Item

### items ###
key = Item('key', 'rusty old key')
dagger = Item('dagger', 'bloody dagger')

# Declare all the rooms

room = {
    'outside':  Room("outside",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [key, dagger]),

    'overlook': Room("overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow passage':   Room("narrow passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure chamber': Room("treasure chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow passage']
room['overlook'].s_to = room['foyer']
room['narrow passage'].w_to = room['foyer']
room['narrow passage'].n_to = room['treasure chamber']
room['treasure chamber'].s_to = room['narrow passage']




#
# Main
#
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() 
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command")
        option = input("> ")
        if option.lower() == ("play"):
            start_game() 
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    title_screen_selections()

def help_menu():
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('- Use up, down, left, right to move')
    print('- Type your commands to do them')
    print('- Use "look" to inspect something')
    title_screen_selections()

def print_location():
    print('\n' + ('#' * (4 + len(player.location.name))))
    print('# ' + player.location.name + ' #')
    print('# ' + room[player.location.name].discription + ' #')
    print('\n' + ('#' * (4 + len(player.location.name))))

def prompt():
    print("\n" + "=========================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go','travel', 'walk', 'quit', 'examine', 'interact', 'inspect', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again. \n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go','travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'interact', 'inspect', 'look']:
        player_examine()

def player_move(myAction):
    ask = "Where would you like to move to? \n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = room[player.location.name].n_to
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = room[player.location.name].w_to
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = room[player.location.name].e_to
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = room[player.location.name].s_to
        movement_handler(destination)

def movement_handler(destination):
    if destination == 'wall':
        print('you have walked into a wall!!!')
    else:
        print("\n" + "You have moved to the" + destination.name + ".")
        player.location = destination
        print_location()

def player_examine():
    if len(room[player.location.name].item) is 0:
        print("you have already exhuasted this room")
    else:
        for i in room[player.location].item:
            print("You inspect the room and find " + i + "Would you like to take it?")
            


            


# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

### Game Functionality ###
def start_game():
    os.system('clear')

    question1 = "Hello, what's your name? \n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    player.name = player_name
    
    question2 = "What role do you want to play? \n"
    question2added = "You can play as a warrior, priest, or mage \n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        player.job = player_job
        print("\n you are now a " + player_job + "!")
    while player_job not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            player.job = player_job
            print("\n you are now a " + player_job + "!")

    if player.job is 'warrior':
        player.hp = 120
        player.mp = 20
    elif player.job is 'mage':
        player.hp = 40
        player.mp = 120
    elif player.job is 'priest':
        player.hp = 60
        player.mp = 60
    
    ### intro ###

    question3 = "Welcome " + player_name + " the" + player_job + "\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    os.system('clear')
    print('lets start now')
    main_game_loop()
    
    

def main_game_loop():
    while player.game_over is False:
        prompt()

title_screen()
