from itertools import permutations


def calculate(op1, op2, operator):
    if operator == "+":
        return op1 + op2
    elif operator == "-":
        return op1 - op2
    else:
        return op1 * op2


def process(expression):
    stack = []
    num = ""
    for e in expression:
        if e.isdigit():
            num += e
        else:
            stack.append(int(num))
            num = ""
            stack.append(e)
            operators.add(e)

    stack.append(int(num))
    return stack


def solution(expression):
    global operators
    operators = set()
    exp = process(expression)
    ans = 0

    for p in permutations(operators, len(operators)):
        new_exp = exp
        for i in range(len(p)):
            operator = p[i]
            stack = []

            for op in new_exp:
                stack.append(op)
                if len(stack) >= 3 and stack[-2] == operator:
                    op2 = stack.pop()
                    operator = stack.pop()
                    op1 = stack.pop()
                    stack.append(calculate(op1, op2, operator))

            new_exp = stack
        ans = max(ans, abs(new_exp[0]))

    return ans
