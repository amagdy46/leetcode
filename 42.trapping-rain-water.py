#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        res= 0
        l,r=0,len(height)-1
        lMax,rMax = height[l],height[r]

        while l<r:
            if lMax < rMax:
                l+=1
                lMax = max(lMax,height[l])
                res+= lMax - height[l]
            else:
                r-=1
                rMax = max(rMax,height[r])
                res+= rMax - height[r]
        return res

        
# @lc code=end

