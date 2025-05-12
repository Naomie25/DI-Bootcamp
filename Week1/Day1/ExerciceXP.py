#Exercice1
print(" Hello World "*4)

#Exercice 2
num= 99**3
print(num)
result=num*8
print("The number is " + str(result) + "\n")

#Exercie3
# >>> 5 < 3 The output will be false
# >>> 3 == 3 The output will be true
# >>> 3 == "3" The output will be false
# >>> "3" > 3 The output will be false
# >>> "Hello" == "hello" The output will be false

#Exercice4
computer_brand="MacBook Pro"
print(f"I have a {computer_brand} computer")

#Exercice 5
name= "Naomie Marciano"
age=24
shoe_size=38
info= f" My name is {name} I am {age} years old and my shoes size is: {shoe_size}"
print(info)

#Exercice 6
a=18
b=12
if a>b:
    print("Hello World")

#Exercice 7
number=int(input("Write am integer number "))
if(number %2==0):
    print("Even number")
else:
    print("Odd number")

#Exercice 8
first_name= input( "what's your name?")
second_name= input( "what's your name?")
if(first_name==second_name):
    print("OMG you both have the same name")
else:
    print("You have the luck to have different name yess")

#Exercice 9
height= int(input( "Hi, What's your heigh is cm?"))
if(height>145):
    print("Your are tall enough to ride!!")
else:
    print(" You need to grow some more to ride")