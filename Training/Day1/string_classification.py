"""
Classisfy the given input strings by thoer length and
number of the words in each string
"""

count = int(raw_input('Enter the count of strings to be used : '))

ip_str = []
for x in range(count):
    ip_str.append(raw_input('enter the string : '))

strings_len_class = {}
strings_words_class = {}

for item in ip_str:
    length_total = len(item)
    if length_total in strings_len_class:
        strings_len_class[length_total].append(item)
    else:
        strings_len_class[length_total] = []
        strings_len_class[length_total].append(item)
    word_count = item.split()
    word_count_length = len(word_count)
    if word_count_length in strings_words_class:
        strings_words_class[word_count_length].append(item)
    else:
        strings_words_class[word_count_length] = []
        strings_words_class[word_count_length].append(item)

for x,y in strings_len_class.items():
    print "String's with lenth of ", x
    for z in y:
        print '-- ', z
    print '-' * 50

print
print

for x, y in strings_words_class.items():
    print "String's with {0} words".format(x)
    for z in y:
        print '-- ', z
    print '-' * 50
