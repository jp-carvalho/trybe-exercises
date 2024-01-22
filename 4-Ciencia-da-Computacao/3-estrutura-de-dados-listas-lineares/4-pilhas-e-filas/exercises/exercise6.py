from exercise3 import Stack


def solve_expression(expr):
    stack = Stack()
    tokens_list = expr.split(" ")

    for token in tokens_list:
        if token == "+":
            # Sum op
            result = stack.pop() + stack.pop()
            stack.push(result)
        elif token == "*":
            # multiply
            result = stack.pop() * stack.pop()
            stack.push(result)
        elif token == "-":
            # minus op
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 - op2
            stack.push(result)
        elif token == "/":
            # division
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 / op2
            stack.push(result)
        else:
            # add the number op
            stack.push(int(token))

    return stack.pop()

    # A = 5, B = 10, C = 30


# A + B - C / A -> 5 10 + 30 5 / -
print(solve_expression("5 10 + 30 5 / -"))  # 9

# B + (A * C) / C * 2 -> 10 5 30 * 30 / 2 * +
print(solve_expression("10 5 30 * 30 / 2 * +"))  # 20

# A * B - C + 4 * A - B -> 5 10 * 30 - 4 5 * 10 - +
print(solve_expression("5 10 * 30 - 4 5 * 10 - +"))  # 30

# (A + C / B ) * (A + B) -> 30 10 / 5 + 5 10 + *
print(solve_expression("30 10 / 5 + 5 10 + *"))  # 120

# 50 * B / 2 * 5 / A -> 50 10 * 2 / 5 * 5 /
print(solve_expression("50 10 * 2 / 5 * 5 /"))  # 250
