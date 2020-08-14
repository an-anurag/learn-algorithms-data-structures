"""
Write a function that evaluates if a given string is valid roman numerals. If valid, return the “Valid”  else return the rule number.
The number will be between 1 and 3999 (both included)
“v”=5 “x”=10 “L”= 50 “C”=100  “D”=500 “M”=1000

Rules
can contain only the roman numeral characters.
No numeral character can repeat more than 3 times.
“I” can be subtracted from “v” and “x” only. “x” can be subtracted from “L” and “C”
4. Subtraction can be done only once.

Examples:
Xxviii=38 hence return “valid”
LIV=44 hence return “Valid”
XL=Violates 1st rule hence return “1”
Xiii= vilolates 2nd rule hence return “2”

"""