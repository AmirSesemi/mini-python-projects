# Student Grade Analyzer
# This program calculates averages, finds min/max scores,
# and categorizes students based on their grades.

import sys

# Variables for tracking highest and lowest scores
max_score = 0
min_score = 20

# Category counters for grade distribution
above_12 = 0      # Students with average above 12
between_10_12 = 0 # Students with average between 10 and 12
under_10 = 0      # Students with average below 10

# Loop through 10 students
for nomarat in range(10):
    # Get scores for each subject
    get_score_math = input("Enter Math Score: ")
    get_score_chemistry = input("Enter Chemistry Score: ")
    get_score_geoghraphy = input("Enter Geography Score: ")
    get_score_language = input("Enter Foreign Language Score: ")
    get_score_logic = input("Enter Logic Score: ")

    # Convert inputs to integers
    get_score_math_int = int(get_score_math)
    get_score_chemistry_int = int(get_score_chemistry)
    get_score_logic_int = int(get_score_logic)
    get_score_language_int = int(get_score_language)
    get_score_geoghraphy_int = int(get_score_geoghraphy)

    # Validate scores are between 0 and 20
    if (
        get_score_chemistry_int < 0
        or get_score_chemistry_int > 20
        or get_score_geoghraphy_int < 0
        or get_score_geoghraphy_int > 20
        or get_score_language_int < 0
        or get_score_language_int > 20
        or get_score_math_int < 0
        or get_score_math_int > 20
        or get_score_logic_int < 0
        or get_score_logic_int > 20
    ):
        print("Please enter a number between 0 and 20. Try Again.")
        sys.exit()
    else:
        # Calculate average score
        moadel = (
            get_score_math_int
            + get_score_chemistry_int
            + get_score_logic_int
            + get_score_language_int
            + get_score_geoghraphy_int
        ) / 5
        print(f"Your Average: {moadel}")

        # Update highest score
        if get_score_math_int > max_score:
            max_score = get_score_math_int
        if get_score_chemistry_int > max_score:
            max_score = get_score_chemistry_int
        if get_score_geoghraphy_int > max_score:
            max_score = get_score_geoghraphy_int
        if get_score_language_int > max_score:
            max_score = get_score_language_int
        if get_score_logic_int > max_score:
            max_score = get_score_logic_int

        # Update lowest score
        if get_score_math_int < min_score:
            min_score = get_score_math_int
        if get_score_chemistry_int < min_score:
            min_score = get_score_chemistry_int
        if get_score_geoghraphy_int < min_score:
            min_score = get_score_geoghraphy_int
        if get_score_language_int < min_score:
            min_score = get_score_language_int
        if get_score_logic_int < min_score:
            min_score = get_score_logic_int

        # Motivational messages based on average
        if moadel == 17 and 18 and 19:
            print("Great job! You got a good average! (: ")
        elif moadel == 20:
            print("Excellent! Perfect score!!")
        elif moadel <= 16:
            print("Good effort! You could do even better! (:")
        elif moadel <= 12:
            print("You need to study harder ):")
        elif moadel <= 9:
            print("I didn't expect this average. You need to retake the course!!")

        # Categorize students by grade range
        if moadel >= 12:
            above_12 = above_12 = +1
        elif moadel >= 10:
            between_10_12 = between_10_12 = +1
        elif moadel < 10:
            under_10 = under_10 = +1

        # Display highest and lowest scores
        print(f"Highest Score: {max_score}")
        print(f"Lowest Score: {min_score}")

        # Display grade distribution summary
        print(
            f"Student Grade Distribution\nAbove 12 : {above_12}\nBetween 10 and 12 : {between_10_12}\nBelow 10 : {under_10}"
        )

# Developed By AmirHosseinKhani.py
# Email : amirsesemi6@gmail.com
# instagram : AmirHosseinKhani.py
