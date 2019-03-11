import re
str = "hi 123 and 456789 ok 1738 and 375 fine"

t = re.findall(r'\b(?:\d{2})+\b', str)
print t
