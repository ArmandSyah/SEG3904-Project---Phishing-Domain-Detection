import re
import string

url_delimiters = ['.', ',', '/', '=', '-', '_']

class QueryPart:
    def __init__(self, queryDict: dict, q: str,  *args, **kwargs):
        self.query = q
        queryDict = {key:value[0] for key,value in queryDict.items()}
        if not queryDict:
            self.query_symbol_count = 0
            self.query_deli_count = 0
            self.avg_value_letter_count = 0
            self.avg_value_symbol_count = 0
            self.avg_var_symbol_count = 0
            self.avg_var_letter_count = 0
            self.avg_var_len = 0
            self.query_value_max_token = 0
            self.query_var_max_token = 0
            self.sum_var_len = 0
            self.query_letter_count = 0
            self.query_digit_rate = 0
            self.query_value_digit_count = 0
            self.query_var_digit_count = 0
        else:
            self.query_symbol_count = check_query_symbol_count(queryDict)
            self.query_deli_count = check_query_delimeter_count(queryDict)
            self.avg_value_letter_count = average_letter_count(queryDict.values())
            self.avg_value_symbol_count = average_symbol_count(queryDict.values())
            self.avg_var_symbol_count = average_symbol_count(queryDict.keys())
            self.avg_var_letter_count = average_letter_count(queryDict.keys())
            self.avg_var_len = average_variable_length(queryDict.keys())
            self.query_value_max_token = longest_token(queryDict.values())
            self.query_var_max_token = longest_token(queryDict.keys())
            self.sum_var_len = sum( [len(q) for q in queryDict.keys()] )
            self.query_letter_count = check_query_letter_count(queryDict)
            self.query_digit_rate = check_query_digit_rate(queryDict) 
            self.query_value_digit_count = sum([1 if c in string.digits else 0 for c in queryDict.values()])
            self.query_var_digit_count = sum([1 if c in string.digits else 0 for c in queryDict.keys()])
        

def check_domain_delimeter_count(domain: str):
    return sum([1 if c in url_delimiters else 0 for c in domain])

def check_letter_count(domain: str):
    return sum([1 if c in string.ascii_letters else 0 for c in domain])

def check_query_digit_rate(query: dict):
    var_digit_count, val_digit_count, var_letter_count, val_letter_count = 0,0,0,0
    for var, val in query.items():
        var_digit_count += sum([1 if c in string.digits else 0 for c in var])
        val_digit_count += sum([1 if c in string.digits else 0 for c in val])
        var_letter_count += check_letter_count(var)
        val_letter_count += check_letter_count(val)
    return (var_digit_count + val_digit_count) / (var_letter_count + val_letter_count)

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

def check_query_symbol_count(query: dict):
    percent_encoded = r'%[0-9a-fA-F]{2}'
    symbol_count = 0
    for var, val in query.items():
        symbol_count += len(re.findall(percent_encoded, var))
        symbol_count += len(re.findall(percent_encoded, val))
    return symbol_count

def average_symbol_count(input: list):
    percent_encoded = r'%[0-9a-fA-F]{2}'
    return sum([len(re.findall(percent_encoded, word)) for word in input]) / len(input)