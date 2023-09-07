from colorama import Fore, Style

class UI:
    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)
    
    @staticmethod
    def mostrar_jugador(jugador):
        print(jugador)
    
    @staticmethod
    def mostrar_tablero(tablero):
       
        for casilla in range(len(tablero.casillas_generales)):
            
            if casilla < 2:
                
                if tablero.casillas_generales[casilla]:
                    print("|"+tablero.casillas_generales[casilla].color, end="|")
                else:
                    print("| |", end="") 
            
            elif casilla == 2:
                if tablero.casillas_generales[casilla]:
                    print("|"+tablero.casillas_generales[casilla].color+"|")
                else:
                    print("| |") 
                    
            elif casilla > 2 and casilla < 8:
                if tablero.casillas_generales[casilla]:
                    print("|"+tablero.casillas_generales[51-(casilla-3)].color+"|| ||"+tablero.casillas_generales[casilla].color+"|")
                else:
                    print("| || || |")
                
            elif casilla == 8:
                
                for c in range(41, 47):
                    if tablero.casillas_generales[c]:
                        print("|"+tablero.casillas_generales[c].color, end="|")
                    else:
                        print("| |", end="")
                        
                if tablero.casillas_generales[casilla]:
                    print("      |"+tablero.casillas_generales[casilla].color+"|", end="")
                else:
                    print("      | |", end="")
                    
            elif casilla > 8 and casilla < 14:
                if tablero.casillas_generales[casilla]:
                    print("|"+tablero.casillas_generales[51-(casilla-3)].color+"||"+tablero.casillas_generales[casilla].color+"|")
                else:
                    print("| |", end="") 
                    
            
                
            

    def mostrar_titulo():
        print('''
         _                                 
        | |                              
        | |     _   _  _ _   ___  
        | |   _| | | |  _ \ / _ \
        | |__| | |_| | |_) | (_) |
        |_____/ \___/|_ _ / \___/         
              \n''')
        
    def mostrar_linea():
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        
    def test():
        # Imprimir texto rojo
        print(f"{Fore.RED}Este es un texto rojo{Style.RESET_ALL}")