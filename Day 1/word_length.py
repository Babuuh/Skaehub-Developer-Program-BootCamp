sentence = str(input('enter a string: '))


def length_of_last_word(sentence):
    words = sentence.split()

    if len(words) == 0:
        return 0
    else:
        return len(words[-1])

print(length_of_last_word(sentence))
