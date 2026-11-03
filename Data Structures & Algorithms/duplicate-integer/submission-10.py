class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Distinct and more than once in an array
        # It's a set


        seen = set()

        for n in nums:
            if n in seen:
                return True

            seen.add(n)

        return False