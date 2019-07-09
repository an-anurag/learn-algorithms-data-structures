import random
import string

exp_sent = 'methinks it is like a weasel'


def sentance_generator():
    res = ''
    alphbets = string.ascii_lowercase + ' '
    for i in random.shuffle(alphbets):
        res = res + alphbets[i]
    return res


res = sentance_generator()
print(res)

print(random.randrange(1, 10, 2))
