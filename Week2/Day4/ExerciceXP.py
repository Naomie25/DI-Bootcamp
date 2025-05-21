#Exercise 1: Random Sentence Generator
import random
file_path="/Users/naomiemarciano/Desktop/DI-Bootcamp/Week2/Day 4/words.txt"
def get_words_from_file(file_path):
    try:
        with open(f'{file_path}','r',encoding='utf-8') as our_file:
            words = our_file.read().split()
            return words
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []
print(get_words_from_file(file_path))

def get_random_sentence(sentence_length):
    ours_words=get_words_from_file(file_path)
    if not ours_words:
        return "No words available."

    # Vérifie que la longueur demandée est raisonnable
    if sentence_length < 1:
        return "Length must be at least 1."
    
    sentence_words = [random.choice(ours_words) for _ in range(sentence_length)]
    sentence = ' '.join(sentence_words).lower()
    return sentence

def main():
    print("Hello! This program generates a random sentence using words from a file")
    try:
        user_length= input("enter sentence length: ")
        sentence_length = int(user_length)

        if sentence_length < 2 or sentence_length > 20:
            print("Error: Please enter a number between 2 and 20.")
            return

        sentence= get_random_sentence(sentence_length)
        print("Generated sentence:")
        print(sentence)

    except ValueError:
        print("Error: That was not a valid number.")

main()

#Exercise 2: Working with JSON
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data=json.loads(sampleJson)
salary=data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

data["company"]["employee"]["birth_date"] = "1992-03-15"
print(json.dumps(data, indent=4))

with open("modified_sample.json", "w") as f:
    json.dump(data, f, indent=4)

print("JSON file saved as 'modified_sample.json'")
    

