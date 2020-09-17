#!/usr/bin/python3

sentence = 'the quick brown fox jumps over the lazy dog'
words = sentence.split()
words_length = []
for word in words:
    if word != 'the':
        words_length.append(len(word))
print(words)
print(words_length)

words_length2 = []
words_length2 = [len(word) for word in words if word != 'the']

# I don't like list comprehensions because they make code harder to read
