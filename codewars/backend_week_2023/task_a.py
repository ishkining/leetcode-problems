n = int(input())
m = int(input())
cost_2 = int(input())
cost_5 = int(input())
min_cost = 0
if m > n:
    if cost_5 >= cost_2 * 5:
        min_cost = (m - n) * cost_2
    else:
        diff = m - n
        min_cost = min((((diff // 4) * cost_5) + cost_2 * (diff % 4)), ((diff // 4) + 1) * cost_5)
print(min_cost)
