# IV.Write a program to return below output from given input (with and without uses of inbuilt function)
# Input -  "My name is Suraj"
# output - "Suraj is name My"

def reverse(string):
    stack =[]

    for word in string.split():
        stack.append(word)
        
    reversed_words = []
    while stack:
        reversed_words.append(stack.pop())

    reversed_string = " ".join(reversed_words)
    return (reversed_string)

input_str=input("Enter the sentence: ")
print(reverse(input_str))