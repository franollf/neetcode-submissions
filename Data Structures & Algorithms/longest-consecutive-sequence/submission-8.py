class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Loop through seen
        seen = set(nums)
        # Check if the previous number is in there and if so then starting length 
        best = 0

        # Loop through set
        for x in seen:
            # If theres one before that doesn't exist then the length = 1
            # Because this is how we know something actually STARTS HERE
            if x - 1 not in seen:
                length = 1
                # Loop to check if the future is in there
                while x + length in seen:
                    length += 1
                    
                # Take the best of that 
                best = max(best, length)
                
        
        return best 
