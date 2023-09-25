import heapq


def halve_array(nums: list[int]) -> int:
    target = sum(nums) / 2
    heap = [-num for num in nums]
    heapq.heapify(heap)

    result = 0
    while target > 0:
        max_el = heapq.heappop(heap)
        target += max_el / 2
        heapq.heappush(heap, max_el / 2)
        result += 1
    return result