
from colorama import Fore


class Ficha:
    def __init__(self, color, posicion_relativa, posicion_absoluta=0):
        self.color = color
        self.libre = False  # Si la ficha está en la cárcel
        self.coronada = False
        self.posicion_relativa = posicion_relativa
        self.posicion_absoluta = posicion_absoluta

    def coronar(self):
        self.coronada = True
        
    def pr_color(c):
        if c == "R":
            return Fore.RED
        elif c == "V":
            return Fore.GREEN
        elif c == "A":
            return Fore.BLUE
        elif c == "M":
            return Fore.YELLOW
