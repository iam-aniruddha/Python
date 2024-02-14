# I. Given a String of Characters
# 1. Print the three most common characters along with their occurrence count.
# 2. Sort in descending order of occurrence count.
# 3. If the occurrence count is the same for any character, sort the characters in alphabetical order.
# Final Output. 
# Top 3 Characters based on the above critera
# E.g. 
# Input: HAPPIESTMINDS
# Output : 
# I: 2
# P: 2
# S: 2

from collections import Counter

def print_top_characters(s, n=3):
    # Count the frequency of each character
    char_freq = Counter(s)
    # Sort the characters based on their frequency count and alphabetical order
    sorted_char_freq = sorted(char_freq.items(), key=lambda x: (-x[1], x[0]))
    # Print the top n characters and their frequencies
    for i in range(n):
        print(f"{sorted_char_freq[i][0]}: {sorted_char_freq[i][1]}")

# Test the function with the given input
s = input("Enter a String: ")
print_top_characters(s)
