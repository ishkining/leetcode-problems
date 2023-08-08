t = int(input())
x = []
for _ in range(t):
    x.append(int(input()))

for element in x:
    arr_number = [int(number) for number in str(element)]
    change_index = None
    for index in range(len(arr_number) - 1, -1, -1):
        if arr_number[index] > 4:
            change_index = index
            if index != 0:
                arr_number[index] = 0
                arr_number[index - 1] = arr_number[index - 1] + 1
            else:
                arr_number[0] = 10

    if change_index is not None:
        for index in range(change_index + 1, len(arr_number)):
            arr_number[index] = 0
    # result.append(int(''.join([str(number) for number in arr_number])))
    print(int(''.join([str(number) for number in arr_number])))
    change_index = None
