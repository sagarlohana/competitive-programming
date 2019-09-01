class Solution(object):
    # Pushing all non-zero elements to the front and tracking index of zero positions
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
        return nums
    
    # Tracking zero position and swapping zero and non-zero elems
    def moveZeroes(self, nums):
        zero_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
                zero_pos += 1
        return nums