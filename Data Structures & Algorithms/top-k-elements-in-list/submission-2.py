class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        items = [(-val, key) for (key,val) in counts.items()]
        heapq.heapify(items)
        return [heapq.heappop(items)[1] for _ in range(k)]