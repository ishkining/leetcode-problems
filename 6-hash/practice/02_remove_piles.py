import heapq
from typing import List
from math import floor


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)

        for _ in range(k):
            heapq.heappush(heap, floor(heapq.heappop(heap) / 2))

        return -sum(heap)
