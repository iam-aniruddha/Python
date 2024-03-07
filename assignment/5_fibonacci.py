"""
# Write a program to print fibonacci series for the given input occurence 
(if user gives input as 6 then it should print series till 6th number)
# FiBoNACCI series
# 0 1 1 2 3 5 8 13 21
 
# Input: 6, Output: 0 1 1 2 3 5
# Input: 10, Output: 0 1 1 2 3 5 8 13 21 34
"""
import decorator

@decorator.log_decorator
def fibonacci(n):
    """function that takes input integer and returns the fibonaaci series"""
    if n==1:
        return 0
    if n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

while True:
    try:
        num = int(input("Enter the number of terms: "))
        break
    except ValueError:
        print("Please enter a valid integer")
if num<=0:
    print("Please enter a positive integer")
else:
    print("Fibonacci Sequence is: ")
    for i in range(1, num+1):
        print(fibonacci(i), end=" ")
