import os
from os import system
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import colorama
from colorama import Fore

title = f'Email Generator'
system(f'title {title}')
clear = lambda: os.system('cls')
clear()
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.minimize_window()
driver.get("https://www.emailnator.com/")
search_aa = driver.find_element(By.CLASS_NAME, "btn")
search_aa.click()
search_VV = driver.find_element(By.NAME, "copy")
search_VV.click()
page = driver.current_url
clear()
sourceFile = open('email.txt', 'w')
print(f'you can have only save one email in his file ! \n\nemail : {page}', file = sourceFile)
sourceFile.close()
print(f"\nYour new email address has been saved in email.txt")
print(f"\n New Email : {page} \n\n this CMD will close in 10 seconds")
driver.close()
time.sleep(10)