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
            
            # imprimir espacios vacios a la izquierda del tablero
            if casilla == 0 or (casilla >= 4 and casilla <= 7) or casilla == 21 or (casilla >=23 and casilla <= 26):
                print(" "*17, end="")
            
            # imprimir fichas no liberadas amarillas
            amarillas_libres = 0
            if casilla == 3:
                print(" "*6, end="")
                
                for ficha in range(len(tablero.casillas_amarillas)):
                    if tablero.casillas_amarillas[ficha] and tablero.casillas_amarillas[ficha].color == "M":
                        if tablero.casillas_amarillas[ficha].libre:
                            amarillas_libres += 1
                            
                for ficha in range(len(tablero.casillas_generales)):
                    if tablero.casillas_generales[ficha] and tablero.casillas_generales[ficha].color == "M":
                        if tablero.casillas_generales[ficha].libre:
                            amarillas_libres += 1
                for p in range(4-amarillas_libres):
                    print(f"{Fore.YELLOW}"+"M ", end=f"{Style.RESET_ALL}")
                    
                for _ in range(amarillas_libres):
                    print(" "*2, end="")

                print(" "*3, end="")
                
            azules_libres = 0
            
            if casilla == 22:
                print(" "*6, end="")
                
                for ficha in range(len(tablero.casillas_azules)):
                    if tablero.casillas_azules[ficha] and tablero.casillas_azules[ficha].color == "A":
                        if tablero.casillas_azules[ficha].libre:
                            azules_libres += 1
                            
                for ficha in range(len(tablero.casillas_generales)):
                    if tablero.casillas_generales[ficha] and tablero.casillas_generales[ficha].color == "A":
                        if tablero.casillas_generales[ficha].libre:
                            azules_libres += 1
                for p in range(4-azules_libres):
                    print(f"{Fore.BLUE}"+"A ", end=f"{Style.RESET_ALL}")
                
                for _ in range(azules_libres):
                    print(" "*2, end="")
                print(" "*3, end="")
                
            # imprimir primeras 3 casillas
            if casilla == 0:
                if tablero.casillas_generales[0]:
                    c1 = f"|{Ficha.pr_color(str(tablero.casillas_generales[0].color))}"+str(tablero.casillas_generales[0].color)+f"{Style.RESET_ALL}|"
                else:
                    c1 = "| |"
                if tablero.casillas_generales[1]:
                    c2 = f"|{Ficha.pr_color(str(tablero.casillas_generales[1].color))}"+str(tablero.casillas_generales[1].color)+f"{Style.RESET_ALL}|"   
                else:
                    c2 = "| |"
                if tablero.casillas_generales[2]:
                    c3 = f"|{Ficha.pr_color(str(tablero.casillas_generales[2].color))}"+str(tablero.casillas_generales[2].color)+f"{Style.RESET_ALL}|"
                else:
                    c3 = "| |"
                    
                print(c1+c2+c3)

            # imprimir resto del ala superior
            elif casilla > 2 and casilla < 8:
                
                if  tablero.casillas_generales[51-(casilla-3)]:
                    c1 = f"|{Ficha.pr_color(str(tablero.casillas_generales[51-(casilla-3)].color))}"+str(tablero.casillas_generales[51-(casilla-3)].color)+f"{Style.RESET_ALL}|"
                else:
                    c1 = "| |"
                if tablero.casillas_rojas[casilla-2]:
                    c2 = f"{Fore.RED}|"+"R"+f"|{Style.RESET_ALL}"
                else:
                    c2 = f"{Fore.RED}|"+" "+f"|{Style.RESET_ALL}"
                if tablero.casillas_generales[casilla]:
                    c3 = f"|{Ficha.pr_color(str(tablero.casillas_generales[casilla].color))}"+str(tablero.casillas_generales[casilla].color)+f"{Style.RESET_ALL}|"
                else:
                    c3 = "| |"
                    
                # caso especial rojo
                if tablero.casillas_rojas[0] and casilla == 3:
                    c3 = f"|{Fore.RED}"+"R"+f"{Style.RESET_ALL}|"
                
                print(c1+c2+c3, end="")
                
                rojas_libres = 0
                if casilla == 3:
                    print(" "*4, end="")
                    
                    for ficha in range(len(tablero.casillas_rojas)):
                        if tablero.casillas_rojas[ficha] and tablero.casillas_rojas[ficha].color == "R":
                            if tablero.casillas_rojas[ficha].libre:
                                rojas_libres += 1
                                
                    for ficha in range(len(tablero.casillas_generales)):
                        if tablero.casillas_generales[ficha] and tablero.casillas_generales[ficha].color == "R":
                            if tablero.casillas_generales[ficha].libre:
                                rojas_libres += 1
                    for p in range(4-rojas_libres):
                        print(f"{Fore.RED}"+"R ", end=f"{Style.RESET_ALL}")
                    
                    for _ in range(rojas_libres):
                        print(" "*2, end="")

                    print(" "*3, end="")

                print()
            # impimir ala izquierda parte superior
            elif casilla == 8:
                for c in range(41, 47):
                    if tablero.casillas_generales[c]:
                        print(f"|{Ficha.pr_color(tablero.casillas_generales[c].color)}"+str(tablero.casillas_generales[c].color), end=f"{Style.RESET_ALL}|")
                    else:
                        print("| |", end="")
                        
                    #caso especial amarillo
                    if tablero.casillas_amarillas[0] and c == 42:
                        print(f"|{Fore.YELLOW}"+"M", end=f"{Style.RESET_ALL}|")
                        
                if tablero.casillas_generales[casilla]:
                    print(f"       |{Ficha.pr_color(tablero.casillas_generales[casilla].color)}"+str(tablero.casillas_generales[casilla].color)+f"{Style.RESET_ALL}|", end="")
                else:
                    print("       | |", end="")
            
            # impirmir ala derecha parte superior
            elif (casilla > 8 and casilla < 14):
                if tablero.casillas_generales[casilla]:
                    print(f"|{Ficha.pr_color(tablero.casillas_generales[casilla].color)}"+str(tablero.casillas_generales[casilla].color)+f"{Style.RESET_ALL}|", end="")
                else:
                    print("| |", end="") 
                  
                if casilla == 13:
                    print()
            
            # imprimir fila de en medio del tablero
            elif casilla == 14:
                
                if tablero.casillas_generales[40]:
                    c1 = f"|{Ficha.pr_color(tablero.casillas_generales[40].color)}"+str(tablero.casillas_generales[40].color)+f"{Style.RESET_ALL}|"
                else:
                    c1 = "| |"
                print(c1, end="")
                
                for i in range(5):
                    if tablero.casillas_amarillas[i+1]:
                        print(f"|{Fore.YELLOW}" + "M", end=f"{Style.RESET_ALL}|")
                    else:
                        print(f"{Fore.YELLOW}|" + " ", end=f"|{Style.RESET_ALL}")
                        
                print("       ", end="")
                
                for i in range(6, 1, -1):
                    if tablero.casillas_verdes[i-1]:
                        print(f"|{Fore.GREEN}" + "V", end=f"{Style.RESET_ALL}|")
                    else:
                        print(f"{Fore.GREEN}|" + " ", end=f"|{Style.RESET_ALL}")

                        
                if tablero.casillas_generales[casilla]:
                    c12 = f"|{Ficha.pr_color(tablero.casillas_generales[casilla].color)}"+str(tablero.casillas_generales[casilla].color)+f"{Style.RESET_ALL}|"
                else:
                    c12 = "| |"
                    
                print(c12)
                
                # imprimir ala izquierda parte inferior
                for c in range(39, 33, -1):
                    if tablero.casillas_generales[c]:
                        print(f"|{Ficha.pr_color(tablero.casillas_generales[c].color)}"+str(tablero.casillas_generales[c].color), end=f"{Style.RESET_ALL}|")
                    else:
                        print("| |", end="")
                
                # imprimir ala derecha parte inferior
                if tablero.casillas_generales[20]:
                    print(f"       |{Ficha.pr_color(tablero.casillas_generales[20].color)}"+str(tablero.casillas_generales[20].color)+f"{Style.RESET_ALL}|", end="")
                else:
                    print("       | |", end="")
                
                for c in range(19, 14, -1):
                    if tablero.casillas_generales[c]:
                        print(f"|{Ficha.pr_color(tablero.casillas_generales[c].color)}"+str(tablero.casillas_generales[c].color), end=f"{Style.RESET_ALL}|")
                    else:
                        print("| |", end="")
                        
                    # caso especial verde
                    if tablero.casillas_verdes[0] and casilla == 16:
                        print(f"|{Fore.GREEN}"+"V", end=f"{Style.RESET_ALL}|")
                print()
            
            # impimir ala inferior     
            elif casilla > 20 and casilla < 26:
                
                if tablero.casillas_generales[33-(casilla-21)]:
                    c1 = f"|{Ficha.pr_color(tablero.casillas_generales[33-(casilla-21)].color)}"+str(tablero.casillas_generales[33-(casilla-21)].color)+f"{Style.RESET_ALL}|"
                else:
                    c1 = "| |"
                if tablero.casillas_azules[26-casilla]:
                    c2 = f"|{Fore.BLUE}"+"A"+f"{Style.RESET_ALL}|"
                else:
                    c2 = f"{Fore.BLUE}|"+" "+f"|{Style.RESET_ALL}" 
                if tablero.casillas_generales[casilla]:
                    c3 = f"|{Ficha.pr_color(tablero.casillas_generales[casilla].color)}"+str(tablero.casillas_generales[casilla].color)+f"{Style.RESET_ALL}|"
                else:
                    c3 = "| |"
                    
                # caso especial azul
                if tablero.casillas_azules[0] and casilla == 25:
                    c1 = f"|{Fore.BLUE}"+"A"+f"{Style.RESET_ALL}|"
                
                print(c1 + c2 + c3, end="")
                
                verdes_libres = 0
                if casilla == 22:
                    print(" "*4, end="")
                    
                    for ficha in range(len(tablero.casillas_verdes)):
                        if tablero.casillas_verdes[ficha] and tablero.casillas_verdes[ficha].color == "V":
                            if tablero.casillas_verdes[ficha].libre:
                                verdes_libres += 1
                                
                    for ficha in range(len(tablero.casillas_generales)):
                        if tablero.casillas_generales[ficha] and tablero.casillas_generales[ficha].color == "V":
                            if tablero.casillas_generales[ficha].libre:
                                verdes_libres += 1
                    for p in range(4-verdes_libres):
                        print(f"{Fore.GREEN}"+"V ", end=f"{Style.RESET_ALL}")
                    
                    for _ in range(verdes_libres):
                        print(" "*2, end="")

                print()
                
                
            
            # imprimir ultimas 3 casillas ala inferior "| || || |"
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