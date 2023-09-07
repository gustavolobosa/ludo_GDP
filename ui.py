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
            
            if casilla == 0 or (casilla >= 3 and casilla <= 7) or (casilla >= 21 and casilla <= 26):
                print(" "*17, end="")
                
            if casilla < 2:
                
                if tablero.casillas_generales[casilla]:
                    print("|"+str(tablero.casillas_generales[casilla].color), end="|")
                else:
                    print("| |", end="") 
            
            elif casilla == 2:
                if tablero.casillas_generales[casilla]:
                    print("|"+str(tablero.casillas_generales[casilla].color)+"|")
                else:
                    print("| |") 
                    
            elif casilla > 2 and casilla < 8:
                if tablero.casillas_generales[casilla]:
                    print("|"+str(tablero.casillas_generales[51-(casilla-3)].color)+"|| ||"+str(tablero.casillas_generales[casilla].color)+"|")
                else:
                    print("| || || |")
                
            elif casilla == 8:
                
                for c in range(41, 47):
                    if tablero.casillas_generales[c]:
                        print("|"+str(tablero.casillas_generales[c].color), end="|")
                    else:
                        print("| |", end="")
                        
                if tablero.casillas_generales[casilla]:
                    print("       |"+str(tablero.casillas_generales[casilla].color)+"|", end="")
                else:
                    print("       | |", end="")
                    
            elif (casilla > 8 and casilla < 14):
                if tablero.casillas_generales[casilla]:
                    print("|"+str(tablero.casillas_generales[casilla].color)+"|", end="")
                else:
                    print("| |", end="") 
                    
                if casilla == 13:
                    print()
            
            elif casilla == 14:
                if tablero.casillas_generales[casilla]:
                    print("|"+str(tablero.casillas_generales[40].color)+"|"+" "*37+"|"+str(tablero.casillas_generales[casilla].color)+"|")
                else:
                    print("| |"+" "*37+"| |")
                    
                for c in range(39, 33, -1):
                    if tablero.casillas_generales[c]:
                        print("|"+str(tablero.casillas_generales[c].color), end="|")
                    else:
                        print("| |", end="")
                        
                if tablero.casillas_generales[20]:
                    print("       |"+str(tablero.casillas_generales[20].color)+"|", end="")
                else:
                    print("       | |", end="")
                    
                for c in range(19, 14, -1):
                    if tablero.casillas_generales[c]:
                        print("|"+str(tablero.casillas_generales[c].color), end="|")
                    else:
                        print("| |", end="")
                print()
                    
            elif casilla > 20 and casilla < 26:
                
                if tablero.casillas_generales[casilla]:
                    print("|"+str(tablero.casillas_generales[33-(casilla-21)].color)+"|| ||"+str(tablero.casillas_generales[casilla].color)+"|")
                else:
                    print("| || || |")
                    
            elif casilla >= 26 and casilla <= 28:
                
                if tablero.casillas_generales[casilla]:
                    print("|"+str(tablero.casillas_generales[28-(casilla-26)].color), end="|")
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