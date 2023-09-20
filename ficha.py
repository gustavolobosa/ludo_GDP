
from colorama import Fore


class Ficha:
    def __init__(self, color, posicion_relativa, posicion_absoluta=0):
        self.color = color
        self.libre = False  # Si la ficha está en la cárcel
        self.meta = False
        self.coronada = False
        self.posicion_salia = posicion_relativa
        self.posicion_relativa = posicion_relativa
        self.posicion_absoluta = posicion_absoluta
    def __str__(self):
        #print the class like a dict
        return str(self.__dict__)

    def encarcelar(self):
        self.libre = False
        self.posicion_relativa = self.posicion_salia
        self.posicion_absoluta = 0
    
    def en_meta(self):
        self.meta = True
        
    def coronar(self):
        self.coronada = True
    
    def liberar(self):
        self.libre = True
        
    def pr_color(c):
        if c == "R":
            return Fore.RED
        elif c == "V":
            return Fore.GREEN
        elif c == "A":
            return Fore.BLUE
        elif c == "M":
            return Fore.YELLOW
