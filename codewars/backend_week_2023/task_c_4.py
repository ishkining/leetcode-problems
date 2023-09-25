def evaluate(condition, row):
    column, operator, value = condition.split()
    value = int(value)

    if operator == '>':
        return row[column] > value
    elif operator == '<':
        return row[column] < value


def calculate_sum(rows, conditions):
    valid_rows = []
    for row in rows:
        if all(evaluate(condition, row) for condition in conditions):
            valid_rows.append(row)

    return sum(sum(row.values()) for row in valid_rows)


n, m, q = map(int, input().split())
columns = input().split()
rows = []
for _ in range(n):
    row_values = input().split()
    row = dict(zip(columns, map(int, row_values)))
    rows.append(row)

print(rows)

conditions = []
for _ in range(q):
    condition = input()
    conditions.append(condition)

result = calculate_sum(rows, conditions)
print(result)
