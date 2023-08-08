for _ in range(int(input())):
    n = int(input())
    a = sorted([int(number) for number in input().split(' ')])
    result = []
    index = 0
    for i in range(n - 1):
        result.append(a[index])
        index += n - 1 - i
    result.append(a[-1])
    print(*result)