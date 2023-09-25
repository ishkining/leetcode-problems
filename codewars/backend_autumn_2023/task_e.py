n = int(input())

prefixes = {}

result = 0
for _ in range(n):
    k = int(input())
    arr = input().split()
    is_found = [False for _ in range(n)]
    for index in range(len(arr), 0, -1):
        joined_str = ' '.join(arr[:index])
        if joined_str in prefixes and not is_found[prefixes[joined_str]]:
            result += index * 1
            is_found[prefixes[joined_str]] = True
        prefixes[joined_str] = _

# print(prefixes)
print(result)

# result = 0
# for i in range(n):
#     for j in range(i+1, n):
#         for counter in range(min(len(all_arrays[i]), len(all_arrays[j])) + 1, -1, -1):
#             if all_arrays[i][:counter + 1] == all_arrays[j][:counter + 1]:
#                 result += counter + 1
#                 break
# print(result)
