class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            m=l+((r-l)//2)
            if nums[m]<target:
                l=m+1
            elif nums[m]==target:
                return m
            else:
                r=m-1

            
        return l if (l<len(nums) and nums[l]==target) else -1
        