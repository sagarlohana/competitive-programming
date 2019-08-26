class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        new_list = []
        for list_item in A:
            item_list = []
            for item in list_item:
                item_list.append((item + 1) % 2)
            new_list.append(item_list[::-1])
        return new_list
        