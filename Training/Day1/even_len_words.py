"""
Counts the words with length as even integer for the given string.
"""

ip_str = raw_input('Enter the input string : ')
words = ip_str.split()
op_words = []
for word in words:
    if len(word) % 2 == 0:
        op_words.append(word)

print 'even number of words in {0} are : {1} '.format(ip_str, len(op_words))
