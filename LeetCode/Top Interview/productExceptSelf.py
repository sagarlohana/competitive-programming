class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        # Create an initial array of 1's
        for i in range(len(nums)):
            res.append(1)
        left = 1
        # Multiply each of the left products
        for i in range (len(nums)):
            res[i] = left
            left *= nums[i]
        right = 1
        # Multiply each of the right products
        for i in range (len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
        # For reference: https://www.programcreek.com/2014/07/leetcode-product-of-array-except-self-java/