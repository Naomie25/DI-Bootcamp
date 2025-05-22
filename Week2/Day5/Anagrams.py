from Anagram_checker import AnagramChecker

def User_Interface():
   while True:
        print("\nMenu:")
        print("1. Input a word")
        print("2. Exit")
        choice = input("Choose an option (1 or 2): ").strip()

        if choice == '1':
            user_input = input("Enter a single word: ").strip()

            # Check if only one word was entered
            if len(user_input.split()) != 1:
                print("Error: Please enter exactly one word.")
                continue

            # Check if the word contains only alphabetic characters
            if not user_input.isalpha():
                print("Error: Only alphabetic characters are allowed.")
                continue
            file_path="/Users/naomiemarciano/Desktop/DI-Bootcamp/Week2/Day5/sowpods.txt"
            anagram=AnagramChecker(file_path)
            # If valid, you can now call is_valid_word or other methods
            if anagram.is_valid_word(user_input):
                our_list=anagram.get_anagrams(user_input)
                print(f"'{user_input}' is a valid word.Anagrams for your word: {our_list}")
            else:
                print(f"'{user_input}' is NOT a valid word.")

        elif choice == '2':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1 or 2.")

User_Interface()

      
