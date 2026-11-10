class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # In a sorted array, one half of the array HAS to be sorted
        l , r = 0, len(nums) - 1


        while l <= r:
            # Get your mid search
            m = (l + r) // 2
            if target == nums[m]:
                return m
            # CASE A: The left approach is sorted 
            if nums[l] <= nums[m]:
                # 1.  If its greater than m than its on the right
                #2. If it's less than the most left pointer than its been rotated and its also on the right because we know that from left pointer to mid that it is sorted
                if target > nums[m] or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1

            # CASE B: The right approach is completely sorted
            else: 
                # 1. If the target is less than the middle than its going to be in the left portion because the right is completely sorted
                # 2. 
                if target < nums[m] or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1

        return -1


