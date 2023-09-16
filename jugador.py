import random
from ui import UI

class Jugador:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.fichas = []

    def lanzar_dado(self):
        return random.randint(1, 6)
 
    def realizar_movida(self):
        dado = self.lanzar_dado()
        UI.mostrar_mensaje(f"{self.nombre} lanzó un {dado}")

    def mover_ficha(self, ficha, casillas):
        # Verificar si la ficha puede moverse según el valor del dado
        # Realizar el movimiento y actualizar la posición de la ficha en el tablero
        pass