#Challenge 1
user_number=int(input("Enter an integer number: "))
user_length=int(input("Enter a length: "))
multiples = []

for i in range(1,user_length+1):
    multiples.append(i*user_number)
print(multiples)

#Challenge 2
user_sequence= input("enter a string: ")

if user_sequence:
    result = user_sequence[0]

    for char in user_sequence[1:]:
        if char != result[-1]:  # Compare with last added character
            result += char

    print("Modified string:", result)
else:
    print("You entered an empty string.")