class Solution(object):
    def findLHS(self, nums):
        c=0
        f=Counter(nums)
        for i in f:
            if i+1 in f:
                c=max(c,f[i]+f[i+1])
        return c 
