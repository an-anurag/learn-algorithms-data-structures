

# sort the dictionary by key

my_dict = {"city": "Pune", "name": "Anurag", "language": "Python", "age": 35}


keys = my_dict.keys()

sorted_key = sorted(keys)

sorted_dict = {}

for key in sorted_key:
    sorted_dict[key] = my_dict[key]

print(sorted_dict)

# {'age': 35, 'city': 'Pune', 'language': 'Python', 'name': 'Anurag'}




# {{ -if .Values.controller.enabled }}

# {{ endif }}

# helm upgrade --install release-name helm-chart-path --set Image

# helm list -n namespace

# deployment

# service

# type Loadbalncer



"""
list a = 1 - 10
list b = 3, 5, 6, 20
"""

a = [1, 2, 9, 10]
b = [3, 5, 6, 20]

combined = a + b

# bubble sort

"""
trverse the list
compare two elements
check whether first number 
if next number is larger previous number swap the position
"""


print(combined)

for i in range(len(combined) - 1):

    print(i)
    current_num = combined[i]
    next_number = combined[i + 1]

    if current_num > next_number:
        current_num, next_number = next_number, current_num


print(combined)
print(sorted(combined)[-1])


combined.sort()
print(combined)


# check palindrome

num = 12321
num2 = 1212

original_str = str(num2)
reversed_str = original_str[::-1]

if original_str == reversed_str:
    print("its parlindrome")
else:
    print("not a palindorome")



# sort the dict based on values
my_dict = {'a': 7, 'b':5, 'c': 9, 'd': 4}

sorted_keys = sorted(my_dict, key=lambda x: my_dict[x])

sorted_dict = {}

for key in sorted_keys:
    sorted_dict[key] = my_dict[key]
    print(my_dict[key])


# {'d': 4, 'b': 5, 'a': 7, 'c': 9}