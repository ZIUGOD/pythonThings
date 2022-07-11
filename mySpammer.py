from pyautogui import write, press
from random import choice as pick
from custom import waitTime, clear
from time import sleep
clear()
x = int(input("How many messages? "))
clear()
waitTime(10)
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()+-=1234567890§^][)(>.<,"
for i in range (1, x + 1):
    print(f"{i}° shot... ", end="")
    password = ""
    for j in range (12):
        password += pick(chars)
    write("*~_" + password + password + "_~*")
    press("enter")
    print("Ok!")
write("by: ZiUG0D")
press("enter")
clear()
print("Done!\nClosing console in 10 seconds")
sleep(10)