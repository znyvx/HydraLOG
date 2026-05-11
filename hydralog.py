#!/usr/bin/env python3
import sys
import os
import platform
import requests
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from colorama import init, Fore

init(autoreset=True)

def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def banner():
    print(Fore.MAGENTA + r"""
                   _             __    ___  ___ 
  /\  /\_   _  __| |_ __ __ _  / /   /___\/ _ \
 / /_/ / | | |/ _` | '__/ _` |/ /   //  // /_\/
/ __  /| |_| | (_| | | | (_| / /___/ \_// /_\\ 
\/ /_/  \__, |\__,_|_|  \__,_\____/\___/\____/ 
        |___/ 
""" + Fore.CYAN + "                                              v. 1.2.4\n" + Fore.RESET)
    print(Fore.BLUE + "Created by: " + Fore.GREEN + "znyvx" + Fore.RESET)

def get_ip_info(ip):
    print(Fore.YELLOW + f"\n[+] Checking IP: {ip}")
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=10)
        data = response.json()
        
        print(Fore.GREEN + "\n" + "="*50)
        print(Fore.CYAN + "IP INFORMATION")
        print(Fore.GREEN + "="*50)
        print(Fore.WHITE + f"  IP: {Fore.YELLOW}{data.get('ip', 'Unknown')}")
        print(Fore.WHITE + f"  City: {Fore.YELLOW}{data.get('city', 'Unknown')}")
        print(Fore.WHITE + f"  Region: {Fore.YELLOW}{data.get('region', 'Unknown')}")
        print(Fore.WHITE + f"  Country: {Fore.YELLOW}{data.get('country', 'Unknown')}")
        print(Fore.WHITE + f"  Location: {Fore.YELLOW}{data.get('loc', 'Unknown')}")
        print(Fore.WHITE + f"  ISP: {Fore.YELLOW}{data.get('org', 'Unknown')}")
        print(Fore.WHITE + f"  Timezone: {Fore.YELLOW}{data.get('timezone', 'Unknown')}")
        
        if 'loc' in data:
            lat, lon = data['loc'].split(',')
            print(Fore.BLUE + f"\n  Maps: https://www.google.com/maps?q={lat},{lon}")
        
        print(Fore.GREEN + "="*50 + "\n")
    except Exception as e:
        print(Fore.RED + f"\n[!] Error: {e}\n")

def get_my_ip():
    try:
        response = requests.get("https://ipinfo.io/json", timeout=10)
        data = response.json()
        my_ip = data.get('ip', 'Unknown')
        print(Fore.GREEN + f"\n[+] Your IP: {Fore.YELLOW}{my_ip}\n")
        return my_ip
    except Exception as e:
        print(Fore.RED + f"\n[!] Error: {e}\n")
        return None

def get_phone_info(phone_number):
    print(Fore.YELLOW + f"\n[+] Checking phone: {phone_number}")
    try:
        if not phone_number.startswith('+'):
            phone_number = '+' + phone_number
        
        parsed = phonenumbers.parse(phone_number, None)
        
        print(Fore.GREEN + "\n" + "="*50)
        print(Fore.CYAN + "PHONE INFORMATION")
        print(Fore.GREEN + "="*50)
        print(Fore.WHITE + f"  Number: {Fore.YELLOW}{phone_number}")
        print(Fore.WHITE + f"  Country: {Fore.YELLOW}{geocoder.description_for_number(parsed, 'en')}")
        print(Fore.WHITE + f"  Carrier: {Fore.YELLOW}{carrier.name_for_number(parsed, 'en')}")
        print(Fore.WHITE + f"  Timezone: {Fore.YELLOW}{', '.join(timezone.time_zones_for_number(parsed))}")
        
        if phonenumbers.number_type(parsed) == 1:
            phone_type = "Mobile"
        elif phonenumbers.number_type(parsed) == 0:
            phone_type = "Fixed Line"
        else:
            phone_type = "Other"
        
        print(Fore.WHITE + f"  Type: {Fore.YELLOW}{phone_type}")
        print(Fore.WHITE + f"  Valid: {Fore.YELLOW}{phonenumbers.is_valid_number(parsed)}")
        print(Fore.GREEN + "="*50 + "\n")
        
    except Exception as e:
        print(Fore.RED + f"\n[!] Invalid number or error: {e}\n")

def menu():
    print(Fore.CYAN + "\n┌─────────────────────────────────┐")
    print(Fore.CYAN + "│" + Fore.YELLOW + "         MAIN MENU               " + Fore.CYAN + "│")
    print(Fore.CYAN + "├─────────────────────────────────┤")
    print(Fore.CYAN + "│  " + Fore.GREEN + "[1]" + Fore.WHITE + "  IP Information              " + Fore.CYAN + "│")
    print(Fore.CYAN + "│  " + Fore.GREEN + "[2]" + Fore.WHITE + "  Phone Number Information    " + Fore.CYAN + "│")
    print(Fore.CYAN + "│  " + Fore.GREEN + "[3]" + Fore.WHITE + "  My Own IP                   " + Fore.CYAN + "│")
    print(Fore.CYAN + "│  " + Fore.RED + "[0]" + Fore.WHITE + "  Exit                        " + Fore.CYAN + "│")
    print(Fore.CYAN + "└─────────────────────────────────┘" + Fore.RESET)

def main():
    while True:
        clear()
        banner()
        menu()
        choice = input(Fore.CYAN + "\n┌─[" + Fore.GREEN + "HydraLOG" + Fore.CYAN + "]\n└──╼ " + Fore.WHITE + "$ " + Fore.RESET)
        
        if choice == "1":
            ip = input(Fore.WHITE + "[+] Enter IP: " + Fore.RESET)
            get_ip_info(ip)
            input(Fore.CYAN + "Press Enter..." + Fore.RESET)
        elif choice == "2":
            phone = input(Fore.WHITE + "[+] Enter phone (e.g., 48123456789): " + Fore.RESET)
            get_phone_info(phone)
            input(Fore.CYAN + "Press Enter..." + Fore.RESET)
        elif choice == "3":
            get_my_ip()
            input(Fore.CYAN + "Press Enter..." + Fore.RESET)
        elif choice == "0":
            print(Fore.RED + "\n[!] Closing..." + Fore.RESET)
            sys.exit(0)
        else:
            print(Fore.RED + "\n[!] Invalid choice!" + Fore.RESET)
            input(Fore.CYAN + "Press Enter..." + Fore.RESET)

if __name__ == "__main__":
    main()
