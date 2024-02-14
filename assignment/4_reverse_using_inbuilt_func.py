# IV.Write a program to return below output from given input (with and without uses of inbuilt function)
# Input -  "My name is Suraj"
# output - "Suraj is name My"

def reverse_string(s):
    str2 = s.split()
    str2.reverse()
    return " ".join(str2)

input_str = "My name is Suraj"
print(reverse_string(input_str))