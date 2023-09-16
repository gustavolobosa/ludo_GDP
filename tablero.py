from ficha import Ficha

class Tablero:
    def __init__(self):
        self.casillas_generales = [None] * 52  
        self.casillas_rojas = [None] * 6
        self.casillas_verdes = [None] * 6
        self.casillas_azules = [None] * 6  
        self.casillas_amarillas = [None] * 6

    def agregar_ficha(self, ficha):
        
        if ficha.posicion_absoluta >= 52:
            posicion = ficha.posicion_absoluta - 52
            
            if ficha.color == "R":
                self.casillas_rojas[posicion] = ficha
            elif ficha.color == "V":
                self.casillas_verdes[posicion] = ficha
            elif ficha.color == "A":
                self.casillas_azules[posicion] = ficha
            elif ficha.color == "M":
                self.casillas_amarillas[posicion] = ficha
        else:
            posicion = ficha.posicion_relativa
            self.casillas_generales[posicion] = ficha

    def quitar_ficha(self, ficha):
                
        if ficha.posicion_absoluta >= 52:
            posicion = ficha.posicion_absoluta - 52
            if ficha.color == "R":
                self.casillas_rojas[posicion] = None
            elif ficha.color == "V":
                self.casillas_verdes[posicion] = None
            elif ficha.color == "A":
                self.casillas_azules[posicion] = None
            elif ficha.color == "M":
                self.casillas_amarillas[posicion] = None
        
        else:
            posicion = ficha.posicion_relativa
            self.casillas_generales[posicion] = None
            

        

    