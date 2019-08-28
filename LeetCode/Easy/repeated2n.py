class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return (sum(A) - sum(set(A))) // (len(A)//2 - 1)