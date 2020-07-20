""" Reverse sentence"""

words = "This is anurag and he is learning data structures"

word_list = []

i = 0
word_length = len(words)

while i < word_length:

    if words[i] != " ":
        word_start = i
        while i < word_length and words[i] != " ":
            i += 1
        word_list.append(words[word_start:i])
    i += 1
print(word_list)

# reverse a word_list to get sentence reversal
print(" ".join(reversed(word_list)))
