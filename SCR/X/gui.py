from colorama import Fore
import os
import ctypes
from pystyle import Colors, Colorate, Write
def gui():
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW('Bonsai - Email Bomber')

    filename="email.txt"
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    num_emails = len(lines)


    Write.Print(f"""
        ,.,
        MMMM_    ,..,                                
            "_ "__"MMMMM          ,...,,             Email: {num_emails}
    ,..., __." --"    ,.,     _-"MMMMMMM             [1]Email Bomber
    MMMMMM"___ "_._   MMM"_."" _                     [2]Info
        "" , \_.   "_. ."     MMMMMMM                [3]Credits
            ,., _"__ \__./ ."                        [4]Exit
        MMMMM_"  "_    ./
            ''''      (    )                         
    ._______________.-'____"---._.
    \                          /
    \________________________/
    (_)                    (_)
    """, Colors.green, interval=0.001)