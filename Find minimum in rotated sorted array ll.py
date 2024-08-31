from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        val = nums[0] 
        while l <= r:
            m = (l + r) // 2
            if nums[l] == nums[m] and nums[m] == nums[r]:
                val=min(val,nums[l])
                l += 1
                r -= 1
                continue
            if nums[l] <= nums[m]:
                val = min(val, nums[l])
                l = m + 1
            else: 
                val = min(val, nums[m])
                r = m - 1
        return val
