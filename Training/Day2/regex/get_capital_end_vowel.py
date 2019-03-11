import re
ip_str = raw_input('Please enter a string : ')

matches = re.findall(r'\b[A-Z]\w+[aeiou]\b', ip_str)
for match in matches:
    print match
