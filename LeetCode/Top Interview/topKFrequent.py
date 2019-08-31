class Solution(object):
    # class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = {}
        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res[num] += 1
            
        # Sort dict by frequency in reverse order in arr 
        arr = sorted(res, key = res.get, reverse=True)
        return arr[:k]