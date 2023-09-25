def apply_conditions(table, conditions):
    result = 0
    for row in table:
        valid = True
        for condition in conditions.items():
            column = condition[0]
            value_great = condition[1].get('<', float('inf'))
            value_less = condition[1].get('>', float('-inf'))
            if row[column] <= value_less:
                valid = False
                break
            if row[column] >= value_great:
                valid = False
                break
        if valid:
            result += sum(row.values())
    return result


N, M, Q = map(int, input().split())

columns = input().split()

table = []
for _ in range(N):
    row = dict(zip(columns, map(int, input().split())))
    table.append(row)

conditions = {}

for _ in range(Q):
    column, operator, value = input().split()
    value = int(value)
    conditions[column] = conditions.get(column, {})
    conditions[column][operator] = max(value, conditions[column].get(operator, float('-inf'))) if operator == '>' \
        else min(value, conditions[column].get(operator, float('inf')))

result = apply_conditions(table, conditions)
print(result)
