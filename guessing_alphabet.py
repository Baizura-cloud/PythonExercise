#https://www.geeksforgeeks.org/python-program-for-word-guessing-game/
#program will have list of strings
#user need to enter their name first
#program will randomly choos string from the list
#program will ask user to guess the alphabet contains the random string
#user will have a number of guess
import random
import re

def main():
    words = ["pizza", "ball", "dance", "spring"]
    word = choose_word(words)
    numb_guess = 5
    guess(word, numb_guess)

def choose_word(words):
    return random.choice(words) 

def guess(word, numb_guess):
    name = input("Enter your name: ")
    count_guess = 1
    flag = False
    while count_guess <= numb_guess:
        uguess = input("Guess the alphabet in the words: ")
        guess_match = re.findall(uguess , word)
        if len(guess_match) > 0:
            count_guess= count_guess + 1
            print(f"{uguess} exist {len(guess_match)} in the word, guess more")
        else:
            print("Wrong guess, try again")
            count_guess= count_guess + 1
    if flag == False:
        print(f"The word is {word} thanks for playing {name}")

if __name__ == "__main__":
    main()