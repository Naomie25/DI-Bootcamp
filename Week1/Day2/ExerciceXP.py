#Exercise 1
my_fav_numbers={1,25,8,14,12,22,24,16}
print(my_fav_numbers)

my_fav_numbers.add(26)
my_fav_numbers.add(2)
print(my_fav_numbers)

my_fav_numbers.remove(2)
print(f'After removing last item  {my_fav_numbers}')

friend_fav_numbers={6,9,11,30,22}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

##Exercise 2
my_tuple=(1,4,9,18,12,26)
print((my_tuple))
#workaround to add items to tuple
temp_list=list(my_tuple)
temp_list.extend([2,8,10])
my_tuple= tuple(temp_list)
print(my_tuple)

#Exercice 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(f'After removing banana  {basket}')

basket.remove("Blueberries")
print(f'After removing Blueberries  {basket}')

basket.append("Kiwi")
print(f'After adding Kiwi  {basket}')

basket.insert(0, "Apples")
print(f'After adding Apples  {basket}')

count_apples = basket.count("Apples")
print("Apples appears", count_apples, "times.")

basket.clear()
print(f'The list is: {basket}')

#Exercice 4
#A float is a decimal value and a int is an integer value
my_list=[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
#second way
numbers = []
current = 1.5
while current <= 5:
    numbers.append(current)
    current += 0.5

print(numbers)

#Exercice 5
for number in range(1,21):
    print(number)

for even_numbers in range(2,21,2):
    print(even_numbers)


#Exerciece 6 
my_name="Naomie"
user_name=input("Enter your name: ")
while my_name !=user_name:
    print("That's not my name. Try again.")
    user_name=input("Enter your name: ")

print("That's my name too! Loop stopped.")

#Exercice 7
user_fruits= input("Enter some fruits separated by spaces:")
fruits_list=[]
fruits_list= user_fruits.split()
print("Your favorite fruits are:", fruits_list)

fruit=input("Enter a name of a fruit")
if fruit in fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

#Exercice 8
toppings_list = []
basic_price = 10
price_per_topping = 2.5

while True:
    user_topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    if user_topping.lower() == 'quit':
        break
    print(f"Adding {user_topping} to your pizza.")
    toppings_list.append(user_topping)

# Final price calculation
final_price = basic_price + len(toppings_list) * price_per_topping
final_price = round(final_price, 2)

print(f"\nYour pizza toppings: {toppings_list}")
print(f"Total price: ${final_price}")

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

#Exercice 9
family_members= int(input("How many person are you in the family?"))
ages_list=[]
total_price = 0
for each_member in range(1,(family_members)+1):
    user_age= int(input(f"Enter the age of family member {each_member}: "))
    ages_list.append(user_age)

for age in ages_list:
    if age<3:
        price=0
    elif 3 <= age <= 12:
        price=10
    else:
        price=15
    total_price += price
print(f'The price is {total_price}')


#Bonus
group_size = int(input("How many people are in the group? "))
attendees = []

for i in range(1, group_size + 1):
    age = int(input(f"Enter the age of person {i}: "))
    if 16 <= age <= 21:
        attendees.append(age)
    else:
        print(f"Person {i} is not allowed to watch the movie.")

# Show final list of allowed attendees
print(f"\nFinal list of attendees (ages 16-21): {attendees}")

#Exercice 10
sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
for food in sandwich_orders:
    if food=="Pastrami":
        sandwich_orders.remove(food)
print(sandwich_orders)

for sandwich in sandwich_orders:
    print(f' I made your {sandwich} sandwich')
print(sandwich_orders)