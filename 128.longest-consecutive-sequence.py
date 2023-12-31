#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet= set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                length=0
                while (n+length) in numSet:
                    length+=1
                longest = max(length,longest)
        return longest

        
# @lc code=end

