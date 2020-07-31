class Solution(object):
    def shuffle(self, nums, n):
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
"""
簡單的思路，向後n個一起append就好
Runtime: 68 ms, faster than 31.06% of Python online submissions for Shuffle the Array.
Memory Usage: 12.8 MB, less than 47.87% of Python online submissions for Shuffle the Array.
"""
