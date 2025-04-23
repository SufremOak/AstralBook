import math

class ExpressionEvaluator:
    def __init__(self):
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y,
            'sqrt': lambda x: x ** 0.5,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log
        }

    def evaluate(self, expression):
        tokens = self._tokenize(expression)
        return self._evaluate_expression(tokens)

    def _tokenize(self, expression):
        tokens = []
        current = ''
        for char in expression:
            if char.isspace():
                if current:
                    tokens.append(current)
                    current = ''
            elif char in '+-*/^()':
                if current:
                    tokens.append(current)
                    current = ''
                tokens.append(char)
            else:
                current += char
        if current:
            tokens.append(current)
        return tokens

    def _evaluate_expression(self, tokens):
        stack = []
        for token in tokens:
            if token in self.operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self.operators[token](operand1, operand2)
                stack.append(result)
            elif token.replace('.','',1).isdigit():
                stack.append(float(token))
            elif token in ['sin', 'cos', 'tan', 'sqrt', 'log']:
                operand = stack.pop()
                result = self.operators[token](operand)
                stack.append(result)
        return stack[0]


class BasicOperations:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def add(self):
        return self.x1 + self.y1

    def subtract(self):
        return self.x1 - self.y1

    def multiply(self):
        return self.x1 * self.y1

    def divide(self):
        return self.x1 / self.y1

    def power(self):
        return self.x1 ** self.y1

    def root(self):
        return self.x1 ** (1 / self.y1)

    def log(self):
        return math.log(self.x1, self.y1)

    def log10(self):
        return math.log10(self.x1)

    def log2(self):
        return math.log2(self.x1)

    def sqrt(self):
        return math.sqrt(self.x1)
