#Exercice 1
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

#Exercice 2
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
for i in range(1500,2501):
    if i%5 ==0 and i%7 ==0:
        print(i)

#Exercice 3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name= input("Enter your name: ")
if user_name in names:
    print(names.index(user_name))

#Exercice 4
list_numbers=[]
for i in range(1,4):
    user_number=int(input("enter a number: " ))
    list_numbers.append(user_number)
max_number=max(list_numbers)
print(f'The maximum value is {max_number}')


#Exercice 5
string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

vowels=['A', 'E', 'I', 'O', 'U', 'Y']
if string:
    for char in string[0:]:
        if char in vowels:
            print(f'{char} is a vowel')
        else:
            print(f'{char} is a consonance')