import os
from os import system
dir_path = os.path.dirname(os.path.realpath(__file__))
path = f'''{dir_path}\\pysetup.exe'''
os.system(f'''{path} /passive InstallAllUsers=1 PrependPath=1 Include_test=0''')