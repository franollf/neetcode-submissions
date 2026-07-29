class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        # Make an array for the length of how many nums there are called frequency
        freq = [[] for i in range(len(nums) + 1)]

        # Iterate through the numbers
        for num in nums:
        # Get the number of how many times that number has appeared
            count[num] = 1 + count.get(num, 0)
        # Put your findings onto the freq array
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        # Iterate through freq backwards (to get the highest value first)
        for i in range(len(freq)- 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        