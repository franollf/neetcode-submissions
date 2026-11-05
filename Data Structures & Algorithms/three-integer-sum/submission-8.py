class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array
        nums.sort()

        res = []

        # Iterate through array to check for triplets
        for i in range(len(nums) - 2):
            # Once anchor reaches to postive loop ends
            if nums[i] > 0:
                break

            # Skip duplicate anchor
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Set your pointers
            left, right = i + 1, len(nums) - 1

            while left < right:
                # Make total
                total = nums[i] + nums[left] + nums[right]

                # Raise left to closer to 0
                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    res.append([nums[left], nums[i], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res



