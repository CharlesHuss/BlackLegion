import socket, os, time, threading, colorama
from colorama import Fore
from datetime import datetime
from socket import*

from Scan import*
from Attaque import*


colorama.init()
print(Fore.BLUE+"  ____  _               _____ _  __     _      ______ _____ _____ ____  _   _ \n"
	           +" |  _ \| |        /\   / ____| |/ /    | |    |  ____/ ____|_   _/ __ \| \ | |\n"
	           +" | |_) | |       /  \ | |    | ' /     | |    | |__ | |  __  | || |  | |  \| |\n"
	           +" |  _ <| |      / /\ \| |    |  <      | |    |  __|| | |_ | | || |  | | . ` |\n"
	           +" | |_) | |____ / ____ \ |____| . \     | |____| |___| |__| |_| || |__| | |\  |\n"
	           +" |____/|______/_/    \_\_____|_|\_\    |______|______\_____|_____\____/|_| \_|\n"+Fore.RESET+Fore.GREEN)


def main():
	n = input(           " 1- Scan\n"
			  			 " 2- Attaque\n"
			  			 " 3- \n\n"
			  			 " >: ")
	if n == "1":
		scan()

	elif n == "2":
		attaque()

	elif n == "3":
		pass

if __name__ == "__main__":
	main()
