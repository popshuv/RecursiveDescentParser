from lexer import tokenizer
from recursive_descent_parser import Parser

def main():
    test_cases = [
        "2 + 3",
        "4 * 5",
        "(1 + 2) * 3",
        "7 / (3 + 4) - 2",
    ]

    for expr in test_cases:
        tokens = tokenizer(expr)
        parser = Parser(tokens)
        result = parser.parse_expression()
        print(f"Expression: {expr}, Result: {result}")

main()

