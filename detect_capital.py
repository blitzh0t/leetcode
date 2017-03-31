class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
#        this was my first solution , but run time was very slow
#        if word == word.upper() or word == word.lower() or word == word.capitalize():
#            return True
#        else:
#            return False
        return word.isupper() or word.islower() or word.istitle()