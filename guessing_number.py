#https://www.geeksforgeeks.org/number-guessing-game-in-python/
#The program will select random number between a range
#The range will provided by the user
#User have to guess the random number based on minimum number of guessing (calculate by program)
#Each guess the program must response either too low or too high
#If user manage to guess, the program will congratulate
#If user didnt manage to guess exceed the guess number, the program will response better luck next time
import random
import math

def main ():
    upper_bound, lower_bound = getbound()
    rand_numb = randnumb(upper_bound, lower_bound)
    guess_numb = guessnumb(upper_bound,lower_bound)
    guess(rand_numb, upper_bound, lower_bound, guess_numb)

def getbound():
    upper_bound = int(input("Enter the upper bound number: "))
    lower_bound = int(input("Enter the lower bound number: "))
    if lower_bound > upper_bound:
        print("Invalid bound range")
    return upper_bound, lower_bound

def randnumb(upper_bound, lower_bound):
    return random.randint(lower_bound, upper_bound)

def guessnumb(upper_bound, lower_bound):
    return math.ceil(math.log(upper_bound - lower_bound +1,2))

def guess(rand__numb, upper_bound, lower_bound, guess_numb):
    guess_count = 1
    flag = False
    while guess_count <= guess_numb:
        uguess = int(input("Guess the random number: "))
        if uguess < lower_bound or uguess > upper_bound:
            print("Your guess is not in the range provided")
            guess_count = guess_count + 1
        elif uguess == rand__numb:
            print(f"Congrats you guess it in {guess_count} try!")
            flag=True
            break
        else:
            print("That's wrong guess, try again!")
            guess_count = guess_count + 1

    if flag == False:
        print(f"You run out guess! The random number is {rand__numb}")

if __name__ == "__main__":
    main()