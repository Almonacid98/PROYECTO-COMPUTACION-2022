from main_constants_menu import *
import os
from os import remove
def save_character_files():
    choice_file = input("Enter which character these characteristics belong to for later saving: -----> 1: [Character_One] * 2: [Character_Two] * 3: [Character_tree]")
    while True:
        if choice_file == '1':
            open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_one.txt", "w")
            if os.stat('C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_one.txt').st_size == 0:
                    print('empty character space')
                    chosen_file = 'C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_one.txt'
                    with open(chosen_file, "w") as archive:
                        archive.writelines(str(lista_character))
                    break
            else:
                print('Character slot full, enter another option')
                break

        elif choice_file == '2':
            if os.stat('C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_two.txt').st_size == 0:
                print('espacio de personaje vacio')
                chosen_file = 'character_two.txt'
                with open(chosen_file, "w") as archive:
                    archive.writelines(str(lista_character))
                break
            else:
                print('Character slot full, enter another option')
                break

        elif choice_file == '3':
            if os.stat('C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_tree.txt').st_size == 0:
                print('espacio de personaje vacio')
                chosen_file = 'character_tree.txt'
                with open(chosen_file, "w") as archive:
                    archive.writelines(str(lista_character))
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
