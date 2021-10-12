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