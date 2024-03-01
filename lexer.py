import re

def tokenizer(expr):
   # Pattern to match integers, floats, and operators
    pattern = r'[-+/*()]|\d+\.\d+|\d+'
    regex = re.compile(pattern)
    
    # Finding all matches
    tokens = regex.findall(expr)
    
    return tokens