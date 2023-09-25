import heapq
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            distance = -1 * sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(heap, (distance, point))
            if len(heap) > k:
                heapq.heappop(heap)
        return [el[1] for el in heap]