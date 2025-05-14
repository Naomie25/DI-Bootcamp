#FUNCTIONS
#syntax

def func_name():
    print("I am a function")
    ''' prints a phrase on the console ''' #doc strings

#This is to call it
func_name()
print(print.__doc__)

#Exercice
def greetings(language):
    if language=="French":
        print("Bonjour")
    else:
        print("שלום")
greetings("French")


#Passing some arguments
def func(language,user_name):
    if language=="French":
        print(f'Bonjour {user_name}')
    else:
        print(f' {user_name} שלום ' )
func("French", "Naomie")

def default_values(language="French",user_name="Naomie"):
    if language=="French":
        print(f'Bonjour {user_name}')
    else:
        print(f' {user_name} שלום ' )

default_values()


def country_info(country_name="France"):
    if country_name=="France":
        print("The capital is Paris")
    elif country_name=="Spain":
         print("The capital is Madrid")
country_info("Spain")


#return keyword
def calculation(num1, num2):
    return num1+num2

print(calculation(3,2))

countries=['France','Israel','China']
def func_countries(countries):
    for country in countries:
        print(f'Hello {country}')
        if country=='Israel':
            return

print(func_countries(countries))


#SCOPES
#Global scope: on the file, in general
name = 'Avner'

def say_hi():
  print(name)

say_hi()

#Local scope: indented scope
def number_by_three(name, day):
  sentence = f'Hello {name}! Today is {day}.'
  print(sentence)

global_var_1 =100

def calculate(a,b):
    global_var_1=10
    global_var_1+=1 # it will change the value 100 to 101 because it's global
calculate(2,3)
print(global_var_1)

