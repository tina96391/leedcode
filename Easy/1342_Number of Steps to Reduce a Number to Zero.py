class Solution(object):
    def numberOfSteps (self, num):
        count=0
        while (num!=0):
            if (num%2== 0):
                num=num/2
            else:
                num=num-1
            count=count+1
        return count
"""
Runtime: 32 ms, faster than 11.90% of Python online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 12.7 MB, less than 75.99% of Python online submissions for Number of Steps to Reduce a Number to Zero.
"""
