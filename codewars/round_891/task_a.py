t = int(input())
a = []
for _ in range(t):
    n = int(input())
    a.append(sum([int(number) for number in input().split(' ')]))

for element in a:
    if element % 2 == 0:
        print('YES')
    else:
        print('NO')
