n, m, q = map(int, input().split())

table = {}

for symbol in input().split():
    table[symbol] = {}

for row in range(1, n + 1):
    values = [int(value) for value in input().split()]

    counter = 0
    for symbol in table.keys():
        table[symbol][row] = values[counter]
        counter += 1


def is_greater(number1, number2):
    return number1 > number2


def is_less(number1, number2):
    return number1 < number2


condition_functions = {
    '>': is_greater,
    '<': is_less
}

conditions = {}

for _ in range(q):
    symbol, condition, number = input().split()
    number = int(number)

    if conditions.get(symbol, None):
        index = 0 if condition == '>' else 1
        if not conditions[symbol][index] or condition_functions[condition](number, conditions[symbol][index]):
            conditions[symbol][index] = number
    else:
        conditions[symbol] = [number, None] if condition == '>' else [None, number]

delete_keys = set()

print(conditions.keys())
print(conditions)

for symbol in conditions.keys():
    for key in table[symbol].keys():
        if (conditions[symbol][0] and not (conditions[symbol][0] < table[symbol][key])) \
                or (conditions[symbol][1] and not (conditions[symbol][1] > table[symbol][key])):
            delete_keys.add(key)

for symbol in table.keys():
    [table[symbol].pop(key) for key in delete_keys]

result = 0
for symbol in table.keys():
    for key in table[symbol].keys():
        result += table[symbol][key]

print(result)
