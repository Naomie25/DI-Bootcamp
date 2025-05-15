#Challenge 1: Sorting
#STEP 1
user_sequence= input("Enter a sequence separated by comas\n")

#STEP 2
my_list=user_sequence.split(",")
print(my_list)

#STEP 3
my_list.sort()
print(my_list)

#STEP 4
sorted_words_sequence = ",".join(my_list)

#STEP 5
print(sorted_words_sequence)

# Challenge 2: Longest Word
def get_longest_word(sentence):
    words_sentence=sentence.split(' ')
    longest_len=0
    longest_word=""

    for each_word in words_sentence:
        current_length = len(each_word)
        if current_length>longest_len:
            longest_len=current_length
            longest_word=each_word
    print(f'The longest word is {longest_word}')

get_longest_word("My name is Naomie Marciano ")