class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # Create a Frequency Dictionary
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        
        heap = []
        for key, value in count.items():
            heapq.heappush(heap, [value, key])
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res

        # Create res array