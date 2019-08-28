class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        nums.sort()
        for i in nums[::2]:
            count += i
        return count