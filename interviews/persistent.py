

# fib 

def fiboacchi(nums):
    if nums == 0:
        return 0
    if nums == 1:
        return 1
    
    return fiboacchi(nums - 1) + fiboacchi(nums - 2)

