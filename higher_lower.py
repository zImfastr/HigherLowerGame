import colorama
from colorama import Fore, Back, Style
import os
import secrets

os.system("")

print("Welcome to:")
print("The " + Fore.GREEN + "Higher" + Fore.RED + "Lower " + Style.RESET_ALL + "Game!")

def Random_Number(a):
    n = secrets.randbelow(a)
    return n

score = 0

def game(right_answer, input, rand, rand2,):
    global score
    if rand2 > rand or rand2 == rand:
        right_answer += "Higher"
    else:
        right_answer += "Lower"

    if input == right_answer:
        score += 1
        print(f"{Fore.GREEN}You won, the Number was {rand2}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}You're Score: {score}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}You Loose, the Number was {rand2}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}You're Score was: {score}{Style.RESET_ALL}")
        score = 0

while True:

    first_number = Random_Number(13) + 1
    second_number = Random_Number(13) + 1
    print(f"The Next Number is: {Fore.YELLOW}{first_number}{Style.RESET_ALL}")
    player_input = input("Higher or Lower? ")
    game("", player_input, first_number, second_number)
