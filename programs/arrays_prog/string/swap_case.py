def swap_case(st):
    res = ""
    for ch in st:
        if ch.isupper():
            low = ch.lower()
            res += low
        elif ch.islower():
            up = ch.upper()
            res += up
        else:
            res += ch
    return res


result = swap_case("AnuragG panDit")
print(result)