shopping_list=['Milk', 'eggs', 'bread']
shopping_list.append("Cereals")
shopping_list.remove("eggs")
print(shopping_list)

#DICTIONARY
students= {"name":"John","age":20,"major":"Computer science"}

#Modify an entry in a dictionary
students["age"]=25
print(students)

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

print(a_dict.items())


# The items() method returns a view object that displays 
# a list of dictionary's (key, value) tuple pairs.

for key, value in a_dict.items():
    print(key, '->', value)

#Data types
#You can store any type of data inside a dictionary. 
# That could be strings and integers but also other dictionaries or lists.
my_dog = {
  'name': 'Rufus',
  'age': 4,
  'best_friend': {
    'name': 'Felix',
    'age': 4.5
  },
  'favorite_foods': ['steaks', 'sausages', 'shawarma']
}
print(my_dog)


rick_dict = {
    'first_name':'Rick',
    'last_name':'Sanchez'
}
print("The last name of rick is:", rick_dict['last_name'])

#Adding an entry to an existing dictionary
rick_dict['age']=20
rick_dict['hair color']='white'
print(rick_dict)


#Dictionaries and lists
shirts = [
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'S',
    'price': 20
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'M',
    'price': 25
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'L',
    'price': 30
  },
]

#Exercice: Access the value of key history
sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict)
print(sample_dict["class"]["student"]["marks"]["history"])

#Delete an entry in a dictionary
del rick_dict['hair color']
print(rick_dict)

# First, keys are uniques; they can appear in a dictionary only once; 
# if you assign a value to an existing dictionary key, 
# it does not add the key a second time but replaces the current value.
# Secondly, the key must be an immutable type; 
# it can be an integer, a float, a string, a boolean, 
# and even a tuple because all those types are immutables. 
# List can’t be a dictionary key.

#IN KEYWORD in a list: returns True or False 
# according to whether the specified operand occurs in the list.

#IN KEYWORD in A dictionary returns True 
# if the operand occurs as a key in the dictionary.

#ITERATING
for shirt in shirts:
  print(shirt['size'])


# item() returns a dict_items of tuples containing the key-value pairs in a dictionary.
print(rick_dict.items())

#deleting keys
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    sample_dict.pop(key, None)  # Safely remove each key
print(sample_dict)

#FOR LOOP
my_books = {
  "title": "Harry Potter",
  "author": "JK Rowling",
}

for x, y in my_books.items():
    print("the " + x + " "
    "is " + y)

#enumerate(iterable) : enumerate each item in the iterable
for item in enumerate('abcd'):
    print(item)
for (index_count, letter) in enumerate('abcd'):
    print('At index {} the letter is {}'.format(index_count, letter))

#zip(iterable,..) : concat [iterables, …] in a tuple.
list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

for item in zip(list1, list2, list3): # only go as far it is possible
    print(item)

#For Else
#The else part is optional.
#  When included, it is always executed once after the for loop is over 
# unless a break statement is encountered.
for i in range(1, 3):
    print(i)
else:
    print('The for loop is over')

#While Else
x = 0
while x < 2:
    print(f'x is {x}')
    x += 1
else:
    print('x is bigger than 2')

#Break, Continue, Pass
for letter in 'Leonardo':
    if letter == 'a':
        break
    print(letter, end='') # end='' renders each letter next to the other

while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')


#continue: return to the top of the loop (continue to the next iteration of the loop)
for letter in 'Leonardo':
    if letter == 'o':
        continue
    print(letter, end='') # dont execute for 'o' letter

#pass: do nothing
for item in [1,2,3]:
    # comment
    pass # to avoid the error

print('Finish the script')

#Dictionary comprehension
family_age = {'Lea': 12, 'Mark': 25, 'George': 50}

new_year = 1

new_family_age = {name: age+new_year for (name, age) in family_age.items()}

print(new_family_age)