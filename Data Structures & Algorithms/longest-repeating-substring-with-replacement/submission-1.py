class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start=0
        state={}
        max_freq = 0
        max_len=0

        for end in range(len(s)):
            state[s[end]]=state.get(s[end],0)+1
            max_freq=max(max_freq,state[s[end]])

            if (end-start+1)-max_freq >k:
                state[s[start]]-=1
                start+=1
            max_len = max(max_len,end-start+1)
        return max_len

        