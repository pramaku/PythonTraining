import re
ip_str = raw_input('Please enter a string : ')

def pattern_match(pattern, ip_str):
    matches = re.findall(pattern, ip_str)

    for match in matches:
        print match

pattern_match(r'1|[1-9][0-9]|1[0-9][0-9]|2[0-5][0-5]', ip_str)
