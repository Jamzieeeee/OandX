from os import system, name
from time import sleep
import random


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
    while True:
        username = input("Please enter a username: ")
        username = username.strip()

        if len(username) < 3 or len(username) > 15:
            print("Username must be between 3 and 15 characters long")
            continue
        else:
            break
    main_menu()


# Go to main menu
def main_menu():
    """
    Show main menu screen
    """
    clear()
    print(f"Welcome {username} to...\n")
    sleep(1)
    print("""
     O |   |
    ---+---+---
     a | n | d
    ---+---+---
       |   | X
        \n""")
    sleep(1)
    print("1 = Start new game")
    sleep(0.5)
    print("2 = Change username\n")
    sleep(0.5)
    print("3 = Quit game")
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
            clear()
            print("Goodbye!")
            break
        else:
            print(f"{menu_str} is not a valid option")
            print("You must provide a number between 1 and 3")
            sleep(1)


# Select difficulty
def select_difficulty():
    """
    Ask and set game difficulty
    """
    clear()
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
            sleep(1)
            clear()
            reset()
            print_board(initial=True)
            play(first_player, turn)
            break
        elif dif_str == "2":
            difficulty = 2
            print("You have selected 'Hard' difficulty!")
            sleep(1)
            clear()
            reset()
            print_board(initial=True)
            play(first_player, turn)
            break
        elif dif_str == "3":
            difficulty = 3
            print("You have selected 'Perfect' difficulty!")
            break
        else:
            print(f"{dif_str} is not a valid difficulty!")


# Game
boxes = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
HUMAN = 'X'
COMPUTER = '0'
WINNING_COMBOS = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                  [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], ]


def reset():
    """
    Resets game board, turn number and first player
    """
    global boxes
    global turn
    global first_player
    boxes = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
    turn = 1
    first_player = HUMAN if random.randint(0, 1) else COMPUTER


def print_board(initial=False):
    """
    Print the game board. If this is the beginning of the game,
    print out 1-9 in the boxes to show players how to pick a
    box. Otherwise, update each box with X or 0 from boxes[].
    """
    print('''
             {} | {} | {}
            ---+---+---
             {} | {} | {}
            ---+---+---
             {} | {} | {}
        '''.format(*([x for x in range(1, 10)] if initial else boxes)))


def take_turn(player, turn):
    """
    Create a loop that keeps asking the current player for
    their input until a valid choice is made.
    """
    while True:
        if player is COMPUTER:
            box = get_computer_move()
        else:
            box = input(
                f'{username}, type a number from 1-9 to select a box: ')

            try:
                box = int(box) - 1  # subtract 1 to sync with index numbers
            except ValueError:
                # Not an integer
                print('That\'s not a valid number, try again.\n')
                continue

        if box < 0 or box > 8:
            print('That number is out of range, try again.\n')
            continue

        if boxes[box] == ' ':  # initial value
            boxes[box] = player  # set to value of current player
            break
        elif player == HUMAN:
            print('That box is already marked, try again.\n')


def get_computer_move():
    """
    Check for 2 in a row for computer and human and return 3rd box
    if difficulty = 2
    Otherwise return a random integer from 0 to 8, inclusive
    """
    if difficulty == 2:
        box = check_for_potential_win(COMPUTER)
        if box != -1:
            return box
        box = check_for_potential_win(HUMAN)
        if box != -1:
            return box
    return random.randint(0, 8)


def check_for_potential_win(player):
    """
    Return index of empty square that would complete or block a row,
    or returns -1 if none are found
    """
    for combo in WINNING_COMBOS:
        score = 0
        empty_index = -1
        for index in combo:
            if boxes[index] == player:
                score += 1
            elif boxes[index] == ' ':
                empty_index = index
            if score == 2 and empty_index != -1:
                return empty_index
    return -1


def switch_player(current_player):
    """
    Switch player to computer if current player is human
    """
    current_player = COMPUTER if current_player == HUMAN else HUMAN
    return current_player


def check_for_win(player, turn):
    """
    Check for a win (or a tie). For each combo in WINNING_COMBOS[],
    count how many of its corresponding squares have the current
    player's mark. If a player's score count reaches 3, return a win.
    If it doesn't, and this is already turn # 9, return a tie. If
    neither, return False so the game continues.
    """
    if turn > 4:  # need at least 5 moves before a win is possible
        for combo in WINNING_COMBOS:
            score = 0
            for index in combo:
                if boxes[index] == player:
                    score += 1
                if score == 3:
                    return 'win'

        if turn == 9:
            return 'tie'


def play(player, turn):
    """
    Create a loop that keeps the game in play
    until it ends in a win or tie
    """
    while True:
        take_turn(player, turn)
        print_board()
        result = check_for_win(player, turn)
        if result == 'win':
            print('Game over. %s wins!\n' % player)
            game_over()
            break
        elif result == 'tie':
            print('Game over. It\'s a tie.\n')
            game_over()
            break
        turn += 1
        player = switch_player(player)


def game_over():
    """
    Show options after game ends
    """
    sleep(1)
    print("1 = Play again")
    print("2 = Change difficulty")
    print("3 = Go back to main menu")
    print("4 = Quit")

    while True:
        game_over_str = input("Please enter an option: ")

        if game_over_str == "1":
            clear()
            reset()
            print_board(initial=True)
            play(first_player, turn)
            break
        elif game_over_str == "2":
            select_difficulty()
            break
        elif game_over_str == "3":
            main_menu()
            break
        elif game_over_str == "4":
            clear()
            print("Goodbye!")
            break
        else:
            print(f"{game_over_str} is not a valid option")
            print("You must provide a number between 1 and 4")
            sleep(1)


start()
