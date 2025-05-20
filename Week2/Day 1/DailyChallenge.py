class Farm:
    def __init__(self,farm_name):
        self.farm_name=farm_name
        self.animals={}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count  # Increase existing count
        else:
            self.animals[animal_type] = count  # Add new animal with count

    def get_info(self):
        info = f"{self.farm_name}'s Farm\n"
        info += "-" * 20 + "\n"
        for animal, count in self.animals.items():
            info += f"{animal:<10} : {count}\n"
        info += "-" * 20 + "\n"
        info += "E-I-E-I-O!"
        return info
    
    def  get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_names = []

        for animal in animal_types:
            count = self.animals[animal]
            name = animal + "s" if count > 1 else animal
            animal_names.append(name)

        if len(animal_names) > 1:
            animals_list = ", ".join(animal_names[:-1]) + " and " + animal_names[-1]
        else:
            animals_list = animal_names[0]

        return f"{self.farm_name}'s farm has {animals_list}."

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
our_animals= macdonald.get_animal_types()
for animal in our_animals:
    print(animal)
info= macdonald.get_short_info()
print(info)
# our_farm= Farm("Naomie's Farm")
# our_farm.add_animal("cow")
# our_farm.add_animal("pig")
# our_farm.add_animal("horse", 2)
# our_farm.add_animal("pig", 1)

# print(our_farm.animals)
# print(our_farm.get_info())



