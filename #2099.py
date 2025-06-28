class Solution(object):
    def maxSubsequence(self, nums, k):
        ind=[]
        for i,j in enumerate(nums):
            ind.append((j,i))
        tk=sorted(ind,key=lambda x:x[0],reverse=True)[:k]
        tk=sorted(tk,key=lambda x:x[1])
        return [i for i,j in tk]
