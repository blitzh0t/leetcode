class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numeral = dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)
        prev = 0
        sum = 0
        for x in s:
            if prev == 0:
                prev = x
                sum = numeral[x]
            else:
                if numeral[x] <= numeral[prev]:
                    sum = sum + numeral[x]
                else:
                    sum = (sum - numeral[prev]) + (numeral[x] - numeral[prev])
            prev = x
        return sum