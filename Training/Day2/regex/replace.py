import re

s = 'hi 1234 and 56789 ok'
pattern = raw_input('Enter some pattern')

s1 = re.sub(pattern, "replace_str", s)  # replace all the strings not just the first occurrence.
print s1

s1 = re.sub(pattern, "replace_str", s, 1)  # replace strings only one occurrence.

t = re.subn(pattern, "replace_str", s)  # returns tuple with replaced string and n number of matches
