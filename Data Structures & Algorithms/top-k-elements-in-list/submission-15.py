class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # Create a count 

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Using a heap 
        heap = []
        res = []
        # Create our heap 
        for key, value in count.items():
            heapq.heappush(heap,[value, key])
            # Pops everyting 
            if len(heap) > k:
               heapq.heappop(heap)

        # Looping through to append the key to your res
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


        