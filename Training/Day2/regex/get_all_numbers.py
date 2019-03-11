import re
ip_str = raw_input('Please enter a string : ')
nums = re.findall(r'\s\d+\s', ip_str)

res = 0
for num in nums:
    res = res + int(num)

print(res)
