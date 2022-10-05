from character_and_enemy_factory.character_factory.character_factory import *
from choice_controller.choice import *
lista_character = []
def character_creation_menu():
    for i in  range(0,3):
        name = input("Enter the character's name:")
        age = input("Enter the age of the character:")
        strength = int(input("Enter the strength of the character, remember that there is a limit of 15 points for all attributes:"))
        agility = int(input("Enter the agility of the character, remember that there is a limit of 15 points for all attributes:"))
        life = int(input("Enter the life of the character, remember that there is a limit of 15 points for all attributes:"))
        choice()
        Character(name, age, strength, agility, life, list_type[0])
        lista_character.extend([name, age, strength, agility, life, list_type[0]])

def enemy_creation_menu():
    pass