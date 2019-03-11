import re

s = 'hi 1234 and 56789 ok'
pattern = raw_input('Enter some pattern')
result = re.findall(pattern, s)
print result
