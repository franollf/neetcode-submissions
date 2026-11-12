class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1


        while l < r:
            # Make hte middle

            m = (l + r) // 2
            
            # Check if the pointers are less than the left or the right 
            if nums[m] <= nums[r]:
                r = m

            else:
                l = m + 1

        return nums[l]