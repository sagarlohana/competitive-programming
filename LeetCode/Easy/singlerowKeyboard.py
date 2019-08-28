class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        curr = 0
        count = 0
        for c in word:
            count = count + abs(keyboard.index(c) - curr)
            curr = keyboard.index(c)
        return count