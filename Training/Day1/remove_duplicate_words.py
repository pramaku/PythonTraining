"""
Removes the duplicate words in the given string and prints the result.
"""

ip_str = raw_input('Enter the input string : ')
words = ip_str.split()
op_words = []
for word in words:
    if word not in op_words:
        op_words.append(word)

print(' '.join(op_words))
