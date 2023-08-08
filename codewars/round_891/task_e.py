t = int(input())

x = []
for _ in range(t):
    n = int(input())
    str_array = input().split(' ')
    # x.append([int(number) for number in str_array])
    array = sorted([(int(str_array[index]), index) for index in range(len(str_array))])
    x.append(array)

print(x)
subtracted_arr = []
for arr in x:
    some_result = []
    for index in range(len(arr) - 1):
        result = arr[index + 1][0] - arr[index][0]
        some_result.append(result)
    subtracted_arr.append(some_result)
print(subtracted_arr)
