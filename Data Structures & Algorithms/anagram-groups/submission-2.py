class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs: # loop through the word
            count = [0] * 26 # create an array for each letter
            for c in s: # for each letter in the word
                count[ord(c) - ord('a')] += 1 ## add it into the array
            res[tuple(count)].append(s) #append the word to that value in the dictionary
        return list(res.values()) # return the list of values from the res as a list



        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())