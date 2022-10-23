import os
from os import remove
from character_and_enemy_factory.character_factory.character_factory import *
class Contantes():

    __lista = []

    def set_lista_save(self, lista):
        self.__lista = lista

    def character_creation_menu(self):
        contador = 1
        while contador <= 3:
            name = input("Enter the character's name:")
            age = input("Enter the age of the character:")
            strength = int(input("Enter the strength of the character, remember that there is a limit of 15 points for all attributes:"))
            agility = int(input("Enter the agility of the character, remember that there is a limit of 15 points for all attributes:"))
            life = int(input("Enter the life of the character, remember that there is a limit of 15 points for all attributes:"))
            choice = input("Enter the type of character, there are only 3 types -----> 1:[WARRIOR] * 2:[Elf] * 3:[Archer]")
            while True:
                        if choice == '1':
                            type = "WARRIOR"   
                            break
                        elif choice == '2':
                            type = "ELF"  
                            break
                        elif choice == '3':
                            type = "ARCHER"
                            break
                        else:
                            print("\n WRONG OPTION.... PLEASE AGAIN CHOOSE AN EXISTING OPTION IN THE SYSTEM....")
            Character(name, age, strength, agility, life, type)
            self.__lista.extend([name, age, strength, agility, life, type])
            contador += 1
            break

    def save_character_files(self):
        choice_file = input("Enter which character these characteristics belong to for later saving: -----> 1: [Character_One] * 2: [Character_Two] * 3: [Character_tree]:")
        while True:
            if choice_file == '1':
                open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_one.txt", "w")
                if os.stat('C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_one.txt').st_size == 0:
                        print('empty character space')
                        chosen_file = 'C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_one.txt'
                        with open(chosen_file, "w") as archive:
                            archive.writelines(str(self.__lista))
                        break
                else:
                    print('Character slot full, enter another option')
                    break

            elif choice_file == '2':
                open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_two.txt", "w")
                if os.stat('C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_two.txt').st_size == 0:
                    print('espacio de personaje vacio')
                    chosen_file = 'C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_two.txt'
                    with open(chosen_file, "w") as archive:
                        archive.writelines(str(self.__lista))
                    break
                else: 
                    print('Character slot full, enter another option')
                    break

            elif choice_file == '3':
                open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_tree.txt", "w")
                if os.stat('C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_tree.txt').st_size == 0:
                    print('espacio de personaje vacio')
                    chosen_file = 'C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_tree.txt'
                    with open(chosen_file, "w") as archive:
                        archive.writelines(str(self.__lista))
                    break
                else:
                    print('Character slot full, please remove a character')
                    break

    def delete_character():
        select = input("Choose the character to eliminate by numbering: 1:[WARRIOR] * 2:[Elf] * 3:[Archer]")
        if select == '1':
            remove('C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_one.txt')
        elif select == '2':
            remove('C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_two.txt')
        elif select == '3':
            remove('C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_tree.txt')
        else:
            print("Wrong option, enter a valid option")