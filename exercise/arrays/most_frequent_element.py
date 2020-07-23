"""
Find most frequently occurred element in array
"""

arr = [1, 2, 3, 1, -4, 1, 3]

count = {}
for i in arr:
    if i not in count.keys():
        count[i] = 1
    else:
        count[i] += 1


v_max = max(list(count.values()))
print(list(count.keys())[list(count.values()).index(v_max)])