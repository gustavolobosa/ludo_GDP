from colorama import Fore, Style
from ficha import Ficha

class UI:
    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)
    
    @staticmethod
    def mostrar_jugador(jugador):
        print(jugador.nombre + " - " + jugador.color)
        
    @staticmethod
    def mostrar_fichas_jugador(jugador):
        for ficha in jugador.fichas:
            print(ficha.color,"Libre:",ficha.libre ,"Coronada:",ficha.coronada, "posicion relativa:", ficha.posicion_relativa, "posicion absoluta:", ficha.posicion_absoluta)
        
    
    @staticmethod
    def mostrar_tablero(tablero):
                
        for casilla in range(len(tablero.casillas_generales)):
            
            if casilla == 0 or (casilla >= 3 and casilla <= 7) or (casilla >= 21 and casilla <= 26):
                print(" "*17, end="")
                
            if casilla < 2:
                
                if tablero.casillas_generales[casilla]:
                    print(f"|{Ficha.pr_color(str(tablero.casillas_generales[casilla].color))}"+str(tablero.casillas_generales[casilla].color), end=f"{Style.RESET_ALL}|")
                else:
                    print("| |", end="") 
            
            elif casilla == 2:
                if tablero.casillas_generales[casilla]:
                    print(f"|{Ficha.pr_color(str(tablero.casillas_generales[casilla].color))}"+str(tablero.casillas_generales[casilla].color)+f"{Style.RESET_ALL}|")
                else:
                    print("| |") 
                    
            elif casilla > 2 and casilla < 8:
                if tablero.casillas_generales[51-(casilla-3)] and tablero.casillas_generales[casilla]:
                    print(f"|{Ficha.pr_color(str(tablero.casillas_generales[51-(casilla-3)].color))}"+str(tablero.casillas_generales[51-(casilla-3)].color)+f"{Style.RESET_ALL}|| ||{Ficha.pr_color(str(tablero.casillas_generales[casilla].color))}"+str(tablero.casillas_generales[casilla].color)+f"{Style.RESET_ALL}|")
                elif tablero.casillas_generales[51-(casilla-3)]: 
                    print(f"|{Ficha.pr_color(str(tablero.casillas_generales[51-(casilla-3)].color))}"+str(tablero.casillas_generales[51-(casilla-3)].color)+f"{Style.RESET_ALL}|| || |")
                elif tablero.casillas_generales[casilla]:
                    print(f"| || ||{Ficha.pr_color(str(tablero.casillas_generales[casilla].color))}"+str(tablero.casillas_generales[casilla].color)+f"{Style.RESET_ALL}|")
                else:
                    print("| || || |")
                
            elif casilla == 8:
                
                for c in range(41, 47):
                    if tablero.casillas_generales[c]:
                        print(f"|{Ficha.pr_color(tablero.casillas_generales[c].color)}"+str(tablero.casillas_generales[c].color), end=f"{Style.RESET_ALL}|")
                    else:
                        print("| |", end="")
                        
                if tablero.casillas_generales[casilla]:
                    print(f"       |{Ficha.pr_color(tablero.casillas_generales[casilla].color)}"+str(tablero.casillas_generales[casilla].color)+f"{Style.RESET_ALL}|", end="")
                else:
                    print("       | |", end="")
                    
            elif (casilla > 8 and casilla < 14):
                if tablero.casillas_generales[casilla]:
                    print(f"|{Ficha.pr_color(tablero.casillas_generales[casilla].color)}"+str(tablero.casillas_generales[casilla].color)+f"{Style.RESET_ALL}|", end="")
                else:
                    print("| |", end="") 
                    
                if casilla == 13:
                    print()
            
            elif casilla == 14:
                if tablero.casillas_generales[casilla] and tablero.casillas_generales[40]:
                    print(f"|{Ficha.pr_color(tablero.casillas_generales[40].color)}"+str(tablero.casillas_generales[40].color)+f"{Style.RESET_ALL}|"+" "*37+f"|{Ficha.pr_color(tablero.casillas_generales[casilla].color)}"+str(tablero.casillas_generales[casilla].color)+f"{Style.RESET_ALL}|")
                elif tablero.casillas_generales[40]:
                    print(f"|{Ficha.pr_color(tablero.casillas_generales[40].color)}"+str(tablero.casillas_generales[40].color)+f"{Style.RESET_ALL}|"+" "*37+"| |")
                elif tablero.casillas_generales[casilla]:
                    print("| |"+" "*37+f"|{Ficha.pr_color(tablero.casillas_generales[casilla].color)}"+str(tablero.casillas_generales[casilla].color)+f"{Style.RESET_ALL}|")
                else:
                    print("| |"+" "*37+"| |")
                    
                for c in range(39, 33, -1):
                    if tablero.casillas_generales[c]:
                        print(f"|{Ficha.pr_color(tablero.casillas_generales[c].color)}"+str(tablero.casillas_generales[c].color), end=f"{Style.RESET_ALL}|")
                    else:
                        print("| |", end="")
                        
                if tablero.casillas_generales[20]:
                    print(f"       |{Ficha.pr_color(tablero.casillas_generales[20].color)}"+str(tablero.casillas_generales[20].color)+f"{Style.RESET_ALL}|", end="")
                else:
                    print("       | |", end="")
                    
                for c in range(19, 14, -1):
                    if tablero.casillas_generales[c]:
                        print(f"|{Ficha.pr_color(tablero.casillas_generales[c].color)}"+str(tablero.casillas_generales[c].color), end=f"{Style.RESET_ALL}|")
                    else:
                        print("| |", end="")
                print()
                    
            elif casilla > 20 and casilla < 26:
                
                if tablero.casillas_generales[33-(casilla-21)] and tablero.casillas_generales[casilla]:
                    print(f"|{Ficha.pr_color(tablero.casillas_generales[33-(casilla-21)].color)}"+str(tablero.casillas_generales[33-(casilla-21)].color)+f"{Style.RESET_ALL}|| ||{Ficha.pr_color(tablero.casillas_generales[casilla].color)}"+str(tablero.casillas_generales[casilla].color)+f"{Style.RESET_ALL}|")
                elif tablero.casillas_generales[33-(casilla-21)]:
                    print(f"|{Ficha.pr_color(tablero.casillas_generales[33-(casilla-21)].color)}"+str(tablero.casillas_generales[33-(casilla-21)].color)+f"{Style.RESET_ALL}|| || |")
                elif tablero.casillas_generales[casilla]:
                    print(f"| || ||{Ficha.pr_color(tablero.casillas_generales[casilla].color)}"+str(tablero.casillas_generales[casilla].color)+f"{Style.RESET_ALL}|")
                else:
                    print("| || || |")
                    
            elif casilla >= 26 and casilla <= 28:
                
                if tablero.casillas_generales[28-(casilla-26)]:
                    print(f"|{Ficha.pr_color(tablero.casillas_generales[28-(casilla-26)].color)}"+str(tablero.casillas_generales[28-(casilla-26)].color), end=f"{Style.RESET_ALL}|")
                else:
                    print("| |", end="") 
                    
                if casilla == 28:
                    print()
            

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
        var = Fore.RED
        var2 =  Style.RESET_ALL
        print(f"Este es un texto roj")
        print(f"Este es {Fore.RED}un{Style.RESET_ALL} texto rojo")
        
        print(52%52)