# Build a program that draws a number between 1 and 15.
# The user will have 3 chances of matching the value.
# At each attempt, you must tell it whether the kick is greater or less than the number.
# If the user gets it right, congratulate them.

import random  # importing to generate the random number

def get_input():  # function to get a valid number
    while True:
        try:
            user_number = int(input("Enter a number to guess: "))
        except ValueError as err:
            print("Invalid value!")
            continue

        if 1 <= user_number <= 15:  # validates user's input
            return user_number
        print("Invalid value")

def check_numbers(user_number, lucky_number):
    if user_number == lucky_number:
        print("Congratulations! You guessed it!")
        return True
    elif user_number > lucky_number:
        print("Choose a lower number")
        return False
    else:
        print("Choose a higher number")
        return False


lucky_number = random.randint(1, 15)  # generating a random number from 1 to 15

for i in range(3):
    user_number = get_input()  # calling the function to get input

    if i < 2:
        if check_numbers(user_number, lucky_number):
            break
    else:  # Last attempt: only checks if correct, doesn't give a hint
        if user_number == lucky_number:
            print("Congratulations! You guessed it!")
            break
else:
    print("Your attempts are over!")

