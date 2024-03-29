"""
This file contains skeleton code for implementing a tic tac toe game in python

End result will be a 2-player interactive game

"""

def play_turn(player, board): # 3rd
    """
    Execute a single turn
    Inputs:
        player - int (1 or 2)
        board - 2D list
    Outputs: None
    """


def check_win(board): # 4th
    """
    Check for any win
    Inputs:
        board - 2D list
    Outputs:
        win - boolean
    """

    # check rows

    # check cols

    # check main diagonal

    # check other diagonal


def print_board(board): #2nd
    """
    Print current form of board
    Inputs:
        board - 2D list
    Outputs: None
    """

    # Print column numbers

    # Print board with row numbers



def play_game(): #1st
    """
    Driver for gameplay
    Inputs: None
    Outputs: None
    """
    print("===============================================================")
    print(" Welcome! We're going to be playing a fun game of tic-tac-toe!\n Make sure that you have 2 players ready :)")
    print("===============================================================")

    while True:
        # Get valid inputs from user for board dimensions
        # define variable, use input() function to get user input
        user_dimension_input = input("Please enter your desired board size: ")
        # check it's a number and greater than or equal to 3
        if user_dimension_input.isdigit() and int(user_dimension_input) >= 3:
            user_dimension_input = int(user_dimension_input)
            break
        else:
            print("You gave invalid input, please try again with a number that is 3 or greater!")

    # Define the board


    # Play game until win or tie condition is met



if __name__ == "__main__":
    play_game()
