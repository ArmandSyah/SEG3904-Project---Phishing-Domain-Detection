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
        self.domain_symbol_count = check_domain_symbol_count(domain)

def check_domain_delimeter_count(domain: str):
    return sum([1 if c in url_delimiters else 0 for c in domain])

def check_letter_count(domain: str):
    return sum([1 if c in string.ascii_letters else 0 for c in domain])

def check_domain_digit_rate(domain: str):
    return sum([1 if c in string.digits else 0 for c in domain]) / (check_letter_count(domain) if check_letter_count(domain) != 0 else 1)

def check_port_in_domain(domain: str):
    return 1 if re.search(':\d+', domain) else 0

def check_domain_symbol_count(domain: str):
    percent_encoded = r'%[0-9a-fA-F]{2}'
    return len(re.findall(percent_encoded, domain))