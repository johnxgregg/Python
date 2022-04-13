

from turtle import clear


class Ninja: 
    
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self 

    def feed(self):
        if len(self.pet_food) > 0: #followed along for this part
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Oh no! You need more food")
        return self

    def bathe(self):
        self.pet.noise()

treats = ["noodle", "cheeto", "couch"]
pet_food = ['dry food', 'wet food']

buddy = Pet("Buddy", "dog", "naps", "bark")
john = Ninja("John", "Gregg", treats, pet_food, buddy)

john.feed();
john.feed();
john.feed();
