class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(numbers)):
            val = numbers[i]
            if target-val in d:
                return [d[target-val]+1, i+1]
            d[val] = i