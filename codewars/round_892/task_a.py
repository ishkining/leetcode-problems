for _ in range(int(input())):
    n = int(input())
    sub_arr = sorted([int(number) for number in input().split(' ')])
    if sub_arr[0] == 1:
        counter = 1
        while counter != len(sub_arr) and sub_arr[counter] == 1:
            counter += 1

        if len(sub_arr) == counter:
            print(-1)
        else:
            print(counter, len(sub_arr[counter:]))
            print(*[1 for _ in range(counter)])
            print(*sub_arr[counter:])
    else:
        last_element = sub_arr.pop()
        c = [last_element]
        while len(sub_arr) and last_element == sub_arr[-1]:
            c.append(sub_arr.pop())

        is_divided = False
        for number in sub_arr:
            if number % last_element == 1:
                is_divided = True
                break

        if is_divided or len(sub_arr) == 0:
            print(-1)
        else:
            print(len(sub_arr), len(c))
            print(*sub_arr)
            print(*c)

