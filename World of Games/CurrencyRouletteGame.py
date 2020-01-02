import requests
import random

difficulty = 0
min = 0
max = 0
number = random.randint(1, 100)


def get_money_interval(difficulty, number):
    global min
    global max
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    t = float(data["rates"]["ILS"])
    t = t * number
    min = t - (5 - difficulty)
    max = t + (5 - difficulty)
    # print("min: " + min + " max: " + max)


def get_guess_from_user(number):
    print("How much is " + str(number) + " US dollars in ILS")
    amount = float(input(""))
    return amount

def play(diff):
    global difficulty
    difficulty = diff
    get_money_interval(difficulty, number)
    amount = get_guess_from_user(number)
    if min < amount < max:
        return True
    else:
        return False

