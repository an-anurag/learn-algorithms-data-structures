"""

l = [1,2,3,[4,3,21,[23,45],56],100]
 
# 4,45,56,100

"""

def get_last_ele(nums):
    if nums:
        return nums[-1]
    
    for item in nums:
        if isinstance(item, list):
            get_last_ele(item)




# employee names, third max salary

"""
SELECT name from employee where salary < (SELECT max(salary) from employee);
"""