"""
# IV.Write a program to return below output from given input 
(with and without uses of inbuilt function)
# Input -  "My name is Suraj"
# output - "Suraj is name My"
"""

import decorator

@decorator.log_decorator
def reverse_string(s):
    """Function that takes input string and returns the reverse of it"""
    str2 = s.split()
    str2.reverse()
    return " ".join(str2)

INPUT_STR = "My name is Suraj"
print(reverse_string(INPUT_STR))
