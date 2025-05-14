#Exercise 1: What Are You Learning?
def display_message():
    print("I am learning about functions in Python.")

display_message()

#Exercise 2: What’s Your Favorite Book?
def favorite_book(title):
    print(f'One of my favorite books is: {title}.')

favorite_book("A contre sens")

#Exercise 3: Some Geography
def describe_city(city, country="Unknown"):
    print(f'{city} is in {country}')

describe_city("Reykjavik", "Iceland")
describe_city("Paris")

#Exercise 4: Random
import random
def rand_number(user_number):
    num=random.randint(1, 100)
    if num==user_number:
        print("Great!! Same number")
    else:
        print(f'You failed! user_number={user_number} and random number= {num}')
user= input("enter a number")
rand_number(int(user))


#Exercise 5: Let’s Create Some Personalized Shirts! 
def make_shirt(size="large", text="I love python"):
    print(f'Your size is: {size} and {text}')
make_shirt("Small", "I love shopping")

make_shirt()
make_shirt("Medium",)
make_shirt("Small", "I love cooking")
make_shirt(size="small", text="Hello!")

#Exercise 6: Magicians…
magician_names=['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names):
    for each_magicien in names:
        print(f'My name is: {each_magicien}')
show_magicians(magician_names)

def make_great(magicians):
    for index, each_magicien in enumerate(magicians):
        magicians[index] = 'The great ' + magicians[index]
    print(magicians)
make_great(magician_names)

#Exercise 7: Temperature Advice
def get_random_temp():
    number=random.uniform(-10, 40)
    return number

def main():
    text=""
    random_temp= get_random_temp()
    if random_temp<0:
        text= "Brrr, that’s freezing! Wear some extra layers today."
    elif 0<random_temp<16:
        ptext="Quite chilly! Don’t forget your coat."
    elif 16<random_temp<23:
        text="Nice weather."
    elif 24<random_temp<32:
        text="A bit warm, stay hydrated."
    elif 32<random_temp<40:
        text="It’s really hot! Stay cool."
    print(f'The temperature right now is {random_temp} degrees Celsius. {text}')
main()

#Month-Based Seasons (Bonus)
def get_random_temp(season):
    if season == "winter":
        return round(random.uniform(-10, 10), 1)
    elif season == "spring":
        return round(random.uniform(5, 20), 1)
    elif season == "summer":
        return round(random.uniform(20, 40), 1)
    elif season == "autumn":
        return round(random.uniform(5, 25), 1)
    else:
        # Default if season not recognized
        return round(random.uniform(-10, 40), 1)
    

def main2():
    month = int(input("Enter the current month (1-12): "))
    season=""
    if month in [12, 1, 2]:
        season = "winter"
    elif month in [3, 4, 5]:
        season = "spring"
    elif month in [6, 7, 8]:
        season = "summer"
    elif month in [9, 10, 11]:
        season = "autumn"
    
    else:
        print("Invalid month! Using a random temperature.")
        season = "unknown"
    print(f"The season is:{season}")
main2()
