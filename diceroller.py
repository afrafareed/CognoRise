import random
import time

print("Welcome to the game Dice Roller")
time.sleep(2)
print("-------------------------------")

print("How many dice would you like to Roll?")
time.sleep(2)

while True:
    try:
        numberpicked = int(input("Type an integer between 1 and 10: "))
        if(numberpicked > 0 and numberpicked < 10):
            break
        else:
            print("Invalid input . Try again")
        
    except:
        print("Please provide an Interger")

def rolldice(amountofdice):
    totalsum = 0
    possiblefaces = [1,2,3,4,5,6]
    for die in range(amountofdice):
        roll = random.choice(possiblefaces)
        print("Die", die + 1, ":", roll)
        time.sleep(2)
        totalsum += roll
    print("Total sum :", totalsum)
rolldice (numberpicked)
