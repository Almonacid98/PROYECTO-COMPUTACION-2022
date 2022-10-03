from abc import abstractmethod
class Character():

    def __init__(self, name, age, strength, agility, life, type) -> None: #Solo se pueden crear un máximo de 3 personajes
        self.name = name
        self.age = age
        self.__strength = strength
        self.__agility = agility            #limite de puntos 15, ninguno puede ser 0.
        self.__life = life
        self.type = type #3 tipos, 2+ a distintos atributos
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age

    def set_strength(self, strength):
        self.__strength = strength

    def set_agility(self, agility):
        self.__agility = agility

    def set_life(self, life):
        self.__life = life

    def set_type(self, type):
        self.type = type

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def get_strength(self):
        return self.__strength
    
    def get_agility(self):
        return self.__agility
    
    def get_life(self):
        return self.__life
    
    def get_type(self):
        return self.type


    def attack(self, objetive):
        pass

    @abstractmethod
    def get_status(self):
        print(f"Name: {self.name}. Life: {self.__life}. Type:{self.type}")
    
    def increase_attribute(self):
        pass

    