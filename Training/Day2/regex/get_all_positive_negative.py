import re
ip_str = raw_input('Please enter a string : ')

def pattern_match(pattern, ip_str):
    matches = re.findall(pattern, ip_str)

    for match in matches:
        print match

pattern_match(r'\b[-]*\d+\d+\b', ip_str)
