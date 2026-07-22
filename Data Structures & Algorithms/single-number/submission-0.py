class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = 0
        for n in nums:
            res ^= n  # Cancels out all duplicate pairs, leaving the single number
        return res


        