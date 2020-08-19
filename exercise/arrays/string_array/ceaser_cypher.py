"""
Ceasar’s  Cypher
Given a simple strings s,encrypt it using key K ,where K= -0.The key K replaces each character using
Example:
When s=”cat”  and “k” is 1 ,the encrypted string is “dbu”
The same string will produce different encrypted strings when k is 2 for s=”cat”
Given an English string s and key k find the encrypted string.

"""
import string

alphbets = string.ascii_lowercase


def encrypt(s, key):
    result = ""

    for i in range(len(s)):
        if s[i] in alphbets:
            sub_index = alphbets.index(s[i])
            result += alphbets[sub_index + key]

    return result


print(encrypt('cat', 2))
