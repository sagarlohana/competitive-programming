class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = []
        self.permute2(nums, [], perms)
        return perms
    
    def permute2(self, nums, path, perms):
        # If no more combinations, return the add permutation to list
        if not nums:
            perms.append(path)
        # Iterate through each num and try each combination
        for i in range(len(nums)):
            self.permute2(nums[:i] + nums[i+1:], path + [nums[i]], perms)