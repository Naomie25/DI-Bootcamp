
class AnagramChecker:
    
    def __init__(self, word_list_file):
        try:
            with open(word_list_file, 'r', encoding='utf-8') as file:
                # Read all words from file into a list, stripping whitespace and newlines
                self.word_list = [line.strip().lower() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Error: The file '{word_list_file}' was not found.")
            self.word_list = []

    def is_valid_word(self,word):
        word = word.lower()
        return word in self.word_list

    def get_anagrams(self, word):
        word = word.lower()
        sorted_word = sorted(word)
        anagram_list = []

        for each_word in self.word_list:
            if each_word != word and sorted(each_word) == sorted_word:
                anagram_list.append(each_word)
        return anagram_list
    
    def is_anagram(self, word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        return word1 != word2 and sorted(word1) == sorted(word2)

file_path="/Users/naomiemarciano/Desktop/DI-Bootcamp/Week2/Day5/sowpods.txt"
anagram=AnagramChecker(file_path)
our_list= anagram.get_anagrams("meat")
print(our_list)

print(anagram.is_anagram("meat","team"))