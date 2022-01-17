class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
  
        count={}
        csum=0
        res=0

        for n in nums:
            
            csum += n
            if csum==k:   
                res+=1
            if csum-k in count: 
                res+=count[csum-k]
            
            if csum in count:
                count[csum]+=1
            else:
                count[csum]=1

        return res