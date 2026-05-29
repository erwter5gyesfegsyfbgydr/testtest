import os
import platform

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

clear_console()

b = "\033[34m"
r = "\033[0m "

input(f"{b}[FunStatModule]{r}Enter username ~#")
