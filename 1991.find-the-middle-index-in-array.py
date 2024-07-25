#
# @lc app=leetcode id=1991 lang=python
#
# [1991] Find the Middle Index in Array
#


# @lc code=start
class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        sum1 = 0
        for i in range(len(nums)):
            sum2 = total_sum - sum1 - nums[i]
            if sum1 == sum2:
                return i
            sum1 += nums[i]

        return -1


# @lc code=end
