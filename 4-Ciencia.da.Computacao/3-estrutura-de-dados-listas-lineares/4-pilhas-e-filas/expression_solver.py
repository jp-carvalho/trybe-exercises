from stack import Stack


def solve_expression(expr):
    stack = Stack()

    tokens_list = expr.split(" ")

    for token in tokens_list:
        if token == "+":
            # Sum operation
            result = stack.pop() + stack.pop()
            stack.push(result)
        elif token == "*":
            # Multiply operation
            result = stack.pop() * stack.pop()
            stack.push(result)
        else:
            # add num operation
            stack.push(int(token))

    return stack.pop()


print(solve_expression("5 10 + 3 *"))
