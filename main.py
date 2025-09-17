import os
import ctypes
from SCR.start import start
os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW('Bonsai - Email Bomber')
start()

