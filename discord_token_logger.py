import os
from os import system
import time
try:
    import colorama
    from colorama import Fore
except:
    os.system('pip install colorama')
    import colorama
    from colorama import Fore
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver import ActionChains
    from os import startfile
except:
    os.system('pip install selenium')
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver import ActionChains
    from os import startfile

title = f'Token Loggin'
system(f'title {title}')
clear = lambda: os.system('cls')
clear()
sss = input(f"T0KEN : ")
aaa = input(f"\nDo you want a tutorial on how to connect to an account only with the token? (y/n) : ")
if aaa == 'y':
    os.startfile("tutorial token login.mp4")
    print(f"{Fore.GREEN}click on F12 go to console then paste your token login text and press Enter the two possibilities either you will be connected to the account or it will put you back to the login page if you are back to the login page this is due to the fact that you are already connected to this account on this computer (specifically with this web browser or chrome user) I also take the opportunity to tell you that from the moment you log out you will not be able to reconnect only with the token of the account unless you change chrome user or web browser")
    fff = input(f"{Fore.CYAN}\n press entrer to continue ")

elif aaa =='n':
    print()
else:
    print(f" '{aaa}' do not have a possible answer")
    time.sleep(2)

print(f"here is your token loggin text copy it before the browser window open ! (or she crash)")
print('''
function login(token) {
setInterval(() => {
document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
}, 50);
setTimeout(() => {
location.reload();
}, 2500);
}''')
print(f'''login('{sss}');
''')
time.sleep(4)
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.set_window_position(1305,-1)
driver.get("https://discord.com/login")
print(f"\nIf you close this cmd window the web browser will close too so if you want to choose other possibilities you have to be sure that you don't want the web browser anymore{Fore.RESET}")
time.sleep(999999)
driver.quit()