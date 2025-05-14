import re

# Matrix string provided
MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%'''

# Step 1: Convert MATRIX_STR into a 2D list (matrix)
matrix_2d = [list(line) for line in MATRIX_STR.strip().splitlines()]

# Step 2
rows = len(matrix_2d)
cols = len(matrix_2d[0])
temp_string = ''

# Iterate over each column
for col in range(cols):
    for row in range(rows):
   # Step 3: Filtering alpha   
        if matrix_2d[row][col].isalpha():
            temp_string += matrix_2d[row][col]
        else:
            #Step 4: Replacing Symbols with Spaces
            if temp_string and temp_string[-1] != ' ':
                temp_string += ' '



decoded_message = temp_string.strip()

# Step 5: Print the decoded message
print(f"Decoded message: {decoded_message}")
