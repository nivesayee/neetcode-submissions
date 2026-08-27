import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        c = Counter(nums)
        for n,c in c.items():
            heapq.heappush(heap,(c,n))
            while len(heap)>k:
                heapq.heappop(heap)
        return [n[1] for n in heap]