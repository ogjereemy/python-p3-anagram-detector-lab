# your code goes here!

# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        new_anagrams = []
        
        word_list = sorted([char for char in self.word])
        for word in list:
            if sorted([letter for letter in word]) == word_list:
                new_anagrams.append(word)
        return new_anagrams