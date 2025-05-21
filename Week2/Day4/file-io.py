# FILE IO: INPUT/OUTPUT
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
#Old way to open a file
# file_object=open("Week2/Day 4/secrets.txt")
# for i in file_object:
#     print(i)

#MODERN PYTHON WAY TO OPEN A FILE
# with open("Week2/Day 4/secrets.txt", encoding='utf -8') as file_obj:
    #output= file_obj.read() # return the whole content of the file
    #output=file_obj.readline() # returns one line
    # output=file_obj.readlines() # returns a list where each line is the element
    # print(output)


#Exercice
with open(f'{dir_path}/star_wars.txt', encoding='utf-8') as our_file:
    lines = our_file.readlines()  # Lire toutes les lignes une seule fois
    
# Afficher toutes les lignes (optionnel)
for line in lines:
    print(line.strip())

# Vérifier qu'il y a au moins 5 lignes
if len(lines) >= 5:
    fifth_line = lines[4].strip()
    print(f'\nThe content of the 5th line is: {fifth_line}')
else:
    print("The file has less than 5 lines.")

with open("Week2/Day 4/secrets.txt",'a', encoding='utf -8') as file_obj:
    file_obj.writelines("\n Hello Python I/O")




