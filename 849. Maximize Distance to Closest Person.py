class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        mx=0
        last=0
        for i in range(len(seats)):
            if seats[i]==1 and seats[last]==1:
                mx=max(mx,(i-last)//2)
                last=i
            elif seats[i]==1:
                mx=max(mx,i-last//2)
                last=i
            elif i==len(seats)-1:
                mx=max(mx,i-last)
        return mx