class Selection:
    def select_character(self):
        option = int(input("<<<Choose Your Character>>>\nOption 1: Character One\nOption 2: Character Two\nOption 3: Character Three\nWho is The Choosen One:"))
        if option == 1:
            with open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_one.txt", "r") as archivo:
                lista_character = [linea.rstrip() for linea in archivo]
            print(lista_character)
            input("Presione una tecla para continuar....")
                    
        elif option == 2:
            with open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_two.txt", "r") as archivo:
                lista_character = [linea.rstrip() for linea in archivo]
            print(lista_character)
            input("Presione una tecla para continuar....")

        elif option == 3:
            with open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_tree.txt", "r") as archivo:
                lista_character = [linea.rstrip() for linea in archivo]
            print(lista_character)
            input("Presione una tecla para continuar....")