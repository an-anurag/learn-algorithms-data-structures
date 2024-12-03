
# print the occurences of each token in the list sorted alphabetically

given = ['the', 'sun', 'is', 'the', 'rising']

sorted_given = sorted(given)
print(sorted_given)

seen = {}
for w in sorted_given:
    if w in seen:
        seen[w] += 1
    else:
        seen[w] = 1

value_counts = [x for x in seen.values()]
print(value_counts)
