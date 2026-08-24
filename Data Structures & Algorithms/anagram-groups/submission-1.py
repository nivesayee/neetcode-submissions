class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            charlist = [0]*26
            for c in s:
                charlist[ord(c)-ord('a')]+=1
            result[tuple(charlist)].append(s)
        return list(result.values())