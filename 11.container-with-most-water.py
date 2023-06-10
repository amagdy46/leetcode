#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res=0
        l,r=0,len(height)-1

        while l<r:
            area = (r-l) * min(height[r],height[l])
            res = max(res,area)
            if height[r] < height[l]:
                r-=1
            else:
                l+=1
        return res
        
# @lc code=end

