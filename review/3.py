def find_vowels(strings):
    if not strings.islower():
        raise ValueError
    d = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letters in strings:
        for vowels in d:
            if letters == vowels:
                d[vowels] += 1
    return d


words = input('type words: ')
print(find_vowels(words))