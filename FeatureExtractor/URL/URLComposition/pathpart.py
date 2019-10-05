import string

class PathPart:
    def __init__(self, path):
        self.path = path
        self.path_letter_count = check_letter_count(path)
        self.path_digit_rate = check_path_digit_rate(path)

def check_letter_count(path: str):
    return sum([1 if c in string.ascii_letters else 0 for c in path])

def check_path_digit_rate(path: str):
    return check_letter_count(path) / sum([1 if c in string.digits else 0 for c in path])