class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        mp = {}
        
        i = 0 
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]])
                
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1
        return ans
    
