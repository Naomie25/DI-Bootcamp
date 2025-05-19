#Exercise 3: Dogs Domesticated
from ExerciceXP import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet!")

# Test the class and methods
dog1 = PetDog("Max", 4, 20)
dog2 = PetDog("Luna", 3, 18)
dog3 = PetDog("Charlie", 5, 25)

# Test train() and do_a_trick()
dog1.train()
dog1.do_a_trick()

# Test play()
dog1.play(dog2, dog3)

# Test do_a_trick() for an untrained dog
dog2.do_a_trick()

#Exercise 4: Family and Person Classes
# Step 1: Create the Person class
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


# Step 2: Create the Family class
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("No family member with that first name.")

    def family_presentation(self):
        print(f"The {self.last_name} family:")
        for member in self.members:
            print(f"- {member.first_name}, age {member.age}")
# Create a family instance
my_family = Family("Smith")

# Add family members
my_family.born("Alice", 16)
my_family.born("Bob", 20)

# Check if they are allowed to go out
my_family.check_majority("Alice")  # Should say not allowed
my_family.check_majority("Bob")    # Should say allowed

# Show all members of the family
my_family.family_presentation()
