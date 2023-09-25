import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [1]
        self.k = 1
        self.added = {}

    def popSmallest(self) -> int:
        el = heapq.heappop(self.heap)
        if el in self.added:
            del self.added[el]
        else:
            self.k += 1
            heapq.heappush(self.heap, self.k)
        return el

    def addBack(self, num: int) -> None:
        if num < self.k and num not in self.added:
            self.added[num] = True
            heapq.heappush(self.heap, num)
