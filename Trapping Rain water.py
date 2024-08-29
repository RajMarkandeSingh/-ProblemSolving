class Solution:
    def trap(self, height: List[int]) -> int:
        w=0
        l=0
        r=len(height)-1
        lm=height[l]
        rm=height[r]
        h=0
        while(l<r):
            if(lm<rm):
                l+=1
                lm=max(lm,height[l])
                h+=lm-height[l]
            else:
                r-=1
                rm=max(rm,height[r])
                h+=rm-height[r]
        return h
