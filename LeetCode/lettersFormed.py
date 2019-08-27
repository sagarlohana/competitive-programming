class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        count = 0
        for word in words:
            contained = True
            char_list = [letter for letter in chars]
            for c in word:
                if c in char_list:
                    char_list.remove(c)
                else:
                    contained = False
                    break
            if contained:
                count += len(word)
        return count