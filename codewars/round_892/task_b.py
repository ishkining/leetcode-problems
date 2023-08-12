for _ in range(int(input())):
    n = int(input())
    data = []
    for _ in range(n):
        _t = int(input())
        data.append(sorted([int(number) for number in input().split(' ')])[:2])
    data = sorted(data, key=lambda x: x[1])
    result = min([sub_arr[0] for sub_arr in data])
    for sub_arr in data[1:]:
        result += sub_arr[1]
    print(result)

