"""
1. Minimum Sum
Given an array of integers, perform some number k of operations. Each operation consists of removing an element
from the array, dividing it by 2 and inserting the ceiling of that result back into the array. Minimize the sum of the
elements in the final array.
Example:
nums = [10, 20, 7]
k=4
Pick Pick/2 Ceiling
Initial array
7
3.5
10 5
20 10 10
4
Result
[10, 20, 7]
[ 10, 20, 47
[5, 20, 4]
(5, 10, 4]
(5, 5, 41
5
10
5
5
The sum of the final array is 5 + 5+ 4 = 14, and that sum is minimal.
Function Description
Complete the function minSum in the editor below.
minsum has the following parameters:
int nums[n: an array of integers, indexed 0 to n-1
int k: an integer
Returns
int: the minimum sum of the array after k steps

"""


#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY num
#  2. INTEGER k
#

def minSum(num, k):
    # Write your code here
    sorted_nums = sorted(num)
    result = []
    for i in range(k):
        for j in range(len(sorted_nums)):
            current_el = sorted_nums.pop(j)
            current_ceil = math.ceil(current_el / 2)
            sorted_nums.append(current_ceil)
            result.append(sum(sorted_nums))

    return min(result)

minSum([10, 20, 7], 4)