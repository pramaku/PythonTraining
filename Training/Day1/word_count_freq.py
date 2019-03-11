"""
Caluculates the frequncy of each word in the given string.
Also prints which word exits more number of times and which word is
used least number of times
"""

ip_str = raw_input('Enter the input string : ')
words = ip_str.split()
op_words_count = {}
for word in words:
    if word in op_words_count:
        op_words_count[word] = op_words_count[word] + 1
    else:
        op_words_count[word] = 1
print(op_words_count)

word_count = op_words_count.values()
most_len = max(word_count)
min_len = min(word_count)

for x, y in op_words_count.items():
    if y == most_len:
        print 'Max ', x
        break

for x, y in op_words_count.items():
    if y == min_len:
        print 'Min ', x
        break
