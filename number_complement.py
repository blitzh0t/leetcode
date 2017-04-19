class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        #this works , but slow
        return int(''.join([('1' if int(x) == 0 else '0') for x in bin(num)[2:]]),2)