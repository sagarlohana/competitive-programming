class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        transformList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        uniqList = set()
        for word in words:
            s = ""
            for c in word:
                s += transformList[ord(c) - ord('a')]
            uniqList.add(s)
        return len(uniqList)