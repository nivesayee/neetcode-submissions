class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        refer_dict = dict()
        for i in nums:
            if refer_dict.get(i,0) != 0:
                return True
            else:
                refer_dict[i] = 1
        return False