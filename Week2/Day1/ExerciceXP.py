#Exercise 1: Cats

class Cat:

    def __init__(self, name, age):
        print("Creating cat\n")
        self.name=name
        self.age=age
    def oldest_cat(self,cats):
        oldest_age=0
        for cat in cats:
            if cat.age>oldest_age:
                oldest_age=cat.age
                our_cat=cat
        return our_cat

Dolev= Cat("Dolev",8) 
Naomie= Cat("Naomie",3) 
Emily= Cat("Emily",12) 
cats=[Dolev,Naomie,Emily]
oldest_cat= Dolev.oldest_cat(cats)
print(f'The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.')

#Exercise 2 : Dogs
class Dog:
    def __init__(self, name, height):
        print("Creating cat\n")
        self.name=name
        self.height=height

    def bark():
        print("goes woof!")
    
    def jump(self):
        jump_height = self.height * 2
        print(f'{self.name} jumps {jump_height} cm high!')

davids_dog=Dog("David",120)
sarahs_dog=Dog("Sarah",110)

davids_dog.jump()
sarahs_dog.jump()

# Compare heights
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller than {sarahs_dog.name}")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is taller than {davids_dog.name}")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same height.")

#Exercise 3 : Who’s the song producer?
class Song:
    def __init__(self,lyrics):
        self.lyrics=lyrics

    def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(lyric)
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#Exercise 4 : Afternoon at the Zoo
class Zoo:
    def __init__(self,zoo_name):
        self.zoo_name=zoo_name
        self.animals = []
    
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print("This animal is already on the list")

    def get_animals(self):
        for each_animal in self.animals:
            print(each_animal)

    def sell_animal(self, animal_sold):
        if animal_sold  in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")
    
    def sort_animals(self):
        self.animals.sort()
        our_dict={}
        grouped_animals = {}

        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = [animal]
            else:
                grouped_animals[first_letter].append(animal)

        return grouped_animals
    
    def get_groups(self):
        grouped_animals = self.sort_animals()
        for letter, animals in grouped_animals.items():
            print(f"{letter}: {animals}")

my_zoo=Zoo("Thouary")
my_zoo.add_animal("Lion")
my_zoo.add_animal("Spider")
my_zoo.add_animal("Crocodile")
my_zoo.add_animal("Lizard")
my_zoo.add_animal("Dog")
my_zoo.add_animal("Dog")
my_zoo.add_animal("Snake")
my_zoo.sell_animal("Dog")
my_zoo.get_animals()

# Sort and group animals
grouped = my_zoo.get_groups()
print("Grouped and sorted animals:")
#for letter, animal_list in grouped.items():
    #print(f"{letter}: {animal_list}")
