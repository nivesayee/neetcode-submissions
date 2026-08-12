class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = dict()
        tdict = dict()
        for i in s:
            sdict[i] = sdict.get(i,0) + 1
        for j in t:
            tdict[j] = tdict.get(j,0) + 1
        if sdict == tdict:
            return True
        else:
            return False