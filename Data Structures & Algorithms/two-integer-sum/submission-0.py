class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i,v in enumerate(nums):
            n = target - v
            if n in d:
                return [d[n], i]
            else:
                d[v] = i
            
