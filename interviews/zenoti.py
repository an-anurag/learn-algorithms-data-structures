# find 3 largest odd number


# find 4th smallest smallest number


# find the second duplicate

my_list = [12, 3, 15, 23, 56, 4, 3, 10, 15, 4]

duplicate = []

for i in range(len(my_list)):

    # check if list has 2 elements, 
    # if so then print the last number
    if len(duplicate) == 2:
        print(duplicate[-1])
        break

    # current number
    num = my_list[i]
    
    # look forward excluding the current number
    for j in my_list[i + 1:]:
        
        if num == j:
            # found duplicate, add to duplicate list
            duplicate.append(num)

