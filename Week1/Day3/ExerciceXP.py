#Exercise 1: Converting Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

our_dictionary= dict(zip(keys, values))
print(our_dictionary)

#Exercise 2: Cinemax #2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

final_price=0
for name, age in family.items():
    if age<3:
        price=0
    elif 3 <= age <= 12:
        price=10
    elif age>12:
        price=15
    print(f"{name.capitalize()}'s ticket: ${price}")
    final_price += price

print(f"\nTotal cost for the family: ${final_price}")

#BONUS
family = {}
total_cost = 0

# Ask how many family members
num_members = int(input("How many person are you in your family ? "))

for i in range(num_members):
    name = input(f"Enter the name of family member {i+1}: ")
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age

print("\n Ticket Prices:")
for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"{name.capitalize()}: ${price}")
    total_cost += price

print(f"\n Total cost for the family: ${total_cost}")


#Exercise 3: Zara
brand= {'name': 'Zara','creation_date': 1975, 'creator_name': 'Amancio Ortega Gaona','type_of_clothes': ['men', 'women', 'children', 'home']
,'international_competitors': ['Gap', 'H&M', 'Benetton']
,'number_stores': 7000
,'major_color': 
    {'France': 'blue', 
    'Spain': 'red', 
    'US': ['pink', 'green']}
}
print(brand)

brand['number_stores']=2
print(f'Zara have many clients that can wear his clothes which are: {brand['type_of_clothes']}')

brand['country_creation']='Spain'
print(brand)

if brand['international_competitors']:
    brand['international_competitors'].append('Desigual')
print(brand)
      
del brand['creation_date']
print(brand)   

length=len(brand['international_competitors'])
print(brand['international_competitors'][length-1])


# Print the major colors in the US.
print("Major colors in the US:", brand["major_color"]["US"])
# Print the number of keys in the dictionary.
print("Number of keys in the dictionary:", len(brand.keys()))
# Print all keys of the dictionary.
print("Keys in the dictionary:", brand.keys())

#BONUS MERGING DICTIONARIES
more_on_zara={'creation_date': 1975,'number_stores': 7000}
brand.update(more_on_zara)
print(brand)

#Exercise 4: Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

#FIRST DICTIONARY
first_dict = {user: index for index, user in enumerate(users)}
print(first_dict)

#SECOND 
second_dict = {index: user for index, user in enumerate(users)}
print(second_dict)

#THIRD

sorted_users = sorted(users)

# Create a dictionary using enumerate to map sorted characters to their indices
sorted_dict = {user: index for index, user in enumerate(sorted_users)}

# Print the result
print(sorted_dict)