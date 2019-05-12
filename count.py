def count(word, to_count):
    count = 0
    for letter in word:
        if letter == to_count:
            count = count + 1
    print(count)


count('banana', 'a')
