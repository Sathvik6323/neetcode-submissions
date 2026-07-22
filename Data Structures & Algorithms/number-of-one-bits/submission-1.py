class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res+=n%2
            n=n>>1
        #or you can do n & (n-1)  and res+=1 this wil only run for as many as 1s are ther ein the code 
        return res
        