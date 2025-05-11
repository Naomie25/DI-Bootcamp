#BASIC VALUE TYPES

#STRINGS: is a sequence of characters that represents text in python
#"Hello python"

#STRINGS METHODS
print("hello naomie".capitalize())
print("hello emily".capitalize())

#Strings : sequence of chars, it allows us to use index (position)
grettings="Hello Python"
print(grettings[6:12])

#First Exercice
description = "strings are..."
print(description.upper())
print(description.replace('are', 'is'))

print(description[:7])

#NUMBERS: INT, FLOAT, COMPLEX
a=5 #int
b=2.6 #float

#SECOND EXERCICE
my_age=24
print(my_age+123879)

#THIRD EXERCICE
bank_balance = '33000'
phone_number = 532287514
print(int(bank_balance))
print(str(phone_number))

#FOURTH EXERCICE
firstName= "Naomie"
lastName= "Marciano"
print(firstName+ " "+ lastName)

#BOOLEAN: TRUE OR FALSE VALUES
#FIFTH EXERCICE
x = 5
y = 10
z = 0
word1 = "hello"
word2 = "world"

print(x < y and y > z)
print(word1 != word2)
print(bool(z))
print(bool(word1))


user_age=int(input("what is your age?"))
print(user_age+50)


#SIXTH EXERCICE
name= "Alice"
age=30
city="New York"
## f-string
print(f"Hello {name}! You are {age} years old and live in {city}.")

#str format
print("Hello {}! You are {} years old and live in {}.".format(name, age, city))


#Exercice 7
userAge=int(input("what is your age?"))
int(userAge)
x=100-userAge

print("You will turn 100 in " +str(x) +" years")

#Conditionals
user_name=(input("What is your name?"))
if len(user_name)<5:
    print('You have a short name :)')
# else:
#     print('You have a long name :)')



user_num=input("Enter a number between 1 to 100 ")
int(user_num)
if int(user_num) %3==0 and int(user_num) %5==0:
    print("FizzBuzz")
elif int(user_num) %5==0:
    print("Buzz")
elif int(user_num) %3==0:
    print("Fizz")
else:
    print("not valid")
