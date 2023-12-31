from ficha import Ficha
from jugador import Jugador 
from tablero import Tablero 
from ui import UI
import random
import keyboard

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
            self.jugadores.append(Jugador("jugador"+str(i+1)+self.colores[i], self.colores[i]))  
            
            for _ in range(3):
                self.jugadores[i].fichas.append(Ficha(self.jugadores[i].color, i*13+3))
            
    
    # Buscar jugador que parte
    def encontrar_jugador_inicial(self):
        dado_mayor = 0
        index_starting_player = 0
        casos = []
        
        for jugador in self.jugadores:
                dado = jugador.lanzar_dado()
                if dado > dado_mayor:
                        starting_player = jugador
                        index_starting_player = self.jugadores.index(starting_player)
                        dado_mayor = dado
                        casos = []
                        casos.append(jugador)
                elif dado == dado_mayor:
                        casos.append(jugador)
        while len(casos) > 1:
            casos1 = []
            for jugador in casos:
                dado = jugador.lanzar_dado()
                if dado > dado_mayor:
                        starting_player = jugador
                        index_starting_player = self.jugadores.index(starting_player)
                        dado_mayor = dado
                        casos1 = []
                        casos1.append(jugador)
                elif dado == dado_mayor:
                        casos1.append(jugador)
            casos = casos1
        UI.mostrar_mensaje(f"{starting_player.nombre} comenzara la partida")
        UI.mostrar_linea()
        
        return index_starting_player
    

    def definir_cantidad_jugadores(self):
        
        while self.cantidad_jugadores == 0:
                cantidad_jugadores = input("¿Cuántos jugadores van a jugar?: ")
                
                try:
                        self.cantidad_jugadores = int(cantidad_jugadores)
                        if self.cantidad_jugadores < 2 or self.cantidad_jugadores > 4:
                                self.cantidad_jugadores = 0
                                print("Ingrese un número válido entre 2 y 4")
                except:
                        cantidad_jugadores = 0
                        print("Ingrese un número válido entre 2 y 4")
                
                UI.mostrar_linea()
                
    # def posicionar_fichas(self, jugador):
    #     for i in range(self.cantidad_jugadores):
    #         self.jugadores[i].fichas[0]
    #         self.tablero.agregar_ficha(self.jugadores[i].fichas[0])
            
    #     UI.mostrar_tablero(self.tablero)
        
    def mover_ficha(self, jugador, ficha, casillas):
        
        self.tablero.quitar_ficha(ficha)

        ficha.posicion_relativa = (ficha.posicion_relativa + casillas) % 52
        ficha.posicion_absoluta = ficha.posicion_absoluta + casillas

        
        if self.verificar_ganador():
            return True

        self.tablero.agregar_ficha(ficha)

        if self.verificar_ganador():
            return True
        # UI.mostrar_fichas_jugador(jugador)
    
    def verificar_ganador(self):
        for jugador in self.jugadores:
            if jugador.verificar_victoria():
                UI.mostrar_mensaje(f"{jugador.nombre} ha ganado")
                return True
                
        return False

    def play(self, index_jugador_inicial):
        UI.mostrar_mensaje("Jugando...")
        UI.mostrar_linea()
        UI.mostrar_tablero(self.tablero)
        turno = index_jugador_inicial
    
        while True:
            input("Presione enter para continuar")
            casillas = self.jugadores[turno].lanzar_dado()
            if self.jugadores[turno].todas_ficha_en_casa():
                if casillas == 1 or casillas == 6:
                    ficha = self.jugadores[turno].siguente_ficha_libre()
                    self.tablero.agregar_ficha(ficha)
                    ficha.liberar()
                    UI.mostrar_mensaje(f"{self.jugadores[turno].nombre} ha sacado un {casillas} y ha liberado una ficha")
                    
            elif self.jugadores[turno].ninguna_fichas_en_casa():
                if self.mover_ficha(self.jugadores[turno], self.jugadores[turno].ficha_a_mover(), casillas):
                    return True
            else:
                if casillas == 1 or casillas == 6:
                     if self.tablero.verificar_casilla_salida(self.jugadores[turno]):
                        ficha = self.jugadores[turno].siguente_ficha_libre()
                        self.tablero.agregar_ficha(ficha)
                        ficha.liberar()
                        UI.mostrar_mensaje(f"{self.jugadores[turno].nombre} ha liberado una ficha")
                   
                if self.mover_ficha(self.jugadores[turno], self.jugadores[turno].ficha_a_mover(), casillas):
                    return True
                
            UI.mostrar_tablero(self.tablero)
            turno += 1
            turno = turno % self.cantidad_jugadores
            
    
    def start(self):
        UI.mostrar_titulo()
        UI.mostrar_linea()
        
        self.definir_cantidad_jugadores()
        self.crear_jugadores()
        #self.posicionar_fichas()
        index_jugador_inicial = self.encontrar_jugador_inicial()
        
        
        self.play(index_jugador_inicial)
        

if __name__ == "__main__":
    game = Game()
    game.start()
