class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        k=-1 
        for i,x in enumerate(nums):
            if x!=i:
                k&=x
        return 0 if k==-1 else k