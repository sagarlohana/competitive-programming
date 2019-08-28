class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l, r = 0, len(S)
        new_list = []
        for c in S:
            if c == 'I':
                new_list.append(l)
                l += 1
            else:
                new_list.append(r)
                r -= 1
        new_list.append(r)
        return new_list