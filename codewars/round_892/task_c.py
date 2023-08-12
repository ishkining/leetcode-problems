for _ in range(int(input())):
    n = int(input())
    start = [number for number in range(1, n)]
    end_part = [n]
    sum_number = 0
    for _ in range(n-1):
        end_part.append(start.pop())
        temp_arr = [(number+1)*i for number, i in enumerate(start + end_part)]
        # print(temp_arr)
        temp_sum = sum(temp_arr) - max(temp_arr)
        # print(temp_sum)
        if temp_sum > sum_number:
            sum_number = temp_sum
        else:
            break
    print(sum_number)


