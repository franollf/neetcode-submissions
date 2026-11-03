class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # Create a count 

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Using a heap 
        heap = []
        res = []
        # Loop through heap and create 
        for key in count.keys():
            heapq.heappush(heap,[count[key], key])
            # Pops everyting 
            if len(heap) > k:
               heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


        