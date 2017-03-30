class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        tmpList = list(range(1,n+1))
        for x in range(n):
            if tmpList[x] % 15 == 0:
                tmpList[x] = 'FizzBuzz'
            elif tmpList[x] % 5 == 0:
                tmpList[x] = 'Buzz'
            elif tmpList[x] % 3 == 0:
                tmpList[x] = 'Fizz'
            else:
                continue
        return [str(x) for x in tmpList]