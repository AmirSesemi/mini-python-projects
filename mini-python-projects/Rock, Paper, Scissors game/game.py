# Rock Paper Scissors Game
# This is a simple game where you play against the computer.
# First to 10 points wins the round.

import random

# Score Variables to keep track of points
user_score = 0
cpu_score = 0

# Main game loop - runs until the user exits
while True:
    # Display menu options
    print(" 1 = Rock\n 2 = Paper\n 3 = Scissors\n 4 = exit")
    user_input = input(" Enter a number: ")

    # Check if user wants to exit
    if user_input == "4" or user_input.lower() == "exit":
        print(" Goodbye!")
        break

    # Validate that input is a number
    if user_input.isdigit():
        user_choice = int(user_input)

        # Check if number is within valid range
        if user_choice < 1 or user_choice > 3:
            print(" Please choose a number between 1 and 3")
            continue

        # Computer makes a random choice (1, 2, or 3)
        cpu_choice = random.randint(1, 3)

        # Show both choices
        print(f" You chose {user_choice} and the Bot chose {cpu_choice}")

        # Determine the winner
        if user_choice == cpu_choice:
            print(" It's a tie!")

        # Rock (1) beats Scissors (3)
        # Paper (2) beats Rock (1)
        # Scissors (3) beats Paper (2)
        elif (
            (user_choice == 1 and cpu_choice == 3)
            or (user_choice == 2 and cpu_choice == 1)
            or (user_choice == 3 and cpu_choice == 2)
        ):
            print(" You Win! (:")
            user_score += 1  # Increase user score

        else:
            print(" You Lose ):")
            cpu_score += 1  # Increase computer score

        # Check if someone reached 10 points
        if cpu_score == 10:
            print(" You lost this round!")
            # Reset scores for next round
            user_score = 0
            cpu_score = 0
        elif user_score == 10:
            print(" You won this round!!!")
            # Reset scores for next round
            user_score = 0
            cpu_score = 0

        # Display current scores
        print(f" Bot Score: {cpu_score}")
        print(f" Your Score: {user_score}")

    else:
        print(" Please enter a valid number!")
        
# Developed By AmirHosseinKhani.py
# Email : amirsesemi6@gmail.com
# instagram : AmirHosseinKhani.py
