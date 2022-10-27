import random
class Points:
    def begin(self):
        if (self.life and self.strength and self.agility) == 15:
            return #pasamos a combat

    def xp_comprobation(self):
        if enemy == 'False': #comprobabos que este muerto
            character_one.xp += 1
            character_two.xp += 1
            character_three.xp += 1
            #llamamos a level_up en combat

    def level_up(self):
        if character_one.xp == 2:
            number = random.randint(1, 10)
            character_one.level += 1
            character_one.self.life = self.life + number
            character_one.self.strength = self.strength + number
            character_one.self.agility = self.agility + number
        
        if character_two.xp == 2:
            number = random.randint(1, 10)
            character_two.level += 1
            character_two.self.life = self.life + number
            character_two.self.strength = self.strength + number
            character_two.self.agility = self.agility + number
        
        if character_three.xp == 2:
            number = random.randint(1, 10)
            character_three.level += 1
            character_three.self.life = self.life + number
            character_three.self.strength = self.strength + number
            character_three.self.agility = self.agility + number
