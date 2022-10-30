import random
from character_and_enemy_factory.character_factory.character_factory import Character

class Enemy:
    def __init__(self, name, age, strength, agility, life, type) -> None:  
        self.name = name
        self.age = age
        self.strength = strength
        self.agility = agility
        self.life = life
        self.type = type #https://pythondiario.com/2016/10/simple-juego-rpg-en-python.html
        

    def generate(self):
            print("Enemies initialized for combat")
            diccionario = {'Raza': self.name,
                           'age': self.age,
                           'strength': self.strength,
                           'agility': self.agility,
                           'life': self.life,
                           'type': self.type}
            print(diccionario)
            
