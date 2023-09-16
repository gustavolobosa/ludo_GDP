from ficha import Ficha

class Tablero:
    def __init__(self):
        self.casillas_generales = [None] * 52
        self.casillas_rojas = [None] * 6
        self.casillas_verdes = [None] * 6
        self.casillas_azules = [None] * 6   
        self.casillas_amarillas = [None] * 6

    def agregar_ficha(self, ficha, posicion):
        self.casillas_generales[posicion] = ficha

    def quitar_ficha(self, posicion):
        ficha = self.casillas_generales[posicion]
        self.casillas_generales[posicion] = None
        return ficha

    