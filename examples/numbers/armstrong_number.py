def is_armstrong(num):
    digits = [int(n) for n in str(num)]
    length = len(digits)
    add = 0
    for n in digits:
        add += n**length
    if add == num:
        print(f"{num} is armstrong number")
    else:
        print(f"{num} is not armstrong number")


is_armstrong(153)


# Python program to check if the number provided by the user is an Armstrong number or not
# take input from the user
num = int(input("Enter a number: "))
# initialize sum
sum = 0
# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")