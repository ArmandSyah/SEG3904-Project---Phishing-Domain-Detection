import re
import string

class PathPart:
    def __init__(self, path):
        self.path = path
        self.path_letter_count = check_letter_count(path)
        self.path_digit_rate = check_path_digit_rate(path)
        self.path_symbol_count = check_domain_symbol_count(path)

def check_letter_count(path: str):
    return sum([1 if c in string.ascii_letters else 0 for c in path])

def check_path_digit_rate(path: str):
    return  sum([1 if c in string.digits else 0 for c in path]) / (check_letter_count(path) if check_letter_count(path) != 0 else 1)

def check_domain_symbol_count(path: str):
    percent_encoded = r'%[0-9a-fA-F]{2}'
    return len(re.findall(percent_encoded, path))