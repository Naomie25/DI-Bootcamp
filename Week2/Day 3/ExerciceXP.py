#Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def __str__(self):
        return f"{self.amount} {self.currency}s" if self.amount != 1 else f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount
    
    def __repr__(self):
        return self.__str__()
    
    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add different currencies: {self.currency} and {other.currency}")
            return Currency(self.currency, self.amount + other.amount)
        elif isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        else:
            raise TypeError("Unsupported type for addition")
        
    def __radd__(self, other):
        return self.__add__(other)  # ensures 5 + c1 also works
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
#the comment is the expected output
print(str(c1))
# '5 dollars'

print(int(c1))
# # 5

print(repr(c1))
# # '5 dollars'

print(c1 + 5)
# # 10

print(c1 + c2)
# # 15

print(c1) 
# # 5 dollars

c1 += 5
print(c1)
# # 10 dollars

c1 += c2
print(c1)
# # 20 dollars

#print(c1 + c3)
# # TypeError: Cannot add between Currency type <dollar> and <shekel>

#Exercise 3: String module
import random
import string

def gen_random_string(str):
    random_str=""
    for i in range(5):
       
        random_str += random.choice(str)
    return random_str
print(gen_random_string("naomie la plus belle salut sava"))

#Exercise 4: Current Date
from datetime import datetime, date
def display_date():
    return datetime.today()
print(display_date())

#Exercise 5: Amount of time left until January 1st
def amount_of_time_left():
    # Step 1 & 2: Get current date and time
    current_date = datetime.now()
    print("Current date and time:", current_date)

# Step 3: Create datetime object for January 1st of next year
    next_year = current_date.year + 1
    jan_1_next_year = datetime(next_year, 1, 1)
    print("January 1st of next year:", jan_1_next_year)

# Step 4: Calculate the time difference
    time_difference = jan_1_next_year - current_date

# Step 5: Display the time difference
    print("Time until next year:", time_difference)
    print(f"Days: {time_difference.days}, Seconds: {time_difference.seconds}")

amount_of_time_left()

#Exercise 6: Birthday and minutes

def minutes_lived(birth_date):
    birthdate = datetime.strptime(birth_date, '%Y-%m-%d')
    
    now = datetime.now()
    
    # Calculate the time difference
    time_diff = now - birthdate
    
    # Convert the difference to minutes
    minutes = time_diff.total_seconds() / 60
    
    print(f"You have lived approximately {int(minutes):,} minutes.")

# Example call:
minutes_lived('1990-02-01')

# Exercise 7: Faker Module
from faker import Faker

# Step 3: Create an empty list of users
users = []

# Create a Faker instance
faker = Faker()

# Step 4: Create a function to add users
def add_users(num_users):
    for _ in range(num_users):
        user = {
            "name": faker.name(),
            "address": faker.address(),
            "language_code": faker.language_code()
        }
        users.append(user)

# Step 5: Call the function and print the users list
add_users(5)  # Generates 5 fake users
for user in users:
    print(user)


