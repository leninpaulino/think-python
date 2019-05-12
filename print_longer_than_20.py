def print_longer_than_20():
    fin = open('words.txt')
    for word in fin:
        if len(word.strip()) > 20:
            print(word)

print_longer_than_20()
