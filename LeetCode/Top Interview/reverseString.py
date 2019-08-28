class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        j, k = 0, len(s) - 1
        while(j < k):
            s[j], s[k] = s[k], s[j]
            j += 1
            k -= 1
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()
    