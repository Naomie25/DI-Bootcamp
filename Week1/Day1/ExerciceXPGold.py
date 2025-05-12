#Exercice 1
print(" Hello World \n"*4 +" I love Python\n"*4)

#Exercice 2


user_month = int(input("Enter the month number (1 to 12): "))

if user_month in [3, 4, 5]:
    print("The season is Spring ")
elif user_month in [6, 7, 8]:
    print("The season is Summer ")
elif user_month in [9, 10, 11]:
    print("The season is Autumn ")
elif user_month in [12, 1, 2]:
    print("The season is Winter ")
else:
    print("Invalid month number ")

