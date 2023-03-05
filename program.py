import os
from time import sleep
import sys
import random
from termcolor import colored, cprint

# essential variables

balance = 5
fruit = ['🍇', '🍊', '🍎', '🥝', '🍆', '💎', '🌟', '💩', '🥓']
slot_1 = "X"
slot_2 = "X"
slot_3 = "X"
rolls = 0
msg = " | Messages will be printed here!"
lboard = {}
speed = 0.3

# essential functions

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') #- clear term



def waiting_animation(): #- animation
    line = ""
    for x in range(1, 3):
        while len(line) < 4:
            print(line)
            line += "."
            sleep(speed)
            clear()
        line = ""
    pass

# menu and leaderboard screen


def menu():
  print("Welcome to the slot machine!")
  menu = input("Type 'leaderboard' to view the leaderboard, just press enter to enter continue to the game. ")
  clear()
  if menu == 'leaderboard':
    for x in open('leaderboard.txt', 'r'):
      print(x)
      sleep(0.5)

    input("Press enter to continue")
    clear()
  
  
# main game

menu()


while balance > 0:

    #- Printing of slot machine

    print("||"+slot_1+"||", "||"+slot_2+"||", "||"+slot_3+"||", '--- balance:', balance, '--- rolls:', rolls, msg)
    
    
    if input("Press 'enter' to roll the machine: ") == "speed_up":
        speed = 0.05
    waiting_animation()
    
    #- Number gen
    
    i = random.randint(0, 8)
    slot_1 = fruit[i]
    i = random.randint(0, 8)
    slot_2 = fruit[i]
    i = random.randint(0, 8)
    slot_3 = fruit[i]

    msg = ""
    
    #- Points calculator
    if slot_1 == slot_2 or slot_2 == slot_3: #- 2 in a row
        balance += 2
        msg += colored(" | You got 2 in a row! +2 balance", "blue")
    if slot_1 == slot_2 == slot_3: #- 3 in a row
        balance += 5
        msg = colored(" | You got 3 in a row! +5 balance", "magenta")
    if slot_1 == slot_2 or slot_1 == slot_3 or slot_2 == slot_3: #- 2 matching
        balance += 1
        msg += colored(" | You got 2 of the same! +1 balance", "green")
    else:
        balance -= 1
        msg += colored(" | You did not match anything! -1 balance", "red") #- nothing
    if slot_1 == "🥓" or slot_2 == "🥓" or slot_3 == "🥓": #- bacon
        balance -= 1
        msg += colored(" | HARAM! -1 balance", "red")
    if slot_1 == "🌟" or slot_2 == "🌟" or slot_3 == "🌟": #- star
        balance += 1
        msg += colored(" | Wish upon a star! +1 balance", "green")
    if slot_1 == "💩" or slot_2 == "💩" or slot_3 == "💩": #- poo
        balance -= 1
        msg += colored(" | Ew! -1 balance", "red")      
    
    rolls += 1

clear()
print(f"You finished with a score of {rolls}")

if input("Would you like to save your score? (y/n): ") == "y":
    name = input("Enter your name: ")
    with open("leaderboard.txt", "a") as f:
        f.write(f"{name}: {rolls} rolls\n")
input("Open and close the program to play again.")