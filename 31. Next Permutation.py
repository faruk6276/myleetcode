class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        array=len(nums)
        if array==1:
            return nums
        lastind=-1
        for index in range(1,array):
            if nums[index-1]<nums[index]:
                lastind=index
        
        if lastind==-1:
            return nums.sort()
        finalind=lastind
        for index in range(lastind+1,array):
            if nums[lastind-1]<nums[index] and nums[lastind]>nums[index]:
                finalind=index
        nums[finalind],nums[lastind-1]=nums[lastind-1],nums[finalind]
        nums[lastind:]=sorted(nums[lastind:])