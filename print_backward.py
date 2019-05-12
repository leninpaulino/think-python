def print_backward(word):
    index = len(word)
    while index > 0:
        index = index - 1 
        letter = word[index]
        print(letter)


print_backward('Shark')