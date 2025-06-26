class Solution(object):
    def longestSubsequence(self, s, k):
        c=0
        v=0
        m=1
        for i in range(len(s)-1,-1,-1):
            d=int(s[i])
            if d==1:
                if m>k:
                    continue
                if v+m<=k:
                    v+=m
                    c+=1
            else:
                c+=1
            m*=2
        return c
