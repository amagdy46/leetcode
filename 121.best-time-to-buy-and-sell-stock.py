#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r = 0,1
        maxP= 0

        while r < len(prices):
            if prices[l] < prices[r]:
                p = prices[r]-prices[l]
                maxP = max(maxP,p)
            else:
                l=r
            r+=1 
        return maxP

        
# @lc code=end

