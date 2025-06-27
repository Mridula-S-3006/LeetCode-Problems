class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        '''c=0
        b=0
        for i in nums:
            if i==1:
                c+=1
            else:
                b=max(b,c)
                c=0
        return max(b,c)'''
        return len(max("".join(map(str,nums)).split("0")))
