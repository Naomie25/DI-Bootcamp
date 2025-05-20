#HOW TO CREATE A CLASS
class Dog:
    def __init__(self, name, color, breed, age):
        print("Creating object\n")
        self.name=name
        self.color=color
        self.breed=breed
        self.age=age

    def bark(self):
        print(f'{self.name} is barking')
    
    def walk(self,meters):
        print(f'{self.name} is walking {meters} meters')
    
    def birthday(self):
        self.age+=1

    def rename(self,new_name):
        self.name=new_name
        return self

#Creating an attribute for the specific instance shelter_dog 
# and not for all instances
#shelter_dog.color="Black"
#print(shelter_dog.color)

#Creating an instance (or object) of class Dog
shelter_dog= Dog("Boby","Blue","Pitbull",2)
print(shelter_dog.__dict__)

#Exercice: create 2 objects of class Dog

shitzu_dog=Dog("Cookies","Brown","Shitzu",6)
husky_dog= Dog("Poppy","Grey","Husky",9)
print(shitzu_dog.__dict__)
print(husky_dog.__dict__)

my_dogs=[shelter_dog,shitzu_dog,husky_dog]
for dog in my_dogs:
    print(dog.name)
print(type(husky_dog))
#print(help(str))

my_dogs_objects=[obj for obj in globals().values() if isinstance(obj,Dog)]
print(my_dogs_objects)

puddle_dog=Dog("Papi","white","puddle",6)
puddle_dog.bark()
puddle_dog.walk(100)
for dog in my_dogs:
    dog.bark()

print(shelter_dog.age) 
shelter_dog.birthday()
print(shelter_dog.age) 
shelter_dog.rename("Emily")
print(shelter_dog.name)
