import heapq

k, n, m = map(int, input().split())
squares = {}
for _ in range(n):
    day, number = map(int, input().split())
    if number in squares:
        new_number = 0
        new_number = day - squares[number]['first']
        squares[number]['first'] = day
        squares[number]['arr'].append(new_number)
    else:
        squares[number] = {'first': day, 'arr': []}

if len(squares.keys()) > m:
    print(-1)

len_keys = len(squares.keys())

delete_keys = []
for key in squares.keys():
    if len(squares[key]['arr']) == 0:
        delete_keys.append(key)
for key in delete_keys:
    del squares[key]


def find_min_sum_multi(arrays, k):
    result = 0
    heap = []
    for arr in arrays:
        arr.sort()
        heapq.heappush(heap, (arr[0], 0, arr))
    print(heap)
    while k > 0 and heap:
        val, idx, arr = heapq.heappop(heap)
        result += val
        idx += 1
        if idx < len(arr):
            heapq.heappush(heap, (arr[idx], idx, arr))
        k -= 1
    return result


new_k = sum([len(squares[key]['arr']) for key in squares.keys()]) + (len_keys - m)
print(find_min_sum_multi([squares[key]['arr'] for key in squares.keys()], new_k))
