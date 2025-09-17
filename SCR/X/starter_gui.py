from colorama import Fore
import os
import ctypes
from pystyle import Colors, Colorate, Write
import os
import time
import keyboard
import shutil 
a = r"""
 /$$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$      
| $$__  $$ /$$__  $$| $$$ | $$ /$$__  $$ /$$__  $$|_  $$_/      
| $$  \ $$| $$  \ $$| $$$$| $$| $$  \__/| $$  \ $$  | $$        
| $$$$$$$ | $$  | $$| $$ $$ $$|  $$$$$$ | $$$$$$$$  | $$        
| $$__  $$| $$  | $$| $$  $$$$ \____  $$| $$__  $$  | $$        
| $$  \ $$| $$  | $$| $$\  $$$ /$$  \ $$| $$  | $$  | $$        
| $$$$$$$/|  $$$$$$/| $$ \  $$|  $$$$$$/| $$  | $$ /$$$$$$      
|_______/  \______/ |__/  \__/ \______/ |__/  |__/|______/      
                                                           
Premi spazio per continuare...
"""
b = r"""
 /$$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
| $$__  $$ /$$__  $$| $$$    /$$$| $$__  $$| $$_____/| $$__  $$
| $$  \ $$| $$  \ $$| $$$$  /$$$$| $$  \ $$| $$      | $$  \ $$
| $$$$$$$ | $$  | $$| $$ $$/$$ $$| $$$$$$$ | $$$$$   | $$$$$$$/
| $$__  $$| $$  | $$| $$  $$$| $$| $$__  $$| $$__/   | $$__  $$
| $$  \ $$| $$  | $$| $$\  $ | $$| $$  \ $$| $$      | $$  \ $$
| $$$$$$$/|  $$$$$$/| $$ \/  | $$| $$$$$$$/| $$$$$$$$| $$  | $$
|_______/  \______/ |__/     |__/|_______/ |________/|__/  |__/ 

Premi spazio per continuare...
""" 
def _center(s):
    cols, rows = shutil.get_terminal_size(fallback=(80,24))
    lines = s.splitlines()
    top = max((rows - len(lines))//2,0)
    out = ['']*top
    for L in lines:
        pad = max((cols - len(L))//2,0)
        out.append(' '*pad + L)
    return '\n'.join(out)
def agui():
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW('Bonsai - Email Bomber')
    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(Colors.green + _center(a))
            time.sleep(0.2)
            if keyboard.is_pressed("space"):
                break
            os.system("cls" if os.name == "nt" else "clear")
            print(Colors.green + _center(b))
            time.sleep(0.2)
            if keyboard.is_pressed("space"):
                break
    except KeyboardInterrupt:
        pass
    os.system("cls" if os.name == "nt" else "clear")