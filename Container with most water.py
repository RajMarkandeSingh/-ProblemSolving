class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        m=0
        while(l<r):
            if(height[l]<=height[r]):
                val=height[l]*abs(l-r)
                m=max(m,val)
                l+=1
            else:
                val=height[r]*abs(l-r)
                m=max(m,val)
                r-=1
        return m
