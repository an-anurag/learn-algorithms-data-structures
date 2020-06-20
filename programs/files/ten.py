file = open("test.txt", "r")
contents = file.read().split()
frequency = dict()
counter = 1
for word in contents:
    if word not in frequency.keys():
        frequency[word] = counter
    else:
        frequency[word] = counter + 1

print(frequency)
