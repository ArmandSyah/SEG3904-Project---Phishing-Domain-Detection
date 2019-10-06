import string

url_delimiters = ['.', ',', '/', '=', '-', '_']

class QueryPart:
    def __init__(self, query: dict,  *args, **kwargs):
        self.query = query

        if not query:
            self.query_deli_count = 0
            self.avg_var_letter_count = 0
            self.avg_value_letter_count = 0
            self.avg_var_len = 0
            self.query_value_max_token = 0
            self.query_var_max_token = 0
            self.sum_var_len = 0
            self.query_letter_count = 0
        else:
            self.query_deli_count = check_query_delimeter_count(query)
            self.avg_var_letter_count = average_letter_count(query.keys())
            self.avg_value_letter_count = average_letter_count(query.values())
            self.avg_var_len = average_variable_length(query.keys())
            self.query_value_max_token = longest_token(query.values())
            self.query_var_max_token = longest_token(query.keys())
            self.sum_var_len = sum( [len(q) for q in query.keys()] )
            self.query_letter_count = check_query_letter_count(query)
        

def check_domain_delimeter_count(domain: str):
    return sum([1 if c in url_delimiters else 0 for c in domain])

def check_letter_count(domain: str):
    return sum([1 if c in string.ascii_letters else 0 for c in domain])

def check_domain_digit_rate(domain: str):
    return sum([1 if c in string.digits else 0 for c in domain]) /  check_letter_count(domain)

def check_query_delimeter_count(query: dict):
    var_count, val_count = 0,0
    for var, val in query.items():
        var_count += check_domain_delimeter_count(var)
        val_count += check_domain_delimeter_count(val)
    return var_count + val_count

def average_letter_count(input: list):
    return sum([check_letter_count(word) for word in input]) / len(input)

def average_variable_length(input: list):
    return sum([len(word) for word in input]) / len(input)

def longest_token(input: list):
    return max([len(word) for word in input])

def check_query_letter_count(query: dict):
    var, val = query.keys(), query.values()
    return sum(check_letter_count(v) for v in var) + sum(check_letter_count(v) for v in val)