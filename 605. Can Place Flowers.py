class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for index in range(len(flowerbed)):
                if flowerbed[index]==0 and (flowerbed[index-1]==0 or index==0) and (index==(len(flowerbed)-1)  or flowerbed[index+1]==0):
                    flowerbed[index]=1
                    n-=1
        return True if n<1 else False