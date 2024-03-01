from lexer import tokenizer
from recursive_descent_parser import Parser

def main():
    expr = "3 + 5 * (2 - 1) / 5"
    
    tokens = tokenizer(expr)

    parser = Parser(tokens)

    try:
        result = parser.parse_expression()
        print(f"The result of '{expr}' is: {result}")
    except (ValueError, SyntaxError) as e:
        print(f"Error in parsing the expression: {e}")


main()


