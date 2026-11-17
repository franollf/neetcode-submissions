class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = maxf = 0

        # Loop through the string s
        for r in range(len(s)):
            # Get the frequency for each letter
            count[s[r]] = 1 + count.get(s[r], 0)
            # Always Take the max frequency in the list
            maxf = max(maxf, count[s[r]])
            # If the window that it's set to currently subtracted by the max frequency is greater than the limit k which means that it's
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
