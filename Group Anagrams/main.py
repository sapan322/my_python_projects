def group_anagrams(words):
    """
    A function that groups words that use the same letters called "anagrams"
    """

    alphabet_dict = {}
    anagrams = []

    #Sort words in alphabetical order
    for word in words:
        alphabetic_key = "".join(sorted(word))
        if alphabetic_key in alphabet_dict:
            alphabet_dict[alphabetic_key].append(word)
        else:
            alphabet_dict[alphabetic_key] = [word]

    #Return anagrams from dictionary
    for value in alphabet_dict.values():
        anagrams.append(value)

    return anagrams

if __name__ == '__main__':
    print(group_anagrams(["cat", "act", "tea", "eat", "moon"]))

