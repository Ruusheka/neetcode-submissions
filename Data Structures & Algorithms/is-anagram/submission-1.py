class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)==sorted(t)
        if len(s)!=len(t):
            return False
        n=len(s)
        cntS,cntT={},{}

        for i in range(n):
            cntS[s[i]]=1+cntS.get(s[i],0)
            cntT[t[i]]=1+cntT.get(t[i],0)
        
        for j in cntS:
            if cntS[j]!=cntT.get(j,0):
                return False
        
        return True