"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


# print("this is a debug message")

def solution(A):

    sorted_arr = sorted(A)
    max_el = sorted_arr[len(sorted_arr) - 1]
    ref_list = range(min(sorted_arr), max(sorted_arr) + 1)
    absent = []
    for i in ref_list:
        ele = i
        if ele not in sorted_arr:
            absent.append(ele)

    if not absent:
        if max_el + 1 == 0:
            print(max_el)
            return max_el + 2
        else:
            return max_el + 1
    elif absent[0] < 0:
        return max_el + 2


a = [1, 3, 6, 4, 1, 2]
print(solution(a))

