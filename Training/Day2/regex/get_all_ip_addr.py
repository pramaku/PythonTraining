import re

str = "hello hi 10.34.45.67"

pattern = r'(\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b)'
t = re.findall(pattern, str)
print t
