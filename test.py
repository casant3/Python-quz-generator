import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.RED + "some red text")
print(Back.GREEN + " and with a green background")
print(Style.BRIGHT + "annd in bright text")
print(Style.RESET_ALL)
print("back to normal now")