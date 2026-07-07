class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        cntS,Cnt_t={},{}
        for i in range(len(s)):
            cntS[s[i]]=1+cntS.get(s[i],0)
            Cnt_t[t[i]]=1+Cnt_t.get(t[i],0)
        #check for the count
        for i in cntS:
            if cntS[i]!=Cnt_t.get(i, 0):
                return False
        return True