class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        heap = []
        for key, val in counts.items():
            heapq.heappush(heap,(val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [key for (val, key) in heap]