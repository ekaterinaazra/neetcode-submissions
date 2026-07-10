class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        
        for num in nums:
            x = 0
            if num not in dic:
                dic[num] = 0
            else:
                return True
        return False

        