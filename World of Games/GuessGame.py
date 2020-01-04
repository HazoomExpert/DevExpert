import random

difficulty = 0
secret_number = 0

def generate_number():
    global secret_number
    secret_number = random.randint(1, difficulty)


def get_guess_from_user():
    global difficulty
    print("choose a number between 1 to " + str(difficulty))
    number = int(input(""))
    return number


def compare_results ():
    generate_number()
    return secret_number == int(get_guess_from_user())


def play (diff):
    global difficulty
    difficulty = diff
    return compare_results()