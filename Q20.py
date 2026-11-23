# Precedence order: Parentheses -> Exponentiation -> Multiplication/Division -> Addition/Subtraction
expr1 = 10 + 3 * 2 ** 2
expr2 = (10 + 3) * 2 ** 2

print("10 + 3 * 2 ** 2 =", expr1)
print("(10 + 3) * 2 ** 2 =", expr2)