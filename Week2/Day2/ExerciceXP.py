
#Exercise 1: Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal_obj=Bengal("Louly",3)
chartreux_obj=Chartreux("Poppy",5)
siamese_obj=Siamese("Lola",8)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]
sara_pets=Pets(all_cats)
sara_pets.walk()

#Exercise 2: Dogs
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}!"
        elif self_power < other_power:
            return f"{other_dog.name} won the fight against {self.name}!"
        else:
            return "It's a tie!"
        
dog1 = Dog("Buddy", 5, 20)
dog2 = Dog("Virgule", 3, 25)
dog3 = Dog("Leo", 4, 18)

print(dog1.bark())
print(f"{dog1.name}'s speed: {dog1.run_speed()}")

print(dog2.bark())
print(f"{dog2.name}'s speed: {dog2.run_speed()}")

print(dog3.bark())
print(f"{dog3.name}'s speed: {dog3.run_speed()}")

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))





