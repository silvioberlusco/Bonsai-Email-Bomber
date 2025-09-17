from .X.gui import gui
from .X.bomber import bomber
from .X.starter_gui import agui
from pystyle import Colors, Colorate, Write
from .X.info import bgui
from .X.credits import cgui
def start():
    agui()
    def nstart():
        gui()
        x = int(input(Colors.green + "option> " + Colors.reset))
        if x == 1:
            bomber()
            input(Colors.green + "\nPremi invio per tornare al menu principale..." + Colors.reset)
            nstart()           
        elif x == 2:
            bgui()
            input(Colors.green + "\nPremi invio per tornare al menu principale..." + Colors.reset)
            nstart()
        elif x == 3:
            cgui()
            input(Colors.green + "\nPremi invio per tornare al menu principale..." + Colors.reset)
            nstart()
        elif x == 4:
            exit()
        else:
            Write.Print("Opzione non valida!\n", Colors.green, interval=0.01)
            input(Colors.green + "\nPremi invio per tornare al menu principale..." + Colors.reset)
            nstart()
    nstart()
