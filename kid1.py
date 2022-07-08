from random import randint
from custom import clear, bColors

start  = 0
ending = 10
clear()

user = str(input("Hi, what's your name, user? "))
print(f"Hey, {user}. In this game you may figure out the right number, lets do it?!\n")

ending = int(input("Insert a random positive number: "))
clear()
print(f"Ok, you have to figure out the right number between {start} and {ending}!\n")

value = randint(start, ending)

for i in range (start, ending):
    userTry = int(input(f"Insert a number betweet {start} and {ending}: "))
    if userTry == value:
        print(bColors.GREEN + f"Nice!! You found the value: " + bColors.END + f"{value}")
        break
    elif userTry not in range (start, ending):
        print(bColors.WARNING + f"Please, insert only numbers between {start} and {ending}!" + bColors.END)
        userTry = ""
    else:
        print(bColors.FAIL + "Wrong value. Try again." + bColors.END)
        continue

input("\nPress enter to close console.")