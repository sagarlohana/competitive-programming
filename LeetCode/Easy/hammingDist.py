class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]
        len_x = len(bin_x)
        len_y = len(bin_y)
        if len_x > len_y:
            bin_y = bin_y.rjust(len_x, '0')
        else:
            bin_x = bin_x.rjust(len_y, '0')
        count = 0
        for i in range(len(bin_x)):
            if bin_x[i] != bin_y[i]:
                count += 1
        return count
    def hammingDistance(self, x, y):
        return bin(x^y).count(1)