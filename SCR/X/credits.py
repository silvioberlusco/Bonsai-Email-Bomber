from colorama import Fore
import os
import ctypes
from pystyle import Colors, Colorate, Write
import shutil
def _center_top(s):
    cols, rows = shutil.get_terminal_size(fallback=(80,24))
    lines = s.splitlines()
    out = []
    for L in lines:
        pad = max((cols - len(L)) // 2, 0)
        out.append(' ' * pad + L)
    return '\n'.join(out)

b= r"""
 ____   ___  _   _ ____    _    ___   ____   ___  __  __ ____  _____ ____  
| __ ) / _ \| \ | / ___|  / \  |_ _| | __ ) / _ \|  \/  | __ )| ____|  _ \ 
|  _ \| | | |  \| \___ \ / _ \  | |  |  _ \| | | | |\/| |  _ \|  _| | |_) |
| |_) | |_| | |\  |___) / ___ \ | |  | |_) | |_| | |  | | |_) | |___|  _ < 
|____/ \___/|_| \_|____/_/   \_\___| |____/ \___/|_|  |_|____/|_____|_| \_\
"""
a = """
Bonsai - Email Bomber
Versione 1.0
Developed by _wao__ (ds)
"""
def cgui():
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW('Bonsai - Email Bomber')
    print(Colors.green + _center_top(b))
    Write.Print(a, Colors.green, interval=0.0001)