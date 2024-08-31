from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        val = []
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                val.append(m)
                
                for i in range(m - 1, l - 1, -1):
                    if nums[i] == target:
                        val.insert(0, i)
                    else:
                        break
                
                for i in range(m + 1, r + 1):
                    if nums[i] == target:
                        val.append(i)
                    else:
                        break
                
                return [val[0], val[-1]]
            
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return [-1, -1]
