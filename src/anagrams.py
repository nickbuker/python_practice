def anagrams(word, words):
    grams = []
    word_sort = sorted(list(word))
    for w in words:
        if sorted(list(w)) == word_sort and word != w:
            grams.append(w)
    return grams
