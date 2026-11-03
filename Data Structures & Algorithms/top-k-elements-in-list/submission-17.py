class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # Create a dictionary
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1

        # Create a heap and append things into it only keeping the top 3

        heap = []
        for key, value in count.items():
            heapq.heappush(heap,[value, key])
            if len(heap) > k:
                heapq.heappop(heap)

        # Loop through that heap and append the value into the result
        print(heap)
        res = []
        
        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1])

        return res