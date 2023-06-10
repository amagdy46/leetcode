#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
import collections


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols =  collections.defaultdict(set)
        rows =  collections.defaultdict(set)
        squares =  collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                curr= board[r][c]
                if curr =='.':
                    continue 
                if curr in rows[r] or curr  in cols[c] or curr in squares[(r//3,c//3)]:
                    return False 
                cols[c].add(curr)
                rows[r].add(curr)
                squares[((r//3,c//3))].add(curr)
        return True 
# @lc code=end

