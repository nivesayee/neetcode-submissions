class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seendict = {}
        for i,v in enumerate(numbers):
            n = target - v
            if n in seendict:
                return [seendict[n], i+1]
            else:
                seendict[v] = i+1