#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r=0,len(numbers)-1
        
        while l<r:
            if  numbers[l] + numbers[r] <target:
                l+=1
            elif  numbers[l] + numbers[r] >target:
                r-=1
            else:
                return [l+1,r+1]
        
# @lc code=end

