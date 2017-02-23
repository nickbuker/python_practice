class WordDictionary(object):

    def __init__(self):
        self.d = []

    def add_word(self, word):
        if word not in self.d:
            self.d.append(word)

    def search(self, word):
        if '.' not in word:
            return word in self.d
        else:
            fuzzy_word = self.fuzzy_word(word)
            return self.fuzzy_search(fuzzy_word, word)

    def fuzzy_word(self, word):
        fuzzy_word = {}
        for i, c in enumerate(word):
            if c != '.':
                fuzzy_word[i] = c
        return fuzzy_word

    def fuzzy_search(self, fuzzy_word, word):
        for element in self.d:
            if len(element) != len(word):
                continue
            if len(fuzzy_word) == 0:
                continue
            element_dict = {}
            for i, c in enumerate(element):
                element_dict[i] = c
            test = all(item in element_dict.items() for item in fuzzy_word.items())
            if test:
                return True
        return False
