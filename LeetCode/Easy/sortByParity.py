class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_list = []
        even_list = []
        for elem in A:
            odd_list.append(elem) if elem % 2 == 1 else even_list.append(elem)
        even_list.extend(odd_list)
        return even_list