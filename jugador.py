import random
from ui import UI

class Jugador:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.fichas = []

    def lanzar_dado(self):
        dado = random.randint(1, 6)
        UI.mostrar_mensaje(f"{self.nombre} lanzó un {dado}")
        return dado
    
    def todas_ficha_en_casa(self):
        for ficha in self.fichas:
            if ficha.libre:
                return False	
        return True
    def ninguna_fichas_en_casa(self):
        for ficha in self.fichas:
            if not ficha.libre:
                return False	
        return True
    def fichas_en_juego(self):
        fichas = []
        for ficha in self.fichas:
            if ficha.libre:
                fichas.append(ficha)
        return fichas

    def ficha_a_mover(self):
        fichas = self.fichas_en_juego()
        index_ficha = random.randint(0, len(fichas)-1)
        return fichas[index_ficha]

    
    def siguente_ficha_libre(self):
        for ficha in self.fichas:
            if ficha.libre:
                return ficha
        return None
    
    def liberar_sino_mover(self):
        probabilidades = random.randint(1, 10)
        if probabilidades <= 8:
            return True
        else:
            return False

            
