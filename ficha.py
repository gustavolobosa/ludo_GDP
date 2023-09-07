
class Ficha:
    def __init__(self, color):
        self.color = color
        self.libre = False  # Si la ficha está en la cárcel
        self.coronada = False

    def coronar(self):
        self.coronada = True
