import re
import string

url_delimiters = ['.', ',', '/', '=', '-', '_']

class DomainPart:
    def __init__(self, domain):
        self.domain = domain
        self.domain_deli_count = check_domain_delimeter_count(domain)
        self.domain_letter_count = check_letter_count(domain)
        self.domain_digit_rate = check_domain_digit_rate(domain)
        self.is_port_in_domain = check_port_in_domain(domain)

def check_domain_delimeter_count(domain: str):
    return sum([1 if c in url_delimiters else 0 for c in domain])

def check_letter_count(domain: str):
    return sum([1 if c in string.ascii_letters else 0 for c in domain])

def check_domain_digit_rate(domain: str):
    return check_letter_count(domain) / sum([1 if c in string.digits else 0 for c in domain])

def check_port_in_domain(domain: str):
    return bool(re.search(':\d+', domain))
