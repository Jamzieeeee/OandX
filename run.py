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

""" GET USERNAME """

def enter_username():
    """
    Get username from the user
    """
    username = input("Please enter a username:")
    print(f"Welcome {username}\n")

enter_username()

""" SELECT DIFFICULTY """

def select_difficulty():
    """
    Ask and set game difficulty
    """
    print("Please set your opponent difficulty\n")
    print("Easy: Chooses moves at random")
    print("Hard: Blocks lines of 2, but still random")
    print("Perfect: Plays perfectly and CANNOT be beaten\n")
    dif_str = input("Enter difficulty as spelled above: ")
    if dif_str == "Easy":
        difficulty = 1
        print("You have selected 'Easy' difficulty!")
    elif dif_str == "Hard":
        difficulty = 2
        print("You have selected 'Hard' difficulty!")
    elif dif_str == "Perfect":
        difficulty = 3
        print("You have selected 'Perfect' difficulty!")
    else:
        raise ValueError(
            f"{dif_str} is not a valid difficulty!"
        )
        dif_str = input("Please enter 'Easy', 'Hard', or 'Perfect': ")


select_difficulty()