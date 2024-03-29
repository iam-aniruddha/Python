"""
# IV.Write a program to return below output from given input 
(without uses of inbuilt function)
# Input -  "My name is Suraj"
# output - "Suraj is name My"
"""

import decorator

@decorator.log_decorator
def reverse(string):
    """Function that takes input string and returns the reverse of it"""
    stack =[]

    for word in string.split():
        stack.append(word)

    reversed_words = []
    while stack:
        reversed_words.append(stack.pop())

    reversed_string = " ".join(reversed_words)
    return reversed_string

input_str=input("Enter the sentence: ")
print(reverse(input_str))
