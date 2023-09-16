from ficha import Ficha
from jugador import Jugador 
from tablero import Tablero 
from ui import UI
import random

class Game:
    # Creación del juego
    def __init__(self):
        self.jugadores = []
        self.cantidad_jugadores = 0
        self.tablero = Tablero()
        self.colores = ["R", "V", "A", "M"]
    
    # Repartir fichas
    def crear_jugadores(self):
        for i in range(self.cantidad_jugadores):
                self.jugadores.append(Jugador("jugador"+str(i+1), self.colores[i]))  
        
        for j in range(4):
            self.jugadores[i].fichas.append(Ficha(self.colores[i]))    
            
        for jugador in self.jugadores:
                UI.mostrar_jugador(jugador)
                UI.mostrar_fichas_jugador(jugador)
    
    # Buscar jugador que parte
    def encontrar_jugador_inicial(self):
        starting_player = self.jugadores[0]
        dado_mayor = starting_player.lanzar_dado()
        
        for jugador in self.jugadores:
                dado = jugador.lanzar_dado()
                UI.mostrar_mensaje(f"{jugador.nombre} lanzó un {dado}")
                if dado > dado_mayor:
                        starting_player = jugador
                        dado_mayor = dado
        UI.mostrar_mensaje(f"{jugador.nombre} comenzara la partida {dado}")
        
        return starting_player

    def definir_cantidad_jugadores(self):
        
        while self.cantidad_jugadores == 0:
                cantidad_jugadores = input("¿Cuántos jugadores van a jugar?: ")
                
                try:
                        self.cantidad_jugadores = int(cantidad_jugadores)
                        if self.cantidad_jugadores < 1 or self.cantidad_jugadores > 4:
                                self.cantidad_jugadores = 0
                                print("Ingrese un número válido entre 1 y 4")
                except:
                        cantidad_jugadores = 0
                        print("Ingrese un número válido entre 1 y 4")

    def play(self, jugador_inicial):
        UI.mostrar_mensaje("Jugando...")
    
    def start(self):
        UI.mostrar_titulo()
        UI.mostrar_linea()
        
        self.definir_cantidad_jugadores()
        self.crear_jugadores()
        jugador_inicial = self.encontrar_jugador_inicial()
        
        self.play(jugador_inicial)
        

if __name__ == "__main__":
    game = Game()
    game.start()
