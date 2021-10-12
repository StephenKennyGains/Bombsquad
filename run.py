from random import choice


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


SMALL_BOARD = "   END \nD . . . .\nC . . . .\nB . . . .\nA . . . .\n \
1 2 3 4\n  START\n"
LARGE_BOARD = "   END \nH . . . .\nG . . . .\nF . . . .\nE . . . .\nD \
. . . .\nC . . . .\nB . . . .\nA . . . .\n  1 2 3 4\n  START\n"


def select_board():
    """
    Asks player if they would like to take the long route or the short route
    Long route will play 8 steps, short plays 4 steps.
    """
    print("Do you want to take the short way out or risk the long way \
out?\n".upper())
    select_path = input("Press -- 1 -- for short, press -- 2 -- for long. \n")
    player_path_choice = select_path
    path_options = ["1", "2"]
    if player_path_choice not in path_options:
        print("That was not an option")
        select_board()
    elif select_path == ("1"):
        print("\nOk safe choice, just make it from Row A to Row D \
without triggering a bomb.\n".upper())
        print("HERE IS YOUR PATH\n")
        print(SMALL_BOARD)
        small_board_play()
    elif select_path == ("2"):
        print("\nI hope luck is on your side!! Make it from Row A to \
Row H without triggering a bomb!!\n".upper())
        print("HERE IS YOUR PATH\n")
        print(LARGE_BOARD)
        large_board_play()


def choose_row(guess):
    """
    Let's player choose between column 1,2,3,4. If player
    guess is vaild, check if there has been a bomb randomly
    assigned in the space. If player choice is a bomb, game over.
    If player guess is not bomb, move to next row.
    """
    row = ["1", "2", "3", "4"]
    row_random_num = choice(row)
    bomb = row_random_num
    player_choice = input("\nCHOOSE YOUR NEXT STEP BETWEEN \
1, 2, 3 or 4:".upper())
    if player_choice not in row:
        print("UNLESS YOU'RE JUMPING OUT A WINDOW, THAT \
WASN'T AN OPTION".upper())
        choose_row(guess)
    elif player_choice == bomb:
        print("\nBOOOOOOOOOOOOOOOOOOOOM!!!!!!!!!\n")
        print("SORRY YOU DIDN'T MAKE IT OUT ALIVE!\n")
        restart_or_leave()
    elif player_choice != bomb:
        print("\nYOU'RE SAFE!")


def small_board_play():
    """
    Plays out a 4 guess board. If player guesses successfully
    through 4 spaces, gives message and request to play again
    or leave. If player guess is a bomb, game over and request
    restart of leave.
    """
    print("BEST OF LUCK IN THERE! YOU HAVE A 32% \
CHANCE OF MAKING IT OUT ALIVE\n")
    player_success = 4
    guess = 0
    while guess < player_success:
        choose_row(guess)
        guess += 1
        if guess == 1:
            print("Row A cleared. You now have a 42% \
chance of making it out alive!\n".upper())
        elif guess == 2:
            print("Row B cleared. You now have a 56% \
chance of making it out alive!\n".upper())
        elif guess == 3:
            print("Row C cleared. You now have a 75% \
chance of making it out alive!\n".upper())
        elif guess == 4:
            print("Row D cleared.\n".upper())
    print("CONGRATULATIONS, YOU MADE IT OUT ALIVE!")
    restart_or_leave()


def large_board_play():
    """
    Plays out an 8 guess board. If player guesses successfully
    through 8 spaces, gives message and request to play again
    or leave. If player guess is a bomb, game over and request
    restart of leave.
    """
    print("BEST OF LUCK IN THERE! YOU HAVE A 10% \
CHANCE OF MAKING IT OUT ALIVE\n")
    player_success = 8
    guess = 0
    while guess < player_success:
        choose_row(guess)
        guess += 1
        if guess == 1:
            print("Row A cleared. You now have a 13% \
chance of making it out alive!\n".upper())
        elif guess == 2:
            print("Row B cleared. You now have a 18% \
chance of making it out alive!\n".upper())
        elif guess == 3:
            print("Row C cleared. You now have a 24% \
chance of making it out alive!\n".upper())
        elif guess == 4:
            print("Row D cleared. You now have a 32% \
chance of making it out alive!\n".upper())
        elif guess == 5:
            print("Row E cleared. You now have a 42% \
chance of making it out alive!\n".upper())
        elif guess == 6:
            print("Row F cleared. You now have a 56% \
chance of making it out alive!\n".upper())
        elif guess == 7:
            print("Row G cleared. You now have a 75% \
chance of making it out alive!\n".upper())
        elif guess == 8:
            print("Row H cleared\n".upper())
    print("CONGRATULATIONS, YOU MADE IT OUT ALIVE!")
    restart_or_leave()


def restart_or_leave():
    """
    Asks player if they would like to restart game or
    leave whether they have been successful or failed.
    """
    print("\nWOULD YOU LIKE TO PLAY AGAIN OR LEAVE?:\n")
    restart_or_exit = input("PRESS --1-- TO PLAY AGAIN OR --2-- TO LEAVE: ")
    player_restart_choice = restart_or_exit
    restart_options = ["1", "2"]
    if player_restart_choice not in restart_options:
        print("WELL WE NEED TO EITHER RESTART OR LEAVE, SO LET'S TRY AGAIN:")
        restart_or_leave()
    elif player_restart_choice == ("1"):
        print("\nGREAT LET'S GO AGAIN\n")
        select_board()
    elif player_restart_choice == ("2"):
        print("\nTHANKS FOR PLAYING. SEE YOU AGAIN SOON!\n")
        exit()


def main():
    """
    Runs through entire process
    """
    start_game()
    start_or_leave()


main()
