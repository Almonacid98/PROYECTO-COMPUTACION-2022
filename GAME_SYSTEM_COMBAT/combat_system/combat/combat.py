from os import remove
import random
from visual_interface.interface.visual import *

class Combat():
    __lista_character = []
    __lista_enemy = []
    
    def set_character_list(self, list_char):
        self.__lista_character = list_char
    
    def set_enemy_list(self, list_enemy):
        self.__lista_enemy = list_enemy

    def select_character(self):
        option = int(input("<<<Choose Your Character>>>\nOption 1: Character One\nOption 2: Character Two\nOption 3: Character Three\nWho is The Choosen One:"))
        while True:
            try:
                if option == 1:
                    with open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_one.txt", "r") as archivo:
                        for linea in archivo:
                            lista = linea.rstrip()
                            self.__lista_character.append(lista)
                    print(self.__lista_character)
                    input("Presione una tecla para continuar....")
                    break
                            
                elif option == 2:
                    with open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_two.txt", "r") as archivo:
                        for linea in archivo:
                            lista = linea.rstrip()
                            self.__lista_character.append(lista)
                    print(self.__lista_character)
                    input("Presione una tecla para continuar....")
                    break

                elif option == 3:
                    with open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_tree.txt", "r") as archivo:
                        for linea in archivo:
                            lista = linea.rstrip()
                            self.__lista_character.append(lista)
                    print(self.__lista_character)
                    input("Presione una tecla para continuar....")
                    break
            except:
                option == input("El personaje murio... Elegir entre los disponibles")
                break
                

    def select_enemy(self):
        enemy_variable = ['enemy_one.txt', 'enemy_two.txt', 'enemy_tree.txt', 'enemy_four.txt', 'enemy_five.txt', 'enemy_six.txt', 'enemy_seven.txt', 'enemy_eight.txt', 'enemy_nine.txt', 'enemy_ten.txt']
        enemy_choice = random.choice(enemy_variable)
        direccion = "C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy" + "/" + str(enemy_choice)
        enemy_variable.remove(str(enemy_choice))
        with open(direccion, "r") as archivo:
                    for linea in archivo:
                        lista = linea.rstrip()
                        self.__lista_enemy.append(lista)
        print(f"The enemy you are going to fight will be: {self.__lista_enemy}")
        input("Presione una tecla para continuar....")

    
    def combat(self):
        start = input("want to start the fight?: yes or no: ")
        contador = 0
        if start == 'yes':
            while True:
                        opcion_character = input("Character's turn, do you want to attack or pass turn? attack/pass turn: ")
                        if opcion_character == 'attack':
                            life = int(self.__lista_enemy[4]) - 1
                            self.__lista_enemy[4] = life
                            print(f"El enemigo quedo en: {life} de vida")
                            if life == 0:
                                print("El enemigo ha sido derrotado!")
                                self.__lista_enemy.clear()
                                item = input("Usted gano un punto de habilidad ---> donde quiere invertirlo? life/strenght/agility: ")
                                if item == 'life':
                                    life = int(self.__lista_character[4]) + 1
                                    self.__lista_character[4] = life
                                    print(f"La vida subio a {life} puntos")
                                    print(self.__lista_character)
                                    input("presione cualquier tecla para continuar")
                                    break
                                if item == 'strenght':
                                    strenght = int(self.__lista_character[2]) + 1
                                    self.__lista_character[2] = strenght
                                    print(f"La fuerza subio a {strenght} puntos")
                                    print(self.__lista_character)
                                    input("presione cualquier tecla para continuar")
                                    break
                                if item == 'agility':
                                    agility = int(self.__lista_character[3]) + 1
                                    self.__lista_character[3] = agility 
                                    print(f"La agilidad subio a {agility} puntos")
                                    print(self.__lista_character)
                                    input("presione cualquier tecla para continuar")
                                    break
                        elif opcion_character == 'pass turn':
                            input("Enemy's turn, do you want to attack or pass turn? attack/pass turn")
                            opcion_enemy = ['attack', 'pass turn']
                            if random.choice(opcion_enemy) == 'attack':
                                life = int(self.__lista_character[4]) - 1
                                self.__lista_character[4] = life
                                print(f"El Personaje quedo en: {life} de vida")
                                if life == 0:
                                    print("El enemigo te ha vencido..")
                                    self.__lista_character.clear()
                                    self.__lista_enemy.clear()
                                    contador += 1
                                    while True:
                                        if contador == 1:
                                            remove('C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_one.txt')
                                            break
                                        elif contador == 2:
                                            remove('C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_two.txt')
                                            break
                                        elif contador == 3:
                                            remove('C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_tree.txt')
                                            break
                                    break         
                            elif random.choice(opcion_enemy) == 'pass turn':
                                pass
        else:
            input("Volviendo al menu.....")