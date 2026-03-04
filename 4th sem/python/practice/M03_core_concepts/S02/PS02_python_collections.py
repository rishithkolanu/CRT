#  Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        c = 0
        for i in nums:
            c += i
            res.append(c)
        return res    