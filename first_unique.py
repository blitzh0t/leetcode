class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = dict()
        for x in s:
            if x not in tmp:
                tmp[x] = 0
            tmp[x] += 1
        for k,v in enumerate(s):
            if tmp[v] == 1:
                return k
                break
        return -1