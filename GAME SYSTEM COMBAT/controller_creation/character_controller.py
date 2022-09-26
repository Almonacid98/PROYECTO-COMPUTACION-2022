import imp
from character_and_enemy_factory.character_factory import *
import os
character_data = Character
lista_character = [character_data.get_name, character_data.get_age, character_data.get_strength, character_data.get_agility, character_data.get_life, character_data.get_type]
def save_character_files(self):
    choice_file = input("Enter which character these characteristics belong to for later saving: -----> 1: [Character_One] * 2: [Character_Two] * 3: [Character_tree]")
    while True:
        if choice_file == 1:
            if os.stat('c:/myarchivo.txt').st_size == 0:

                    print('empty character space')
                    chosen_file = 'character_one.txt'
                    with open(chosen_file, "w") as archive:
                        archive.writelines(lista_character)
                    break
            else:
                print('Character slot full, enter another option')
                break

        elif choice_file == 2:
            if os.stat('c:/myarchivo.txt').st_size == 0:
                print('espacio de personaje vacio')
                chosen_file = 'character_two.txt'
                with open(chosen_file, "w") as archive:
                    archive.writelines(lista_character)
                break
            else:
                print('Character slot full, enter another option')
                break

        elif choice_file == 3:
            if os.stat('c:/myarchivo.txt').st_size == 0:
                print('espacio de personaje vacio')
                chosen_file = 'character_tree.txt'
                with open(chosen_file, "w") as archive:
                    archive.writelines(lista_character)
                break
            else:
                print('Character slot full, enter another option')
                break

                
"""    while True:

        if choice_file == '1':

            file_name = 'character_one.txt'
            with open(file_name, 'w') as archivo:
                archivo.writelines(lista_character) 
            break

        elif choice_file == '2':

            file_name = 'character_two.txt'
            with open(file_name, 'w') as archivo:                                               #Agregar opcion de identificar si el archivo esta lleno o no.
                archivo.writelines(lista_character) 
            break

        elif choice_file == '3':

            file_name = 'character_tree.txt'
            with open(file_name, 'w') as archivo:
                archivo.writelines(lista_character) 
            break

        else:

            print("\n WRONG OPTION.... PLEASE AGAIN CHOOSE AN EXISTING OPTION IN THE SYSTEM....")"""