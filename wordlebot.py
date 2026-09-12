import random
import json
from operator import index

# Load the words from words.json
with open('words_list.json', 'r') as file:
    words_list = json.load(file)

wordle = random.choice(words_list["words"])
english_alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
print(wordle)

def wordle_game():
    print("Welcome to Wordle: The objective is simple: Guess the correct 5 letter word within 6 tries!")
    print("✓ means correct and in the right spot, ~ means correct, but in the wrong spot, and X means incorrect. Good luck!")
    while True:
        guess = input("Answer: ").lower()
        len_g = len(guess)
        tries = 6

        for char in guess:
            if ' ' in guess:
                print("No Spaces Allowed")
            elif len_g != 5:
                print("Only 5 letter words are valid")
            elif not guess.isalpha():
                print("Only letters allowed!")
            elif char in guess != char in english_alphabet:
                print("_")
            elif guess != wordle:
                print("Correct Letters: ")
                for x, (c1, c2) in enumerate(zip(wordle, guess)):
                    if c1 == c2:
                        print(f"{c2} ✓")
                    elif c2 in wordle:
                        print(f"{c2} ~")
                    else:
                        print(f"{c2} x")
            elif guess == wordle:
                print("You win! You have won in X tries")
                break


class Wordle:
    def __init__(self):
        self.world_len = 5
        self.tries = 6
    def guess(self):
        


def wordlebot():
    