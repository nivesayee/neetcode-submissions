class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        CharS = {}
        CharT = {}
        for i in range(len(s)):
            CharS[s[i]] = 1 + CharS.get(s[i], 0)
            CharT[t[i]] = 1 + CharT.get(t[i], 0)

        for i in CharS:
            if CharT.get(i) != CharS[i]:
                return False
        return True 