import random
from time import sleep

rand_list = []
difficulty = 0

def generate_sequence():
    global rand_list
    global difficulty
    for i in range(1, difficulty+1):
        rand_list.append(random.randint(1, 101))
    print(rand_list, end="")
    sleep(0.7)
    print("\r", end="\r")

def get_list_from_user():
    user_list = []
    global difficulty
    for i in range(1, difficulty + 1):
        user_input = int(input())
        user_list.append(user_input)
    return user_list


def is_list_equal():
    generate_sequence()
    return get_list_from_user() == rand_list


def play(diff):
    global difficulty
    difficulty = diff
    return is_list_equal()

