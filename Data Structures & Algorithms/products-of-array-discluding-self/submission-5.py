class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Start with creating an array same length
        ans = [1] * n

        left = 1
        # Calculate the product of every number to the left
        for i in range(n):
            ans[i] = left
            left *= nums[i]
        # Calculate the number of every number to the right
        right = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right
            right *= nums[i]

    
        return ans

