from character_and_enemy_factory.character_factory import *
from controller_creation.character_controller import *
def character_creation_menu(self):
    for i in  range(0,2):
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
        save_character_files()

def enemy_creation_menu(self):
    pass




