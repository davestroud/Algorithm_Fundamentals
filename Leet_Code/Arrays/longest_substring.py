class Solution:
    '''
    >>> ob1 = Solution()
    >>> ob1.lengthOfLongestSubstring("ABCABCBB") 
    3
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range[i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans
    
    
# python3 -m doctest longest_substring.py ~ to run doc test