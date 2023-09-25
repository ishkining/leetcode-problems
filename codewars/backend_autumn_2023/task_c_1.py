def evaluate_condition(condition, row):
    column, operator, value = condition.split()
    column_index = columns.index(column)
    column_value = row[column_index]
    if operator == '>':
        return column_value > int(value)
    elif operator == '<':
        return column_value < int(value)


N, M, Q = map(int, input().split())
columns = input().split()
rows = []
for _ in range(N):
    rows.append(list(map(int, input().split())))
conditions = []
for _ in range(Q):
    conditions.append(input())

total_sum = 0
for row in rows:
    valid = True
    for condition in conditions:
        if not evaluate_condition(condition, row):
            valid = False
            break
    if valid:
        total_sum += sum(row)

print(total_sum)
