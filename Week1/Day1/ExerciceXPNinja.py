my_text = "Lorem ipsum "
count=len(my_text.replace(" ", ""))
print(count)


#Exercice 5
longest_length = 0

while True:
    sentence = input("Enter the longest sentence you can without the letter 'A': ")

    if 'a' in sentence.lower():
        print("Oops! The sentence contains the letter 'A'. Try again.\n")
        continue

    if len(sentence) > longest_length:
        longest_length = len(sentence)
        print(" Congratulations! That's your new longest sentence without 'A'!\n")
    else:
        print("Nice try, but that wasn't longer than your best.\n")
