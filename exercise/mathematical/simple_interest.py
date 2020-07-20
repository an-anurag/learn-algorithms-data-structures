"""
Simple interest formula is given by:
Simple Interest = (P x T x R)/100
Where,
P is the principle amount
T is the time and
R is the rate
"""

"""
EXAMPLE1:
Input : P = 10000
        R = 5
        T = 5
Output :2500
We need to find simple interest on 
Rs. 10,000 at the rate of 5% for 5 
units of time.

EXAMPLE2:
Input : P = 3000
        R = 7
        T = 1
Output :210
"""

# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.

# We can change values here for
# different inputs
P = 1
R = 1
T = 1

# Calculates simple interest
SI = (P * R * T) / 100

# Print the resultant value of SI
print("simple interest is", SI)
