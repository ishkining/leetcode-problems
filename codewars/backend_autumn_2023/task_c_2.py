def evaluate_conditions(row, conditions):
    for condition in conditions:
        column, operator, value = condition.split()
        if operator == ">":
            if row[column] <= int(value):
                return False
        elif operator == "<":
            if row[column] >= int(value):
                return False
    return True


def evaluate_table(table, conditions):
    total_sum = 0
    for row in table:
        if evaluate_conditions(row, conditions):
            total_sum += sum(row.values())
    return total_sum


N, M, Q = map(int, input().split())
column_names = input().split()

table = []

for _ in range(N):
    row_values = input().split()
    row = {column_names[i]: int(row_values[i]) for i in range(M)}
    table.append(row)

conditions = []
for _ in range(Q):
    condition = input()
    conditions.append(condition)

result = evaluate_table(table, conditions)

print(result)
