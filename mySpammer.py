from pyautogui import write, press
from random import choice as pick
from custom import * 
from time import sleep
clear()
x = int(input("How many messages? "))
clear()
waitTime(10)
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&()+-=1234567890§^][)(>.<,"
for i in range (1, x + 1):
    print(f"{i}° shot... ", end="")
    password = ""
    for j in range (128):
        password += pick(chars)
    write("*~_" + password + password + "_~*")
    press("enter")
    print("Ok!")
write("\nby: ZiUG0D")
press("enter")
clear()
print("Done!\nClosing console in 10 seconds")
sleep(10)