class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        ## Loop through words in array and create 
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
                # Need to append as tuple with the word

            res[tuple(count)].append(s)

        return list(res.values())