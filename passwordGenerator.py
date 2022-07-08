from random import choice as pick
from time import sleep
from custom import *

print("————————————————————————————\n"
      "==== Password generator ====\n"
      "————————————————————————————\n")

while True:
    length = int(input("Insert your password length: "))
    if length >= 12:
        break
    else:
        print(bColors.WARNING + "\nFor your own safety, insert at least 12.\n" + bColors.END)
        continue

#    variables for the final password
numbers = "0123456789"
uppers  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers  = "abcdefghijklmnopqrstuvwxyz"
symbols = "{[]()}!'@#$%&*-_=+><.:\|/"

values = numbers + uppers + lowers + symbols    #all values in only one object

password = ""      # empty now but full after running the code

#    generating and printing
for i in range (length):
    password += pick(values)

clear()

print("-" * length)
print(password)
print("-" * length)
print("\n")

print("Closing console...")
waitTime(5)