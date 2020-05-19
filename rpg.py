import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

#### player setup ###
class player:
    def __init__(self):
        self.name = ''
        self.myClass = ''
        self.hp = 0
        self.mp = 0
        self.gold = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False
myPlayer = player()

#title screen
def title_screen_selections():
    option = input("> ")
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == 'quit':
        sys.exit
    while option.lower() not in ['play', 'help', 'quit']:
        print("Command not valid.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()


def title_screen():
    os.system('cls')
    print("###################################################")
    print("###########  Welcome to Isaia's Game! #############")
    print("###################################################")
    print("###################################################")
    print("###################################################")
    print("#########           - Play -              #########")
    print("#########           - Help -              #########")
    print("#########           - Quit -              #########")
    print("#########                                 #########")
    print("###################################################")
    print("################ Copyright 2020 ###################")
    print("################ Isaia Wariner  ###################")
    print("###################################################")
    print("###################################################")
    print("###################################################")
    print("###################################################")
    title_screen_selections()

def help_menu():

    print("###################################################")
    print("########## Welcome to Isaia's Game ###############")
    print("###################################################")
    print("######################O###O########################")
    print("########################+##########################")
    print("######################^^^^^########################")
    print("###################################################")
    print("###################################################")
    print("###################################################")
    print("######## Use up, down, left, right to move ########")
    print("#########           - Help -              #########")
    print("#########           - Quit -              #########")
    print("#########                                 #########")
    print("################ Copyright 2018 ###################")
    print("############### Kalidor Vorlich ###################")
    print("###################################################")
    print("###################################################")
    print("###################################################")
    print("###################################################")
    title_screen_selections()





ZONENAME = ''
DESCRIPTION = 'DESCRIPTION'
examination = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'


solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                'b1': False, 'b2': False, 'b3': False, 'b4': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False,
                'd1': False, 'd2': False, 'd3': False, 'd4': False,
                }

zonemap = {
    'a1':{
        ZONENAME: 'Town Market',
        DESCRIPTION: 'DESCRIPTION',
        examination: 'info',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2'
    },

    'a2':{
        ZONENAME: 'Town Entrance',
        DESCRIPTION: 'DESCRIPTION',
        examination: 'info',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3'
    },    
    
    'a3':{
        ZONENAME: 'Town Square',
        DESCRIPTION: 'DESCRIPTION',
        examination: 'info',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4'
    },    
    
    'a4':{
        ZONENAME: 'Town Shop',
        DESCRIPTION: 'DESCRIPTION',
        examination: 'info',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: ''
    },    
    
    'b1':{
        ZONENAME: '',
        DESCRIPTION: 'DESCRIPTION',
        examination: 'info',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2'
    },    

    'b2':{
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your home.',
        examination: 'Your home looks the same as always.',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3'
    },    
    
    'b3':{
        ZONENAME: '',
        DESCRIPTION: 'DESCRIPTION',
        examination: 'info',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },    
    
    'b4':{
        ZONENAME: '',
        DESCRIPTION: 'DESCRIPTION',
        examination: 'info',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: 'b5',
    },    
    
    'c1':{
        ZONENAME: '',
        DESCRIPTION: 'DESCRIPTION',
        examination: 'info',
        SOLVED: False,
        UP: 'b1',
        DOWN: 'd1',
        LEFT: '',
        RIGHT: 'c2'
    },    
    
    'c2':{
        ZONENAME: '',
        DESCRIPTION: 'DESCRIPTION',
        examination: 'info',
        SOLVED: False,
        UP: 'b2',
        DOWN: 'd2',
        LEFT: 'b1',
        RIGHT: 'c3'
    },    
    
    'c3':{
        ZONENAME: '',
        DESCRIPTION: 'DESCRIPTION',
        examination: 'info',
        SOLVED: False,
        UP: 'b3',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4'
    },    
    
    'c4':{
        ZONENAME: '',
        DESCRIPTION: 'DESCRIPTION',
        examination: 'info',
        SOLVED: False,
        UP: 'b4',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: ''
    },    
    
    'd1':{
        ZONENAME: '',
        DESCRIPTION: 'DESCRIPTION',
        examination: 'info',
        SOLVED: False,
        UP: 'c1',
        DOWN: '',
        LEFT: '',
        RIGHT: 'd2'
    },    
    
    'd2':{
        ZONENAME: '',
        DESCRIPTION: 'DESCRIPTION',
        examination: 'info',
        SOLVED: False,
        UP: 'd3',
        DOWN: '',
        LEFT: 'd1',
        RIGHT: 'd3'
    },    
    
    'd3':{
        ZONENAME: '',
        DESCRIPTION: 'DESCRIPTION',
        examination: 'info',
        SOLVED: False,
        UP: 'c3',
        DOWN: '',
        LEFT: 'd2',
        RIGHT: 'd4'

    },    
    
    'd4':{
        ZONENAME: '',
        DESCRIPTION: 'DESCRIPTION',
        examination: 'info',
        SOLVED: False,
        UP: 'c4',
        DOWN: '',
        LEFT: 'd3',
        RIGHT: '',

    },    

}



#game interactivity
def print_location():
    print('\n' + '#' * (4 + len(myPlayer.location)))
    print('# ' + myPlayer.location + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + '#' * (4 + len(myPlayer.location)))


def prompt():
    print("\n" + "===================================")
    print('What would you like to do?')
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print('Unknown action. Try again.\n')
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(myAction):
    ask = 'Where do you want to move to?'
    dest = input(ask)
    if dest in ['up', 'north']:  
        destination = zonemap[myPlayer.location[UP]]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location[DOWN]]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location[LEFT]]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location[RIGHT]]
        movement_handler(destination)

def movement_handler(destination):
    print('\n' + 'You have moved to the ' + destination + '.')
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zonemap[myPlayer.location] [SOLVED]:
        print('You have already exhausted this zone')
    else:
        print('You can trigger puzzle here')


#game
def main_game_loop():
    while myPlayer.game_over is False:
        prompt()


def setup_game():
    os.system('cls')
    ####name selector
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name.capitalize()

    #class selector
    question2 = f"Nice to meet you {player_name}, what class would you like to play as?\n"
    question2added = "You can play as a warrior, mage, archer, or thief.\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

    player_class = input("> ")
    valid_classes = ['warrior', 'mage', 'archer', 'thief']
    if player_class.lower()in valid_classes:
        myPlayer.myClass = player_class
        print(f"You are now a {player_class}!\n")
    else:
        while player_class.lower not in valid_classes:
            player_class = input("> ")
            if player_class.lower()in valid_classes:
                myPlayer.myClass = player_class
                print(f"You are now a {player_class}!\n")
                input('\n')
                return 'cls'
                main_game_loop()



    #player stats

    # if player_class == 'warrior':
    #     self.hp = 120
    #     self.mp = 20
    # elif myPlayer.myClass == 'mage':
    #     self.hp = 50
    #     self.mp = 120
    # elif myPlayer.myClass == 'archer':
    #     self.hp = 90
    #     self.mp = 60
    # elif myPlayer.myClass == 'thief':
    #     self.hp = 90
    #     self.mp = 90
        

    question3 = "Welcome" + player_name + "the." + player_class + " \n"
    question2added = "You can play as a warrior, mage, archer, or thief.\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    

    speech1 = "Welcome to your new life...\n"
    speech2 = "I hope you never leave...\n"
    speech3 = "May your old life be forgotten...\n"
    speech4 = "heheheheh...\n"

    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)    
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)

    os.system('cls')
    print('##############')
    print('# Link Start!#')
    print('##############')
    main_game_loop()
    


# title_screen()
# main_game_loop()

def gamegame():
    title_screen()
    setup_game()
    main_game_loop()

gamegame()