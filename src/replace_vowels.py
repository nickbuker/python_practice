def replace_exclamation(s):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for vowel in vowels:
        s = s.replace(vowel, "!")
    return s
