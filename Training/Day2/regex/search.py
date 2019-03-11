import re

s = 'hi 1234 and 56789 ok'

pattern = raw_input('Enter some pattern')
if re.search(pattern, s):
    print('found')
else:
    print('not found')
