from typing import Any
import sys
import random

user = input("What is Your Name: \n")
lst = ["r", "p", "s"]

win = 0


def choice():
    global win
    b = random.choice(lst)
    user_inp = input(f"{user}'s Input: \n")
    if b == "r" and user_inp == "r":
        print("J.A.R.V.I.S says Rock\n"
              "No-one Wins !!")
    elif b == "r" and user_inp == "p":
        print("J.A.R.V.I.S says Rock\n"
              f"{user} Wins!!")
        win += 1
    elif b == "r" and user_inp == "s":
        print("J.A.R.V.I.S says Rock\n"
              f"J.A.R.V.I.S Wins!!")
    elif b == "p" and user_inp == "r":
        print("J.A.R.V.I.S says Paper\n"
              f"J.A.R.V.I.S Wins!!")
    elif b == "p" and user_inp == "p":
        print("J.A.R.V.I.S says Paper\n"
              "No-one Wins !!")
    elif b == "p" and user_inp == "s":
        print("J.A.R.V.I.S says Paper\n"
              f"{user} Wins!!")
        win += 1
    elif b == "s" and user_inp == "r":
        print("J.A.R.V.I.S says Scissors\n"
              f"{user} Wins!!")
        win += 1
    elif b == "s" and user_inp == "p":
        print("J.A.R.V.I.S says Scissors\n"
              f"J.A.R.V.I.S Wins!!")
    elif b == "s" and user_inp == "s":
        print("J.A.R.V.I.S says Scissors\n"
              "No-one Wins !!")
    else:
        print("Invalid Option \n"
              "Shutting Down!!!")
        sys.exit()


count = 0
while count < 10:
    choice()
    if win >= 5:
        print(f"\n* * * * * * *\n* * * * *\n* * * *\n* * *\n* *\n*\n\n{user} Wins!!!\n"
              f"Welcome Mr.{user} Stark")
        break
    elif count == 9 and win != 5:
        print("\n:( :( :( :( :( :( :(\n:( :( :( :( :( :(\n:( :( :( :(\n:( :( :(\n:( :(\n:(\nYou Didn't Win :(")
        break
    else:
        count += 1
