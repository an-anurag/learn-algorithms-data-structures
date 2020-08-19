"""
Currency formatter
Write a function that formats given currency by grouping the digit separated comma. Grouping should be in indian system.
Example:
Input: 1234567
Return: 12,34,567

"""


def formatter(currency):
    str_currency = str(currency)
    currency_lt = len(str_currency)
    last_third = currency_lt - 3
    print(last_third)
    result = ""
    for i in range(currency_lt):
        if not i == last_third:
            if i % 2 == 0:
                result += "," + str_currency[i]
            else:
                result += str_currency[i]


    print(result)



formatter(1234567)