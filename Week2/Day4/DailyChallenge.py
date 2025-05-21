import string
import re
class Text:
    def __init__(self,text):
        self.text=text
    
    def word_frequency(self, word):
        cleaned_text = self.text.lower().translate(str.maketrans('', '', string.punctuation))
        words = cleaned_text.split()

        word = word.lower()

        count = words.count(word)
        if count > 0:
            return count
        else:
            return f"The word '{word}' was not found in the text."

        
    def most_common_word(self):
        words = self.text.lower().split()  # Met tout en minuscules et découpe en mots
        freq = {}

        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        most_common = None
        max_count = 0

        for word, count in freq.items():
            if count > max_count:
                max_count = count
                most_common = word

        return most_common
    
    def unique_words(self):
        cleaned_text = self.text.lower().translate(str.maketrans('', '', string.punctuation))
        words = cleaned_text.split()
        return sorted(set(words))
    
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return cls(content)

    def remove_punctuation(self):
        no_punct = ''.join(char for char in self.text if char not in string.punctuation)
        return no_punct
    
    def remove_stop_words(self):
        # Liste de stop words en anglais
        stop_words = {
            'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you',
            'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his',
            'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself',
            'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
            'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
            'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having',
            'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
            'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for',
            'with', 'about', 'against', 'between', 'into', 'through', 'during',
            'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
            'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',
            'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how',
            'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other',
            'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
            'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',
            'should', 'now'
        }

        # Supprimer la ponctuation
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = self.text.translate(translator)

        # Diviser le texte en mots
        words = cleaned_text.split()

        # Filtrer les stop words
        filtered_words = [word for word in words if word.lower() not in stop_words]

        # Reconstituer le texte
        return ' '.join(filtered_words)
    
    def remove_special_characters(self):
        # Remplace tout ce qui n'est pas une lettre, un chiffre ou un espace par ''
        cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return cleaned_text
    

# Sample text
sample_text = """Hello! This is a simple test. This test is only a test.
Hello again, world... Let's see how many times the word 'test' appears!
Also, let's remove punctuation and stop words."""

# Create a Text instance
text_instance = Text(sample_text)

print("\n--- Original Text ---")
print(text_instance.text)

print("\n--- Word Frequency ('test') ---")
print(text_instance.word_frequency('test'))

print("\n--- Most Common Word ---")
print(text_instance.most_common_word())

print("\n--- Unique Words ---")
print(text_instance.unique_words())

print("\n--- Text Without Punctuation ---")
print(text_instance.remove_punctuation())

print("\n--- Text Without Stop Words ---")
print(text_instance.remove_stop_words())

print("\n--- Text Without Special Characters ---")
print(text_instance.remove_special_characters())


