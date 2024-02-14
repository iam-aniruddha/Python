# V.Write a program to print fibonacci series for the given input occurence (if user gives i\p as 6 then it should print series till 6th number)
# FiBoNACCI series
# 0 1 1 2 3 5 8 13 21
 
# Input: 6, Output: 0 1 1 2 3 5
# Input: 10, Output: 0 1 1 2 3 5 8 12 21 34

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input("Enter the number of terms: "))
if n<=0:
    print("Please enter a positive integer")
else:
    print("Fibonacci Sequence is: ")
    for i in range(1, n+1):
        print(fibonacci(i), end=" ")