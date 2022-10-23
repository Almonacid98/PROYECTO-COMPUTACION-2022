from character_and_enemy_factory.character_factory.character_factory import Character
class Enemy(Character):
    def __init__(self, name, age, strength, agility, life, type) -> None:
        super().__init__(name, age, strength, agility, life, type)                         #https://pythondiario.com/2016/10/simple-juego-rpg-en-python.html
        
