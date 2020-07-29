class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        wordlist = list(s)
        
        for i,si in enumerate(indices):
            
            wordlist[si] = s[i]
        return "".join(wordlist)
"""
Runtime: 48 ms, faster than 62.61% of Python online submissions for Shuffle String.
Memory Usage: 12.9 MB, less than 19.14% of Python online submissions for Shuffle String.
"""
