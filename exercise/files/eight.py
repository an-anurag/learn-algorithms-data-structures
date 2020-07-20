file = open('test.txt', 'r')
word_list = file.read().split()
element = [el for el in word_list if len(el) == max([len(word) for word in word_list])][0]
print(element)
