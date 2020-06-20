import random

random_line = random.choice(open('test.txt', 'r').readlines())
print(random_line)
