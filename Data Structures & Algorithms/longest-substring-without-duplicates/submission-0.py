class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, r = 0, 1
        res = 0

        for r in range(len(s)):
            ## because we need to check if theres duplicates so if it's already in there we need to REMOVE IT!! 
            ## and add the l += 1 so we can keep shrinking from the left side...
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res


        