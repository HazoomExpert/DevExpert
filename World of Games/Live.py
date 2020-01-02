import GuessGame
import CurrencyRouletteGame
import MemoryGame


def welcome (name):
    print("Hello " + name + " and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")



def load_game ():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    game_number = int(input(""))
    global difficulty
    difficulty = int(input("Please choose game difficulty from 1 to 5:"))
    if not (0 < game_number < 4):
        print("Please re-enter a game number")
    if not 0 < difficulty < 6:
        print("Please re-enter a game level")
    if game_number == 1:
        print(MemoryGame.play(difficulty))
    if game_number == 2:
        print(GuessGame.play(difficulty))
    if game_number == 3:
        print(CurrencyRouletteGame.play(difficulty))



