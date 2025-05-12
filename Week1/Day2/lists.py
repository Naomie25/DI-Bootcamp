#list is an ordered sequence of elements 

some_list=list('item 1') # to convert a sequence to a list
other_list=['item 1'] # the best way to create an empty list

print(some_list)
print(other_list)

print(len(some_list))
print(len(other_list))

#Accessing by index
print(some_list[1])

#Methods for list
some_list.append('A')
print(some_list)

my_list=[]
my_list.append('A')

#it allows us to add more than one element
my_list.extend(['B','C','D'])
print(my_list)

# Create an empty list and add 4 names (using a methode) of your favourite characters from show

names=[]
names.extend(["Chuck Bass","Damon Salvatore","Nick Leister","James Beaufort"])
print(names)

num_list=(list(range(1,8)))
print(num_list)
print(num_list[2:6])

copied_list=num_list.copy()
print(copied_list)
print(id(num_list))
print(id(copied_list))

copied_list=num_list
name="Naomie"
new_name=name
print(id(name))
print(id(new_name))


#other methods
#insert(where,what)
#remove(what) removes the first occurence of the element

#deleting some elements
del(num_list[3])
print(num_list)

#extract the last element
num_list.pop()
print(num_list)

#sorted() don't change the original list
new_list=[1,5,3,7,5,3]
sorted_list=sorted(new_list)
print(sorted_list)


#sort() change the original list
fruits_list=["Banana","Ananas", "Lemon"]
fruits_list.sort()
print(fruits_list)

#index(element) and it returns you the index of the element
list1=[5,10,20,25,30,35]
if 20 in list1:
        index_found=list1.index(20)
        list1.insert(index_found,200)
        list1.remove(20)
        print(list1)
else:
        print("element not found")
