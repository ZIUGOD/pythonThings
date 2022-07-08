def clear():
    from os import name, system
    if name == "nt":
        system("cls")
    else:
        system("clear")

class bColors:
    BOLD      = '\033[1m'
    BLUE      = '\033[94m'
    CYAN      = '\033[96m'
    END       = '\033[0m'
    FAIL      = '\033[91m'
    GREEN     = '\033[92m'
    HEADER    = '\033[95m'
    UNDERLINE = '\033[4m'
    WARNING   = '\033[93m'

def waitTime(time):
    from time import sleep
    for i in reversed(range(0, time, 1)):
        print(bColors.WARNING + f"{i + 1}s remaining." + bColors.END)
        sleep(1)
        if i == 0:
            clear()