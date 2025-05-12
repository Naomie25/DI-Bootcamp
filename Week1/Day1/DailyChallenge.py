import random
string= input("Hi enter a string\n")
if len(string)<10:
    print("String not long enough.")
elif len(string)>10:
    print("String too long.")
else:
    print("Perfect string")
last_index=len(string)
print("The first character is: "+ string[0]+" and the last character is: "+string[len(string)-1]) 

for i in range(1, len(string) + 1):
    print(string[:i])


our_list = list(string)

# Shuffle the list
random.shuffle(our_list)

shuffled_string = ''.join(our_list)

print("Shuffled string:", shuffled_string)