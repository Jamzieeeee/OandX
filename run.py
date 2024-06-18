# import only system from os
from os import system, name
 
# import sleep to show output for some time period
from time import sleep

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('OandX')

# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Start function
def start():
    clear()
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(1)
    enter_username()

# Get username
def enter_username():
    """
    Get username from the user
    """
    clear()
    global username
    username = input("Please enter a username:")
    main_menu()

# Go to main menu
def main_menu():
    """
    Show main menu screen
    """
    clear()
    print(f"Welcome {username} to...\n")
    sleep(2)
    print("""\
 .----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. |
| |     ____     | | |              | | |              | |
| |   .'    `.   | | |              | | |              | |
| |  /  .--.  \  | | |              | | |              | |
| |  | |    | |  | | |              | | |              | |
| |  \  `--'  /  | | |      _       | | |      _       | |
| |   `.____.'   | | |     (_)      | | |     (_)      | |
| |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' |
 .----------------. .-----------------..----------------. 
| .--------------. | .--------------. | .--------------. |
| |      __      | | | ____  _____  | | |  ________    | |
| |     /  \     | | ||_   \|_   _| | | | |_   ___ `.  | |
| |    / /\ \    | | |  |   \ | |   | | |   | |   `. \ | |
| |   / ____ \   | | |  | |\ \| |   | | |   | |    | | | |
| | _/ /    \ \_ | | | _| |_\   |_  | | |  _| |___.' / | |
| ||____|  |____|| | ||_____|\____| | | | |________.'  | |
| |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' |
 .----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. |
| |              | | |              | | |  ____  ____  | |
| |              | | |              | | | |_  _||_  _| | |
| |              | | |              | | |   \ \  / /   | |
| |              | | |              | | |    > `' <    | |
| |      _       | | |      _       | | |  _/ /'`\ \_  | |
| |     (_)      | | |     (_)      | | | |____||____| | |
| |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' 
        \n""")
    sleep(2)
    print("1 = Start new game")
    sleep(0.5)
    print("2 = Change username")
    sleep(0.5)
    print("3 = ...")
    sleep(0.5)
    print("4 = ...")
    sleep(0.5)
    print("5 = Quit game")
    sleep(0.5)
    while True:
        menu_str = input("Please enter an option: ")

        if menu_str == "1":
            select_difficulty()
            break
        elif menu_str == "2":
            enter_username()
            break
        elif menu_str == "3":
            print("Unavailable")
        elif menu_str == "4":
            print("Unavailable")
        elif menu_str == "5":
            clear()
            print("Goodbye!")
            break
        else:
            print(f"{menu_str} is not a valid option")
            print("You must provide a number between 1 and 5")
            sleep(1)

# Select difficulty
def select_difficulty():
    """
    Ask and set game difficulty
    """
    print("Please set your opponent difficulty\n")
    print("1 = Easy: Chooses moves at random")
    print("2 = Hard: Blocks lines of 2, but still random")
    print("3 = Perfect: Plays perfectly and CANNOT be beaten\n")

    global difficulty

    while True:
        dif_str = input("Enter difficulty number: ")

        if dif_str == "1":
            difficulty = 1
            print("You have selected 'Easy' difficulty!")
            break
        elif dif_str == "2":
            difficulty = 2
            print("You have selected 'Hard' difficulty!")
            break
        elif dif_str == "3":
            difficulty = 3
            print("You have selected 'Perfect' difficulty!")
            break
        else:
            print(f"{dif_str} is not a valid difficulty!")

start()