class Tablero:
    def __init__(self):
        self.emojis = {
            'R': '🟥',
            'G': '🟩',
            'Y': '🟨',
            'B': '🟦',
            'W': '⬜',
        }
        self.tablero = self.crear_tablero()

    def crear_tablero(self):
        # Define las letras para cada tipo de cuadrado
        tablero = [
            ['G', 'G', 'G', 'G', 'G', 'G', 'W', 'W', 'W', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['G', 'W', 'W', 'W', 'W', 'G', 'W', 'R', 'R', 'R', 'W', 'W', 'W', 'W', 'R'],
            ['G', 'W', ' ', ' ', 'W', 'G', 'W', 'R', 'W', 'R', 'W', ' ', ' ', 'W', 'R'],
            ['G', 'W', ' ', ' ', 'W', 'G', 'W', 'R', 'W', 'R', 'W', ' ', ' ', 'W', 'R'],
            ['G', 'W', 'W', 'W', 'W', 'G', 'W', 'R', 'W', 'R', 'W', 'W', 'W', 'W', 'R'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'W', 'R', 'W', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['W', 'G', 'W', 'W', 'W', 'W', ' ', 'R', ' ', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'G', 'G', 'G', 'G', 'G', 'G', ' ', 'B', 'B', 'B', 'B', 'B', 'B', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', ' ', 'Y', ' ', 'W', 'W', 'W', 'W', 'B', 'W'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'W', 'Y', 'W', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['Y', 'W', 'W', 'W', 'W', 'Y', 'W', 'Y', 'W', 'B', 'W', 'W', 'W', 'W', 'B'],
            ['Y', 'W', ' ', ' ', 'W', 'Y', 'W', 'Y', 'W', 'B', 'W', ' ', ' ', 'W', 'B'],
            ['Y', 'W', ' ', ' ', 'W', 'Y', 'W', 'Y', 'W', 'B', 'W', ' ', ' ', 'W', 'B'],
            ['Y', 'W', 'W', 'W', 'W', 'Y', 'Y', 'Y', 'W', 'B', 'W', 'W', 'W', 'W', 'B'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'W', 'W', 'W', 'B', 'B', 'B', 'B', 'B', 'B'],
        ]
        return tablero

    def imprimir_tablero(self):
        for fila in self.tablero:
            for cuadro in fila:
                emoji = self.emojis.get(cuadro, '  ')
                print(emoji, end=' ')
            print()  # Nueva línea después de cada fila

if __name__ == "__main__":
    tablero = Tablero()
    tablero.imprimir_tablero()
