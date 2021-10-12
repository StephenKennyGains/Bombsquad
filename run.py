from random import *


def start_game():
    """
    Asks player for their Name and used the name to prompt
    player selection to continue or leave
    """
    print("\nWELCOME TO BOMBSQUAD \n")
    player_name = input("WHAT IS THE NAME OF OUR BOMB SQUAD EXPERT?:")
    print(f"\nOK {player_name}, ARE YOU READY TO BEGIN? \n")


def start_or_leave():
    """
    Asks player if they wish to continue and if so offer instructions
    If player selects no, bring back to start, or re prommpt invalidity.
    """
    play_or_leave = input("Press -- y -- to continue, press -- n -- \
to chicken out! \n")
    player_entry = play_or_leave
    player_choices = ["y", "n"]
    if player_entry not in player_choices:
        print("That was not an option".upper())
        start_or_leave()
    elif play_or_leave == ("n"):
        print("Ok just run it again when you're ready to begin.\n".upper())
        exit()
    elif play_or_leave == ("y"):
        instructions()


def instructions():
    """
    Asks player if they would like instructions or if they would like
    to proceed to board selection.
    """
    print("Would you like instructions from us or do you know what to \
do? \n".upper())
    for_instructions = input("Press -- i -- for instrctions, press -- \
b -- to choose board. \n")
    player_tips_choice = for_instructions
    instrcution_options = ["i", "b"]
    if player_tips_choice not in instrcution_options:
        print("That was not an option".upper())
        instructions()
    elif for_instructions == ("i"):
        print("We need to get you out of the building alive.\nThere are \
bombs scattered along the corridor and we don't know where \
they are.\nStarting from row A we need to get you to \
the end of the corridor.\nYou can move forward one \
row at a time and choose between four spaces 1, 2, 3 or 4.\
\nBut you'll need luck on your side.\n".upper())
        select_board()
    elif for_instructions == ("b"):
        print("\nOk let's see what we're dealing with here.\n".upper())
        select_board()