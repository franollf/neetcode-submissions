class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Create a left and right pointer
        l = 0
        r = len(nums) - 1



        # Basically you're trying to find the minimum number in the sorted array 
        # So you're going to continuely to binary search 

        while l < r:
            # make your middle
            m = (l + r) // 2
            # If the middle is less than the right pointer 

            # It takes it ONLY if its less than
            if nums[m] < nums[r]:
                r = m
            # and when they touch it only returns one value whoch is the miniumum
            else:
                l = m + 1

        return nums[l]

