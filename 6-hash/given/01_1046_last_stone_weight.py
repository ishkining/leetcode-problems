import heapq


def last_stone_weight(stones: list[int]) -> int:
    stones = [-stone for stone in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = abs(heapq.heappop(stones))
        second = abs(heapq.heappop(stones))
        if first != second:
            heapq.heappush(stones, -abs(first - second))

    return -stones[0] if len(stones) == 1 else 0