from ficha import Ficha
from jugador import Jugador 
from tablero import Tablero 
from ui import UI

# Crear jugadores y tablero
jugador1 = Jugador("Jugador 1", "Rojo")
jugador2 = Jugador("Jugador 2", "Verde")
tablero = Tablero()

# Agregar fichas al tablero al inicio del juego
tablero.agregar_ficha(Ficha("R"), 0)
tablero.agregar_ficha(Ficha("V"), 1)
tablero.agregar_ficha(Ficha("A"), 2)
tablero.agregar_ficha(Ficha("M"), 3)
tablero.agregar_ficha(Ficha("R"), 4)
tablero.agregar_ficha(Ficha("V"), 5)
tablero.agregar_ficha(Ficha("A"), 6)
tablero.agregar_ficha(Ficha("M"), 7)

tablero.agregar_ficha(Ficha("R"), 51)
tablero.agregar_ficha(Ficha("V"), 50)
tablero.agregar_ficha(Ficha("A"), 49)
tablero.agregar_ficha(Ficha("M"), 48)
tablero.agregar_ficha(Ficha("R"), 47)

# ... (agregar el resto de las fichas iniciales)

UI.mostrar_tablero(tablero)

# Empezar el juego
# while True:
#     for jugador in [jugador1, jugador2]:
#         input(f"Presiona Enter para que {jugador.nombre} juegue.")
#         jugador.realizar_movida()

        # Aquí deberías agregar la lógica para mover las fichas según el dado

        # Mostrar el estado actual del tablero
        # tablero.mostrar_tablero()

        # Verificar si hay un ganador y terminar el juego si lo hay
