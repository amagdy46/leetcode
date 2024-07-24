#
# @lc app=leetcode id=1360 lang=python
#
# [1360] Number of Days Between Two Dates
#

from datetime import datetime as dt


# @lc code=start
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        list1 = date1.split("-")
        list2 = date2.split("-")
        date1 = [int(i) for i in list1]
        date2 = [int(i) for i in list2]
        m = dt(date1[0], date1[1], date1[2])
        n = dt(date2[0], date2[1], date2[2])
        return abs((n - m).days)


# @lc code=end
