import imp


import random
from character_and_enemy_factory.character_factory import *
class Combat(Character):
    def __init__(self, name, age, strength, agility, life, type) -> None:
        super().__init__(name, age, strength, agility, life, type)
        self.__life = 5
        self.__life_max = 7

    def variacion(self):
        for i in range(self.__life_max):
            variacion = random.random()
        return variacion
    
    def get_status(self):
        return super().get_status()

    def attack(self, objetive):
        pass
