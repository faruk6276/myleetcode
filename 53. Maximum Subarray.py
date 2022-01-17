class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sm=nums[0]
        if len(nums)==1:
            return sm
        mx=sm
        for i in range(1,len(nums)):
            if sm+nums[i]<nums[i]:
                sm=nums[i]
            else:
                sm+=nums[i]
            mx=max(mx,sm)
        return mx