n, k = map(int, input().split())

a = [tuple(map(int, input().split())) for _ in range(n)]

a = sorted(a, key=lambda x: x[0])
print(a)
min_unevenness = float('inf')
start = 0
int_start, int_end = 0, 0
while start + n - k <= n:
    print(a[start + n - k - 1][0], a[start][0])
    # print(a[start + n - k - 1][0] - a[start][0])
    unevenness = a[start + n - k - 1][0] - a[start][0]
    if unevenness < min_unevenness:
        int_end, int_start = start + n - k - 1, start
        min_unevenness = unevenness
    start += 1

min_max = {}
for new_tuple in a[int_start:int_end + 1]:
    if new_tuple[1] in min_max:
        min_max[new_tuple[1]].append(new_tuple[0])
    else:
        min_max[new_tuple[1]] = [new_tuple[0]]

result_sum = 0
for key in min_max.keys():
    if len(min_max[key]) == 1:
        pass
    result_sum += min_max[key][-1] - min_max[key][0]

print(min_max)
print(result_sum)
