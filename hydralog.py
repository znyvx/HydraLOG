#!/usr/bin/env python3
import sys
import os
import platform

class DummyFore:
    RED = GREEN = BLUE = CYAN = MAGENTA = RESET = ""
Fore = DummyFore()
def init(autoreset=True):
    pass

def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def banner():
    print(Fore.MAGENTA + r"""
  __    __  ___  ___  ________    _______        __      ___        ______    _______   
 /" |  | "\|"  \/"  ||"      "\  /"      \      /""\    |"  |      /    " \  /" _   "|  
(:  (__)  :)\   \  / (.  ___  :)|:        |    /    \   ||  |     // ____  \(: ( \___)  
 \/      \/  \\  \/  |: \   ) |||_____/   )   /' /\  \  |:  |    /  /    ) :)\/ \       
 //  __  \\  /   /   (| (___\ || //      /   //  __'  \  \  |___(: (____/ // //  \ ___  
(:  (  )  :)/   /    |:       :)|:  __   \  /   /  \\  \( \_|:  \\        / (:   _(  _| 
 \__|  |__/|___/     (________/ |__|  \___)(___/    \___)\_______)\"_____/   \_______)  
""" + Fore.CYAN + "                                                                              v. 1.2.4\n" + Fore.RESET)
    print(Fore.BLUE + "Created by: " + Fore.GREEN + "znyvx" + Fore.RESET)

def menu():
    print(Fore.CYAN + "\n[1] IP Info")
    print("[2] Phone Number Info")
    print("[0] Exit\n")

def main():
    while True:
        clear()
        banner()
        menu()
        choice = input(">> ")
        if choice == "1":
            print("IP function - coming soon")
            input()
        elif choice == "2":
            print("Phone function - coming soon")
            input()
        elif choice == "0":
            sys.exit(0)

if __name__ == "__main__":
    main()
