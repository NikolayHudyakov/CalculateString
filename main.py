from functools import reduce


def replace_list(string: str) -> tuple[list[int], list[str]]:
    o_list = ['*', '/', '+', '-']
    numbers = reduce(lambda p, c: p.replace(c, ' '), o_list, string).split()
    return list(map(lambda a: int(a), numbers)), reduce(lambda p, c: p.replace(c, ' '), numbers, string).split()


def calculated(expression: str) -> int:
    o_dict = {
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b
    }
    res = replace_list(expression)
    numbers = res[0]
    operations = res[1]
    for key, value in o_dict.items():
        for item in range(operations.count(key)):
            i = operations.index(key)
            numbers[i] = value(numbers[i], numbers[i + 1])
            numbers.pop(i + 1)
            operations.pop(i)
    return numbers[0]


def calc(expression: str) -> int:
    if '(' in expression:
        cls = expression.index(')')
        opn = expression[:cls].rindex('(')
        return calc(expression.replace(expression[opn:cls + 1], str(calculated(expression[opn + 1:cls]))))
    else:
        return calculated(expression)


print(calc('(2 + (2 + 3)) * 2 + 8 * (12 + 54)'))

