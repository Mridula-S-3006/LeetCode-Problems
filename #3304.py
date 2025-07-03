class Solution(object):
    def kthCharacter(self, k):
        w='a'
        while len(w)<=k:
            g=''
            for i in w:
                g+=chr(ord(i)+1)
            w+=g
        return w[k-1]