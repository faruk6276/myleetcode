class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx=0
        x=prices[0]
        for i in range(1,len(prices)):
            val=prices[i]-x
            if val>mx:
                mx=val
            elif prices[i]<x:
                x=prices[i]
        return mx