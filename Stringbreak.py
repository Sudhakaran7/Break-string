class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        l1 = sorted(list(s1))
        l2 = sorted(list(s2))

        res = True
        for i,j in zip(l1,l2):
            if i < j:
                res = False
                break
        if res : return res

        res = True
        for i,j in zip(l1,l2):
            if i > j:
                res = False
                break

        return res
val=Solution()
a,b=map(str,input().split())
print(val.checkIfCanBreak(a,b))
