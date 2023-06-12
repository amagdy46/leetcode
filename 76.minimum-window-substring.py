#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t=="": return ""

        countT,window= {},{}
        have,need=0,len(t)
        res,resLen=[0,0],float('infinity')
        l=0
        for c in t:
            countT[c]=1+countT.get(c,0)
        
        for r in range(len(s)):
            c = s[r]
            window[c]=1+window.get(c,0)

            if c in countT and window[c] <= countT[c]: # why <= and not ==
                have+=1
            while have==need:
                if (r-l+1)<resLen:
                    res = [l,r]
                    resLen=r-l+1
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen!=float("infinity") else ""
        
        
# @lc code=end

