class Parser:    
    def __init__(self, tokens):
        self.tokens = iter(tokens) 
        self.current_token = None
        self.next_token()

    def next_token(self):
        self.current_token = next(self.tokens, None)
    
    def parse_expression(self):
        # E -> TE'
        value = self.parse_term()
        return self.parse_expression_prime(value)

    def parse_expression_prime(self, val):
    # E' -> +TE' | -TE' | ε
        if self.current_token in ('+', '-'):
            op = self.current_token
            self.next_token()
            value = self.parse_term()
            if op == '+':
                val += value
            else:
                val -= value
            return self.parse_expression_prime(val)
        return val 


    def parse_term(self):
        # T -> FT'
        value = self.parse_factor()
        return self.parse_term_prime(value)
    
    def parse_term_prime(self, val):
    # T' -> *FT' | /FT' | ε
        if self.current_token in ('*', '/'):
            op = self.current_token
            self.next_token()
            value = self.parse_factor()
            if op == '*':
                val *= value
            else:
                val /= value
            return self.parse_term_prime(val)
        return val  # Return the current value if no more * or / is found

    
    def parse_factor(self):
        # F -> (E) | integer
        if self.current_token == '(':
            self.next_token()
            value = self.parse_expression()
            if self.current_token == ')':
                self.next_token()
                return value
            else:
                raise ValueError('Expected )')
        elif self.current_token.isdigit():
            value = int(self.current_token)
            self.next_token()
            return value
        else:
            raise SyntaxError()

