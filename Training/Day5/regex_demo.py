import re

"""
.*  -> greedy
.*? -> non greedy (minimum give high priority)
?= -> look aead positively
?! -> look age
\B -> digit boundary.
"""

s = 'okABCDAXYZXYZBCDAXDhello'

pat = r'A.*?D'
pat1 = r'A.*D'

result = re.findall(pat, s)

print result

result = re.findall(pat1, s)
print result

s1 = "hi 234 sdhj 567 sdsh 3456 kddfjdhf 456678 fdjfh 5677"
pat3 = r'\d{3,4}\s(?=\d+)'
result = re.findall(pat3, s1)
print result

pat4 = r'\d{3,4}\s(?!=\d+)'
result = re.findall(pat4, s1)
print result


s = "h"
pat=r'(?:\b|\B)\d+(?:\b\B)'

match = re.search(r'([a-z]+)\s(\d+)')
match.groups()
