class Solution(object):
    def findLucky(self, arr):
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=-1
        for i in d:
            if d[i]==i:
                l=max(l,i)
        return l