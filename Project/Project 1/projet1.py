from random import randint, seed
import messages

"""
import sys

sys.path.append('/pub/code')
"""


def find_best_move(b):  # Function to find the best move
    for i in range(5, 2, -1):
        if (b - i) % 5 == 0:
            return i - 1
    return 1


def new_game():
    if input(messages.entree_4) == "non":  # Ask if the user wants to play again
        print(messages.message_11)
        exit()
    else:
        print(messages.message_10)


print(messages.message_1)  # Welcome message
try:
    graine = int(input(messages.entree_1))  # Seed input
except ValueError:  # If the user doesn't enter an integer take 0 as seed
    graine = 0
    print(messages.error_1)
seed(graine)

while True:  # Loop to play again
    print(messages.message_2)  # Rules
    try:
        billes = int(input(messages.entree_2))  # Number of balls input
    except ValueError:  # If input is not an integer
        billes = 0
    while billes < 6 or billes > 40:  # Loop to get a valid number of balls
        print(messages.error_2)
        try:
            billes = int(input(messages.entree_2))  # Number of balls input
        except ValueError:  # If input is not an integer ( if the user doesn't understand the rules )
            print(messages.error_3)
    print(messages.message_3)
    play = True

    while play:  # Loop to play
        if billes == 1:  # If there is only one ball left game over
            play = False
            print(messages.message_9)
            new_game()
        else:  # If there is more than one ball left
            print(messages.message_4.format(billes))
            try:
                inp = int(input(messages.entree_3))  # Number of balls to remove input
            except ValueError:  # If input is not an integer
                inp = 0
            while inp > 4 or inp < 1:  # Loop to get a valid number of balls to remove
                print(messages.error_4)
                try:
                    inp = int(input(messages.entree_3))  # Number of balls to remove input
                except ValueError:  # If input is not an integer ( if the user doesn't understand the rules )
                    print(messages.error_3)
            billes -= inp  # Remove the balls
            if billes == 1:  # If there is only one ball left game over for the IA
                play = False
                print(messages.message_8)
                new_game()
            else:  # If there is more than one ball left
                print(messages.message_5.format(billes))
                print(messages.message_6)
                if (billes - 1) % 5 == 0:  # If the number of balls minus 1 is a multiple of 5
                    if billes >= 7:  # If there is more than 6 balls left
                        inp = randint(1, 100)  # Random number
                        if inp <= 70:  # 70% chance to remove 1 ball
                            inp = 1
                        else:  # 30% chance to remove 2 balls
                            inp = 2
                    else:  # If there is less than 7 balls left remove 1 ball
                        inp = 1
                else:
                    inp = find_best_move(billes)  # Find the best move
                billes -= inp  # Remove the balls
                print(messages.message_7.format(inp))
