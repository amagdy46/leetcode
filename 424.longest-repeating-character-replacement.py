#
# @lc app=leetcode id=424 lang=python
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        count = {}
        l = 0
        maxF = 0

        for r in range(len(s)):
             count[s[r]] = 1 + count.get(s[r],0)
             maxF = max(maxF,count[s[r]])

             if (r-l+1) - maxF > k:
                count[s[l]]-=1
                l+=1
            
             res = max(res, r-l+1)
        return res
                

        
# @lc code=end

