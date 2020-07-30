class Solution(object):
    def runningSum(self, nums):
        output=[]
        a=0
        for i in nums:
            a = a+i
            output.append(a)
        return output
        """
        :type nums: List[int]
        :rtype: List[int]
        """
"""
Runtime: 32 ms, faster than 59.31% of Python online submissions for Running Sum of 1d Array.
Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Running Sum of 1d Array.
"""
