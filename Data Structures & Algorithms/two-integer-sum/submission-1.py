class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seendict = {}
        for i,v in enumerate(nums):
            n = target - v
            if n in seendict:
                return [seendict[n],i]
            else:
                seendict[v] = i