class Solution(object):
    # Find sum of 2 * set of nums and subtract sum of nums to find non-duplicate val
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums)) - sum(nums)
    # Xor each number in nums and the result is the non-duplicate val
    def singleNumber(self, nums):
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]