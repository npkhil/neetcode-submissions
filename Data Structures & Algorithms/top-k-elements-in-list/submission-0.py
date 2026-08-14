class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        heap = []
        for key, value in counts.items():
            heapq.heappush(heap, (value, key))
        return [key for value, key in heapq.nlargest(k, heap)]
 