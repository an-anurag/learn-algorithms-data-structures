"""
Compress string eg- AABBBC - A2B3C1
"""

st = "AAAB"

# approach 2 with dicts/hash

count = {}

for c in st:
    if c not in count.keys():
        count[c] = 1
    else:
        count[c] += 1

print(count)

# method 3


# approach 1
i = 1
out = ''
count = 1
while i < len(st):
    current = st[i]
    pre = st[i - 1]
    if current == pre:
        count += 1
    else:
        out += pre + str(count)
        count = 1
    i += 1
print(out)