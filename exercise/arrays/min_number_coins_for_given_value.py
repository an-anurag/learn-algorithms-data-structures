"""
Write a function to deduce the minimum number of coins required to complete the change value
eg: coins = [9, 6, 5, 1] change value V = 11
here mum number of coins required is 2 (6 + 5)
"""


def min_number_of_coins(coins, value):

    sorted_coins = sorted(coins)
    counter = 0
    # import pdb; pdb.set_trace()
    while counter <= len(sorted_coins):

        temp = []
        print(temp)
        inc = counter + 1
        while sum(temp) <= value:
            temp.append(sorted_coins[inc])
            inc += 1
        counter += 1
        return temp


c = [9, 6, 5, 1]
print(min_number_of_coins(c, 11))