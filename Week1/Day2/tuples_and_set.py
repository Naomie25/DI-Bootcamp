#Tuples are immutables list (items can't be changed)
#There is no notion of an empty tuple

my_tupple=('TLV','CDG')
print(my_tupple)
print(type(my_tupple))

#Convert other sequence into a tuple
my_tuple= tuple(range(11))
print(my_tuple)

passwords=('abc','j','abc','abc')
print(passwords.count('abc'))

#access by index
print(passwords[1])

#Workaround on how to change tuples
temp_list=list(my_tuple)
temp_list.extend(['A','B','C'])
my_tuple= tuple(temp_list)
print(my_tuple)

my_tuple+=('A','B','C')
print(my_tuple)

#SETS: NOT ORDERED: not possible to access by index
#don't allow dupplicate elements
set=set()
countries={'Israel','France','USA'}
names={'Naomie','Sarah','Anaelle','Israel'}

#print(countries[1]) #typeError 'set' object is not subscriptable

person_country= countries.intersection(names)
print(person_country)