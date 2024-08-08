#https://www.geeksforgeeks.org/python-program-implement-rock-paper-scissor-game/
# Winning Rules as follows:
# Rock vs paper-> paper wins
# Rock vs scissor-> Rock wins
# paper vs scissor-> scissor wins.
import random

def main():
    us_choice = choice()
    us_hand = assign_hand(us_choice)
    prg_choice = random.choice(["Rock", "Paper", "Scissor"])
    versus(us_hand, prg_choice)

def choice():
    print("Enter selection based on the number assign\n1 - Rock\n2 - Paper\n3 - Scissor")
    us_choice = int(input("Enter your choice: "))
    if us_choice < 1 or us_choice > 3:
        while us_choice < 1 or us_choice > 3:
            us_choice = int(input("Input invalid, enter valid choice: "))
    else:
        return us_choice
    
def assign_hand(us_choice):
    if us_choice == 1:
        return "Rock"
    elif us_choice == 2:
        return "Paper"
    else:
        return "Scissor"
    
def versus(us_hand, prg_choice):
    if us_hand == prg_choice:
        print(f"Draw! you both choose {prg_choice}")
    elif us_hand == "Rock" and prg_choice == "Paper":
        print(f"I win! I choose {prg_choice}")
    elif us_hand == "Rock" and prg_choice == "Scissor":
        print(f"You win! I choose {prg_choice}")
    elif us_hand == "Paper" and prg_choice== "Scissor":
        print(f"I win! I choose {prg_choice}")
    elif us_hand == "Paper" and prg_choice == "Rock":
        print(f"You win! I choose {prg_choice}")
    elif us_hand == "Scissor" and prg_choice == "Paper":
        print(f"You win! I choose {prg_choice}")
    elif us_hand == "Scissor" and prg_choice == "Rock":
        print(f"I win! I choose {prg_choice}")
    else:
        print("I confuse...")
    


if __name__ == "__main__":
    main()