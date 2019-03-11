"""
Word search application:
    User will be entering 'n' number of strings at start.
    Then user can given ny word to search if the given word is part of any string.
    if there is a match, the length of the string and the string itselfis printed.
    use 'quit' to stop searching and exit from app.
"""

count = int(raw_input('Enter the count of strings to be used : '))

ip_str = []
for x in range(count):
    ip_str.append(raw_input('enter the string : '))

word_index = {}

for item in ip_str:
    words = item.split()
    for word in words:
        if word not in word_index:
            word_index[word] = []
            word_index[word].append(item)
        else:
            word_index[word].append(item)

result = {}
word = raw_input("enter any word to search (enter 'quit' to exit) : ")
while word != 'quit':
    if word in word_index:
        values = word_index[word]
        for val in values:
            print len(val), ' : ', val
    else:
        print 'Sorry no match, please try agian !!!'
    word = raw_input("enter any word to search (enter 'quit' to exit) : ")

print 'Thanks for using search app.. bye :) '
