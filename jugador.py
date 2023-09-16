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
