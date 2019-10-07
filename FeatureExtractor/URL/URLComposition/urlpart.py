import string

well_known_ports = [1, 5, 7, 18, 20, 21, 22, 23, 25, 29, 37, 42, 43, 49, 53, 69, 70, 79, 80, 103, 108, 109, 110, 115,
118, 119, 137, 193, 143, 150, 156, 161, 179, 190, 194, 197, 389, 396, 443, 444, 445, 458, 546, 547, 563, 569, 1080]
url_delimiters = ['.', ',', '/', '=', '-', '_']

class URLpart:
    def __init__(self, url):
        self.url = url.geturl()
        self.protocol = url.scheme
        self.port_number = url.port
        self.is_default_port_number = check_default_port(url.port)
        self.url_letter_count = check_letter_count(url.geturl())
        self.url_delimeter_count = check_url_delimeter_count(url.geturl())
        self.url_digit_rate = check_url_digit_rate(url.geturl())
        self.is_url_encoded = check_url_encoded(url.geturl())
        # self.url_symbols ask for help later

def check_default_port(port: int):
    return port in well_known_ports

def check_letter_count(url: str):
    return sum([1 if c in string.ascii_letters else 0 for c in url])

def check_url_delimeter_count(url: str):
    return sum([1 if c in url_delimiters else 0 for c in url])

def check_url_digit_rate(url: str):
    return sum([1 if c in string.digits else 0 for c in url]) / (check_letter_count(url) if check_letter_count(url) != 0 else 1)

def check_url_encoded(url: str):
    return '%' in url
