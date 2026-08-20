class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i,v in enumerate(nums):
            if v in seen:
                return True
            else:
                seen[v] = i    
        return False

