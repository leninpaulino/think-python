def find(word, letter, start):
    index = 0
    if 0 < start < len(word):
        index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find('Banana', 'n', 3))