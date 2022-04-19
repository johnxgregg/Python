class Ninja:
    def __init__(self, name, weapon, rating, defense = 45, strength = 55, health = 100):
        self.name = name
        self.health = health
        self.weapon = weapon 
        self.rating = rating 
        self.defense = defense
        self.strength = strength


    def fight(self, enemy_pirate):
        damage = self.strength - enemy_pirate.defense
        enemy_pirate.health -= damage
        return self


# class Pirate(Ninja): inheritance
# pass
# or

class Pirate:
    def __init__(self, name, weapon, rating, defense = 50, strength = 50, health = 100):
        self.name = name
        self.health = health 
        self.weapon = weapon 
        self.rating = rating 
        self.strength = strength
        self.defense = defense

    def fight(self, enemy_ninja):
        damage = self.strength - enemy_ninja.defense
        enemy_ninja.health -= damage
        return self 


ninja_one = Ninja("John", "ninja star", 10)
pirate_one = Pirate("Arg", "sword", 4)

ninja_one.fight(pirate_one)
print(f"Health of the ninja named {ninja_one.name} : {ninja_one.health}")
print(f"Health of the ninja named {pirate_one.name} : {pirate_one.health}")